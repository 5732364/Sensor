/* empty css             *//* empty css                     */import{_ as b,r as u,h as y,c as h,a as t,b as o,w as n,u as f,F as S,E as w,s as T,o as E,e as d,f as C,g as A,v as k}from"./index-Re_RWizQ.js";import{i as O}from"./request-C08gkA4w.js";import{i as P}from"./index-DFpWVYxE.js";const U={class:"Header"},j={class:"main"},M={class:"imgJiemian"},B={class:"img"},I={class:"information"},N={class:"biaoge"},V={__name:"index",setup(F){const r=C(),m=u(null);var p=u([]),g=u("2");const x=a=>{console.log(a),g.value=a,a==1?r.push("/Main"):a==2?r.push("/Categories"):a==3?r.push("/Application"):a==4&&r.push("/Sensors")},_=async()=>{const a=await O.get("/api/category_data");console.log(a.data),p.value=Object.entries(a.data).map(([s,c])=>({name:s,...c})),console.log(p.value);const e=Object.keys(a.data),l=Object.values(a.data).map(s=>s.expected),i=Object.values(a.data).map(s=>s.unexpected);v(e,l,i)},v=(a,e,l)=>{var i=P(m.value),s={title:{text:"Expected vs Unexpected Sensors by App Category",left:"right"},tooltip:{trigger:"axis",axisPointer:{type:"shadow"}},legend:{},grid:{left:"3%",right:"4%",bottom:"3%",containLabel:!0},xAxis:{type:"category",data:a},yAxis:{type:"value",boundaryGap:[0,.01]},series:[{name:"Expected",type:"bar",data:e,barWidth:"50px",itemStyle:{color:"#ffaf00"}},{name:"Unexpected",type:"bar",data:l,barWidth:"50px",itemStyle:{color:"#f46920"}}]};i.setOption(s)};return y(()=>{_()}),(a,e)=>{const l=A,i=w,s=k,c=T;return E(),h(S,null,[t("div",U,[e[4]||(e[4]=t("div",{class:"logo"},null,-1)),o(i,{"default-active":f(g),class:"el-menu-demo",mode:"horizontal",onSelect:x,style:{width:"80%"}},{default:n(()=>[o(l,{index:"1"},{default:n(()=>e[0]||(e[0]=[d("Home")])),_:1}),o(l,{index:"2"},{default:n(()=>e[1]||(e[1]=[d("Categories")])),_:1}),o(l,{index:"3"},{default:n(()=>e[2]||(e[2]=[d("Applications")])),_:1}),o(l,{index:"4"},{default:n(()=>e[3]||(e[3]=[d("Sensors/Permission Data")])),_:1})]),_:1},8,["default-active"])]),t("div",j,[e[7]||(e[7]=t("h1",{class:"title"},"Categories",-1)),t("div",M,[e[5]||(e[5]=t("h2",{class:"title"},"Popular categories with Sensor Usage",-1)),t("div",B,[t("div",{ref_key:"mains",ref:m,style:{width:"80%",height:"450px",position:"absolute",top:"50px","border-radius":"10px"}},null,512)])]),t("div",I,[e[6]||(e[6]=t("div",{class:"text"},[t("div",{class:"timu"},"The following table shows the following data for all Android app categories:"),t("ul",{style:{"margin-left":"40px"}},[t("li",null,"The average risk rating"),t("li",null,"The number of total Expected Sensor"),t("li",null,"The number of total Unexpected Sensor"),t("li",null,"Total Permission requested")])],-1)),t("div",N,[o(c,{data:f(p),style:{width:"100%"}},{default:n(()=>[o(s,{prop:"name",label:"Category"}),o(s,{prop:"risk_score",label:"Average rating"}),o(s,{prop:"expected",label:"Total Expected Sensor"}),o(s,{prop:"unexpected",label:"Total Unexpected Sensor"}),o(s,{prop:"permission_count",label:"Total Permission"})]),_:1},8,["data"])])])])],64)}}},D=b(V,[["__scopeId","data-v-4d32899c"]]);export{D as default};
