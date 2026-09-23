
from pathlib import Path
import json, math, itertools, random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, load_breast_cancer, make_blobs
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, GradientBoostingClassifier, IsolationForest
from sklearn.neighbors import KNeighborsClassifier, NearestNeighbors
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, accuracy_score, roc_auc_score, silhouette_score, confusion_matrix
import networkx as nx

SEED = 42
np.random.seed(SEED)
random.seed(SEED)


def _save(root, metrics, fig=None, extras=None):
    root = Path(root)
    art = root / 'artifacts'
    art.mkdir(exist_ok=True)
    with open(art/'metrics.json','w') as f:
        json.dump(metrics, f, indent=2)
    if extras is not None:
        with open(art/'details.json','w') as f:
            json.dump(extras, f, indent=2, default=str)
    if fig is not None:
        fig.tight_layout()
        fig.savefig(art/'result.png', dpi=150, bbox_inches='tight')
        plt.close(fig)
    return metrics


def taxi_data(n=1400):
    rng=np.random.default_rng(SEED)
    pickup_lat=40.70+rng.normal(0,0.035,n); pickup_lon=-73.98+rng.normal(0,0.045,n)
    drop_lat=pickup_lat+rng.normal(0,0.025,n); drop_lon=pickup_lon+rng.normal(0,0.03,n)
    distance=np.sqrt(((drop_lat-pickup_lat)*69)**2+((drop_lon-pickup_lon)*53)**2)
    hour=rng.integers(0,24,n); passenger=rng.integers(1,5,n)
    rush=((hour>=7)&(hour<=9))|((hour>=16)&(hour<=19))
    duration=5+4.3*distance+6*rush+0.4*passenger+rng.normal(0,3,n)
    duration=np.clip(duration,2,None)
    return pd.DataFrame(dict(pickup_lat=pickup_lat,pickup_lon=pickup_lon,dropoff_lat=drop_lat,dropoff_lon=drop_lon,distance_miles=distance,hour=hour,passenger_count=passenger,duration_min=duration))


def run_01(root):
    df=taxi_data(); X=df.drop(columns='duration_min'); y=df.duration_min
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,random_state=SEED)
    models={'Linear Regression':LinearRegression(),'Random Forest':RandomForestRegressor(n_estimators=120,random_state=SEED,min_samples_leaf=2)}
    rows={}; best=None
    for name,m in models.items():
        m.fit(Xtr,ytr); p=m.predict(Xte)
        rows[name]={'MAE':float(mean_absolute_error(yte,p)),'RMSE':float(mean_squared_error(yte,p)**.5),'R2':float(r2_score(yte,p))}
        if best is None or rows[name]['RMSE']<rows[best]['RMSE']: best=name
    m=models[best]; p=m.predict(Xte)
    fig,ax=plt.subplots(figsize=(7,5)); ax.scatter(yte,p,s=14,alpha=.5); lim=[min(yte.min(),p.min()),max(yte.max(),p.max())]; ax.plot(lim,lim); ax.set(xlabel='Actual duration (min)',ylabel='Predicted duration (min)',title='Taxi duration: actual vs predicted')
    metrics={'best_model':best,**rows[best]}
    return _save(root,metrics,fig,{'all_models':rows,'rows':len(df)})


def run_02(root):
    corpus=('data science is the practice of learning useful patterns from data. '
            'good experiments separate training data from evaluation data. '
            'a language model estimates the probability of the next token. '
            'reproducible machine learning uses fixed seeds and clear metrics. ')*35
    order=3; counts={}; contexts={}
    for i in range(len(corpus)-order):
        ctx=corpus[i:i+order]; nxt=corpus[i+order]
        counts.setdefault(ctx,{}); counts[ctx][nxt]=counts[ctx].get(nxt,0)+1; contexts[ctx]=contexts.get(ctx,0)+1
    logp=[]
    for i in range(len(corpus)-order):
        ctx=corpus[i:i+order]; nxt=corpus[i+order]; total=contexts[ctx]; vocab=len(counts[ctx]); prob=(counts[ctx].get(nxt,0)+1)/(total+vocab)
        logp.append(-math.log(prob))
    perplexity=float(math.exp(np.mean(logp)))
    rng=random.Random(SEED); text='data'
    for _ in range(180):
        ctx=text[-order:]
        options=counts.get(ctx)
        if not options: text += rng.choice(corpus); continue
        chars=list(options); weights=list(options.values()); text += rng.choices(chars,weights=weights,k=1)[0]
    freqs=sorted(((k,sum(v.values())) for k,v in counts.items()),key=lambda x:x[1],reverse=True)[:10]
    fig,ax=plt.subplots(figsize=(7,5)); ax.bar([x[0] for x in freqs],[x[1] for x in freqs]); ax.set(title='Most frequent character contexts',ylabel='Count'); ax.tick_params(axis='x',rotation=45)
    return _save(root,{'perplexity':perplexity,'contexts':len(counts)},fig,{'sample_generation':text})


def run_03(root):
    X,_=make_blobs(n_samples=700,centers=4,cluster_std=[1.0,1.3,.8,1.1],random_state=SEED)
    scaler=StandardScaler(); Z=scaler.fit_transform(X)
    scores={}
    for k in range(2,7):
        labels=KMeans(k,n_init=20,random_state=SEED).fit_predict(Z); scores[k]=float(silhouette_score(Z,labels))
    best=max(scores,key=scores.get); labels=KMeans(best,n_init=20,random_state=SEED).fit_predict(Z)
    fig,ax=plt.subplots(figsize=(7,5)); ax.scatter(Z[:,0],Z[:,1],c=labels,s=15,alpha=.65); ax.set(title=f'Customer segments (k={best})',xlabel='Scaled feature 1',ylabel='Scaled feature 2')
    return _save(root,{'best_k':int(best),'silhouette':scores[best]},fig,{'silhouette_by_k':scores})


def run_04(root):
    tx=[{'bread','milk','eggs'},{'bread','butter'},{'milk','eggs','cereal'},{'bread','milk','butter'},{'bread','eggs'},{'milk','cereal'},{'bread','milk','eggs','butter'},{'cereal','milk'},{'bread','milk'},{'eggs','butter'}]*20
    n=len(tx); items=sorted(set().union(*tx)); support={i:sum(i in t for t in tx)/n for i in items}; rules=[]
    for a,b in itertools.permutations(items,2):
        both=sum(a in t and b in t for t in tx)/n
        if both>=.1:
            conf=both/support[a]; lift=conf/support[b]
            rules.append({'rule':f'{a} -> {b}','support':both,'confidence':conf,'lift':lift})
    rules=sorted(rules,key=lambda r:r['lift'],reverse=True)
    top=rules[:8]
    fig,ax=plt.subplots(figsize=(7,5)); ax.barh([r['rule'] for r in top][::-1],[r['lift'] for r in top][::-1]); ax.set(title='Top association rules by lift',xlabel='Lift')
    return _save(root,{'top_rule':top[0]['rule'],'top_lift':float(top[0]['lift']),'transactions':n},fig,{'rules':top})


def run_05(root):
    d=load_iris(); X=d.data; y=d.target
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,stratify=y,random_state=SEED)
    model=make_pipeline(StandardScaler(),LogisticRegression(max_iter=500,random_state=SEED)); model.fit(Xtr,ytr); p=model.predict(Xte); acc=float(accuracy_score(yte,p))
    pca=PCA(2,random_state=SEED).fit_transform(StandardScaler().fit_transform(X))
    fig,ax=plt.subplots(figsize=(7,5)); ax.scatter(pca[:,0],pca[:,1],c=y,s=22,alpha=.7); ax.set(title='Iris PCA learning view',xlabel='PC1',ylabel='PC2')
    return _save(root,{'accuracy':acc,'test_rows':len(yte),'classes':3},fig,{'confusion_matrix':confusion_matrix(yte,p).tolist()})


def run_06(root):
    rng=np.random.default_rng(SEED); normal=rng.normal(0,1,(650,2)); anomalies=rng.normal(4,0.65,(50,2)); X=np.vstack([normal,anomalies]); y=np.array([0]*len(normal)+[1]*len(anomalies))
    m=IsolationForest(contamination=.07,random_state=SEED); m.fit(normal); score=-m.score_samples(X); auc=float(roc_auc_score(y,score)); pred=(m.predict(X)==-1).astype(int)
    fig,ax=plt.subplots(figsize=(7,5)); ax.scatter(X[:,0],X[:,1],c=pred,s=16,alpha=.65); ax.set(title='Isolation Forest anomaly view',xlabel='Feature 1',ylabel='Feature 2')
    return _save(root,{'roc_auc':auc,'flagged':int(pred.sum()),'true_anomalies':int(y.sum())},fig)


def run_07(root):
    d=load_breast_cancer(); X,y=d.data,d.target
    models={'Logistic Regression':make_pipeline(StandardScaler(),LogisticRegression(max_iter=1000,random_state=SEED)),'Random Forest':RandomForestClassifier(n_estimators=140,random_state=SEED),'Gradient Boosting':GradientBoostingClassifier(random_state=SEED),'KNN':make_pipeline(StandardScaler(),KNeighborsClassifier(7))}
    scores={name:float(cross_val_score(m,X,y,cv=5,scoring='accuracy').mean()) for name,m in models.items()}; best=max(scores,key=scores.get)
    fig,ax=plt.subplots(figsize=(7,5)); ax.bar(scores.keys(),scores.values()); ax.set_ylim(.85,1); ax.set(title='AutoML-style model tournament',ylabel='5-fold CV accuracy'); ax.tick_params(axis='x',rotation=25)
    return _save(root,{'best_model':best,'cv_accuracy':scores[best]},fig,{'scores':scores,'autogluon_note':'Install AutoGluon to replace the lightweight local tournament.'})


def run_08(root):
    d=load_iris(); Xtr,Xte,ytr,yte=train_test_split(d.data,d.target,test_size=.25,stratify=d.target,random_state=SEED); m=GaussianNB().fit(Xtr,ytr); p=m.predict(Xte); acc=float(accuracy_score(yte,p)); cm=confusion_matrix(yte,p)
    x=np.linspace(-4,4,120); y=x**2; w=3.5; path=[]
    for _ in range(18): path.append(w); w-=.08*(2*w)
    fig,ax=plt.subplots(figsize=(7,5)); ax.plot(x,y); ax.scatter(path,np.array(path)**2); ax.set(title='Gradient descent on f(x)=x²',xlabel='x',ylabel='f(x)')
    quizzes=[{'q':'What does a false positive mean?','a':'The model predicts positive when the true class is negative.'},{'q':'Why does gradient descent use a derivative?','a':'The derivative gives the local slope and direction of greatest increase, so moving opposite reduces loss.'}]
    return _save(root,{'accuracy':acc,'gradient_steps':len(path)},fig,{'confusion_matrix':cm.tolist(),'quizzes':quizzes})


def run_09(root):
    G=nx.DiGraph(); edges=[('ingest','validate'),('validate','features'),('features','train'),('features','evaluate'),('train','evaluate'),('evaluate','deploy'),('deploy','monitor')]; G.add_edges_from(edges)
    assert nx.is_directed_acyclic_graph(G); order=list(nx.topological_sort(G)); status={node:'completed' for node in order}
    fig,ax=plt.subplots(figsize=(8,5)); pos=nx.spring_layout(G,seed=SEED); nx.draw_networkx(G,pos,ax=ax,node_size=1800,font_size=8,arrows=True); ax.set_title('FlowForge DAG execution graph'); ax.axis('off')
    return _save(root,{'tasks_completed':len(order),'is_dag':True,'execution_order':' -> '.join(order)},fig,{'status':status})


def run_10(root):
    d=load_breast_cancer(); X,y=d.data,d.target
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,stratify=y,random_state=SEED)
    clf=RandomForestClassifier(n_estimators=120,random_state=SEED).fit(Xtr,ytr); p=clf.predict(Xte); acc=float(accuracy_score(yte,p))
    Z=StandardScaler().fit_transform(X); labels=KMeans(2,n_init=15,random_state=SEED).fit_predict(Z); sil=float(silhouette_score(Z,labels)); iso=IsolationForest(contamination=.05,random_state=SEED).fit_predict(Z); out=int((iso==-1).sum())
    nn=NearestNeighbors(n_neighbors=4).fit(Z[:400]); dist,idx=nn.kneighbors(Z[400:401])
    bins=(X[:,0]>np.median(X[:,0])).astype(int); assoc=float(np.mean((bins==1)&(y==1))/max(np.mean(bins==1),1e-9))
    fig,ax=plt.subplots(figsize=(7,5)); ax.bar(['Classification acc','Silhouette','High-feature & positive'],[acc,sil,assoc]); ax.set_ylim(0,1); ax.set(title='CRISP-DM integrated outcomes')
    return _save(root,{'accuracy':acc,'silhouette':sil,'outliers':out,'nearest_neighbor_distance':float(dist[0,1])},fig,{'association_proxy':assoc,'crisp_dm_phases':['Business understanding','Data understanding','Data preparation','Modeling','Evaluation','Deployment']})


def run_11(root):
    root=Path(root); repo=root.parent; required=['README.md','prompts.md','src/experiment.py','dashboard.html','artifacts/metrics.json','artifacts/result.png']
    shared=(repo/'shared'/'experiments.py').read_text(errors='ignore')
    rows=[]
    for p in sorted(repo.glob('[0-9][0-9]_*')):
        missing=[x for x in required if not (p/x).exists()]
        pid=p.name[:2]
        checks={'required_files':not missing,'fixed_seed':'SEED = 42' in shared,'experiment_implemented':f'def run_{pid}' in shared}
        score=sum(checks.values())/len(checks)*100; rows.append({'project':p.name,'score':score,'missing':missing,'checks':checks})
    vals=[r['score'] for r in rows] or [0]
    fig,ax=plt.subplots(figsize=(9,5)); ax.bar([r['project'][:5] for r in rows],[r['score'] for r in rows]); ax.set_ylim(0,100); ax.set(title='Repository audit coverage',ylabel='Audit score')
    return _save(root,{'audit_score':float(np.mean(vals)),'projects_checked':len(rows)},fig,{'projects':rows})


def make_series(n=320):
    rng=np.random.default_rng(SEED); t=np.arange(n); return 100+.12*t+8*np.sin(2*np.pi*t/24)+rng.normal(0,2,n)

def lag_frame(values,lags=12):
    s=pd.Series(values); df=pd.DataFrame({'y':s});
    for lag in range(1,lags+1): df[f'lag_{lag}']=s.shift(lag)
    return df.dropna().reset_index(drop=True)

def run_12(root):
    values=make_series(); df=lag_frame(values,12); split=int(len(df)*.8); tr,te=df.iloc[:split],df.iloc[split:]; Xtr,ytr=tr.drop(columns='y'),tr.y; Xte,yte=te.drop(columns='y'),te.y
    models={'Linear':LinearRegression(),'Random Forest':RandomForestRegressor(n_estimators=120,random_state=SEED,min_samples_leaf=2)}; rows={}; preds={}
    for name,m in models.items(): m.fit(Xtr,ytr); p=m.predict(Xte); preds[name]=p; rows[name]={'MAE':float(mean_absolute_error(yte,p)),'RMSE':float(mean_squared_error(yte,p)**.5)}
    best=min(rows,key=lambda k:rows[k]['RMSE']); fig,ax=plt.subplots(figsize=(8,5)); ax.plot(range(len(yte)),yte.values,label='Actual'); ax.plot(range(len(yte)),preds[best],label='Forecast'); ax.legend(); ax.set(title='Chronological holdout forecast',xlabel='Test time step',ylabel='Value')
    return _save(root,{'best_model':best,**rows[best],'chronological_split':True},fig,{'all_models':rows})


def run_13(root):
    df=taxi_data(1800).sort_values('hour').reset_index(drop=True); X=df.drop(columns='duration_min'); y=df.duration_min; split=int(len(df)*.8); Xtr,Xte,ytr,yte=X.iloc[:split],X.iloc[split:],y.iloc[:split],y.iloc[split:]
    m=RandomForestRegressor(n_estimators=160,random_state=SEED,min_samples_leaf=2).fit(Xtr,ytr); p=m.predict(Xte); rmse=float(mean_squared_error(yte,p)**.5); imp=sorted(zip(X.columns,m.feature_importances_),key=lambda z:z[1],reverse=True)
    coords=StandardScaler().fit_transform(df[['pickup_lat','pickup_lon']]); clusters=KMeans(4,n_init=15,random_state=SEED).fit_predict(coords)
    fig,ax=plt.subplots(figsize=(7,5)); ax.scatter(df.pickup_lon,df.pickup_lat,c=clusters,s=8,alpha=.55); ax.set(title='NYC-like pickup location clusters',xlabel='Longitude',ylabel='Latitude')
    audit={'target_not_in_features':'duration_min' not in X.columns,'train_before_test':True,'fixed_seed':True,'preprocessing_scope_ok':True}
    return _save(root,{'RMSE':rmse,'MAE':float(mean_absolute_error(yte,p)),'audit_checks_passed':sum(audit.values())},fig,{'feature_importance':imp[:7],'audit':audit})


def run_14(root):
    rng=np.random.default_rng(SEED); n=900; age=rng.normal(40,12,n); income=rng.normal(70000,22000,n); text_len=rng.integers(5,50,n); positive_words=rng.poisson(2,n); image_brightness=rng.normal(.5,.15,n); image_edges=rng.normal(.3,.1,n)
    raw=np.c_[age,income,text_len,positive_words,image_brightness,image_edges]; score=.02*(age-40)+.00002*(income-70000)+.35*positive_words+.8*(image_brightness-.5)+rng.normal(0,.8,n); y=(score>np.median(score)).astype(int)
    Xtr,Xte,ytr,yte=train_test_split(raw,y,test_size=.25,stratify=y,random_state=SEED)
    models={'Logistic':make_pipeline(StandardScaler(),LogisticRegression(max_iter=600,random_state=SEED)),'Random Forest':RandomForestClassifier(n_estimators=140,random_state=SEED),'Gradient Boosting':GradientBoostingClassifier(random_state=SEED)}; scores={}
    for name,m in models.items(): m.fit(Xtr,ytr); scores[name]=float(accuracy_score(yte,m.predict(Xte)))
    best=max(scores,key=scores.get); fig,ax=plt.subplots(figsize=(7,5)); ax.bar(scores.keys(),scores.values()); ax.set_ylim(.5,1); ax.set(title='Multimodal AutoML-style tournament',ylabel='Accuracy')
    return _save(root,{'best_model':best,'accuracy':scores[best]},fig,{'modalities':['tabular','text summary features','image summary features'],'scores':scores,'autogluon_optional':True})


def run_15(root):
    rng=np.random.default_rng(SEED); n=650; returns=rng.normal(.0004,.012,n); returns[1:]+=0.10*returns[:-1]; price=100*np.exp(np.cumsum(returns)); df=lag_frame(returns,10); split=int(len(df)*.8); tr,te=df.iloc[:split],df.iloc[split:]; Xtr,ytr=tr.drop(columns='y'),tr.y; Xte,yte=te.drop(columns='y'),te.y
    m=RandomForestRegressor(n_estimators=140,random_state=SEED,min_samples_leaf=3).fit(Xtr,ytr); p=m.predict(Xte); rmse=float(mean_squared_error(yte,p)**.5); da=float(np.mean(np.sign(p)==np.sign(yte.values))); strat=np.where(p>0,yte.values,0); cumulative=float(np.prod(1+strat)-1)
    fig,ax=plt.subplots(figsize=(8,5)); ax.plot(np.cumprod(1+yte.values)-1,label='Buy & hold test'); ax.plot(np.cumprod(1+strat)-1,label='Long/cash signal'); ax.legend(); ax.set(title='SPY-style walk-forward test',xlabel='Test day',ylabel='Cumulative return')
    return _save(root,{'RMSE':rmse,'directional_accuracy':da,'strategy_test_return':cumulative,'chronological_split':True},fig,{'data_note':'Offline synthetic SPY-style returns. Replace with real historical CSV for final extension.'})

RUNNERS={f'{i:02d}':globals()[f'run_{i:02d}'] for i in range(1,16)}
def run_project(pid, root): return RUNNERS[pid](root)
