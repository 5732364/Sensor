/* empty css             *//* empty css                                                              */import{i as f}from"./request-C08gkA4w.js";import{_ as x,r as c,h as k,u as l,c as r,a as t,F as V,i as w,b as d,j as C,w as S,d as T,k as b,l as A,o as i,t as u,e as B,f as D}from"./index-Re_RWizQ.js";const N={key:0},z={class:"appList"},E=["onClick"],L=["src"],j={class:"wenzi"},q={class:"text"},F={class:"risk_number"},I={class:"search"},R={__name:"index",setup(H){const p=D(),_=()=>{s.value&&p.push({path:"/appDetail",query:{searchText:s.value,type:"name",page:"1"}})},h=o=>{p.push({path:"/appDetail",query:{searchText:o.id,type:"id",page:"1"}})};var n=c([]),s=c(null);const m=()=>{f({method:"get",url:"/api/homepage_rand"}).then(async o=>{console.log(o,"##########"),n.value=o.data})};return k(async()=>{console.log("!!!!!!!!!!"),await m()}),(o,a)=>{const g=b,v=A;return l(n).length?(i(),r("div",N,[a[2]||(a[2]=t("h1",null,"Sensor Detection Tool",-1)),t("div",z,[(i(!0),r(V,null,w(l(n),(e,y)=>(i(),r("div",{class:"one",key:y,onClick:M=>h(e)},[t("img",{src:"http://47.90.217.63:8000/logo/"+e.id+".jpg"},null,8,L),t("div",j,[t("div",q,u(e.new_names),1),t("div",F,u(e.risk_score),1)])],8,E))),128))]),t("div",I,[d(g,{modelValue:l(s),"onUpdate:modelValue":a[0]||(a[0]=e=>C(s)?s.value=e:s=e),size:"large",placeholder:"Please input",style:{width:"850px"}},null,8,["modelValue"]),d(v,{style:{"margin-left":"5px"},type:"primary",size:"large",onClick:_},{default:S(()=>a[1]||(a[1]=[B("Search")])),_:1})])])):T("",!0)}}},K=x(R,[["__scopeId","data-v-d8b064dc"]]);export{K as default};