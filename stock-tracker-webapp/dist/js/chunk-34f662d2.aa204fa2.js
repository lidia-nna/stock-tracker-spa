(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-34f662d2"],{"01ef":function(t,e,o){"use strict";o("3ce8")},"0e73":function(t,e,o){"use strict";o.r(e);var n=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("v-card",{attrs:{id:t.symbol+"_trend"},on:{plotly_relayout:function(e){return t.console.log("Relayout")}}})},r=[],i=(o("d81d"),o("96cf"),o("1da1")),a=o("2909"),c=o("5530"),l=o("030a"),s=o.n(l),f=o("2f62"),u=o("db49"),h={name:"FTChart",props:{symbol:{type:String}},data:function(){return{config:u["a"]}},computed:Object(c["a"])(Object(c["a"])({},Object(f["e"])({ftse:function(t){return t.history.ftse},ftmc:function(t){return t.history.ftmc},ftlc:function(t){return t.history.ftlc},ftai:function(t){return t.history.ftai}})),Object(f["c"])({stockSeries:"DataLY",isFTEmpty:"isFTEmpty"})),methods:Object(c["a"])({plotTrendChart:function(){var t={x:this.ftse.time,y:this.normalize(this.ftse.data),mode:"lines",name:"FT100",line:{color:this.config.plt.trace.color.secondary_d1}},e={x:this.ftmc.time,y:this.normalize(this.ftmc.data),mode:"lines",name:"FT250",line:{color:this.config.plt.trace.color.secondary_l2}},o={x:this.ftlc.time,y:this.normalize(this.ftlc.data),mode:"lines",name:"FT350",line:{color:this.config.plt.trace.color.secondary_l1}},n={x:this.ftlc.time,y:this.normalize(this.ftai.data),mode:"lines",name:"FTAI",line:{color:this.config.plt.trace.color.secondary}},r={x:this.ftlc.time,y:this.normalize(this.stockSeries),mode:"lines",name:this.symbol,line:{color:this.config.plt.trace.color.primary}},i=[t,e,o,n,r],a={title:"Financial Times Stock Indices",plot_bgcolor:this.config.plt.layout.plot_bgcolor,paper_bgcolor:this.config.plt.layout.paper_bgcolor,font:{color:this.config.plt.layout.font.color},xaxis:{gridcolor:this.config.plt.layout.xaxis.gridcolor,title:"Time"},yaxis:{title:"Value [£p]",gridcolor:this.config.plt.layout.yaxis.gridcolor}},c={responsive:!0};s.a.newPlot(this.symbol+"_trend",i,a,c)},normalize:function(t){var e=Math.max.apply(Math,Object(a["a"])(t)),o=Math.min.apply(Math,Object(a["a"])(t));return t.map((function(t){return(t-o)/(e-o)}))}},Object(f["b"])(["lastYearsFTS"])),mounted:function(){var t=this;return Object(i["a"])(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:if(console.log("YearlyChart: mounted, current route:",t.$route),!t.isFTEmpty){e.next=7;break}return e.next=4,t.lastYearsFTS();case 4:t.plotTrendChart(),e.next=8;break;case 7:t.plotTrendChart();case 8:case"end":return e.stop()}}),e)})))()}},m=h,p=(o("01ef"),o("2877")),d=o("6544"),y=o.n(d),b=o("b0af"),g=Object(p["a"])(m,n,r,!1,null,"9bcbda5a",null);e["default"]=g.exports;y()(g,{VCard:b["a"]})},"3ce8":function(t,e,o){}}]);
//# sourceMappingURL=chunk-34f662d2.aa204fa2.js.map