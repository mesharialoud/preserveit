/* Preserve It — procedural 3D pouch (three.js r128). Built in code, no external model file. */
(function(){
  var stage=document.getElementById("stage"); if(!stage) return;
  var fb=stage.querySelector(".fallback");
  function ok(){try{var c=document.createElement("canvas");return !!(window.WebGLRenderingContext&&(c.getContext("webgl")||c.getContext("experimental-webgl")))}catch(e){return false}}
  if(!window.THREE||!ok()) return;
  var T=window.THREE;

  function rr(ctx,x,y,w,h,r){ctx.beginPath();ctx.moveTo(x+r,y);ctx.arcTo(x+w,y,x+w,y+h,r);ctx.arcTo(x+w,y+h,x,y+h,r);ctx.arcTo(x,y+h,x,y,r);ctx.arcTo(x,y,x+w,y,r);ctx.closePath()}
  function drop(ctx,cx,cy,s,col){ctx.save();ctx.translate(cx,cy);ctx.scale(s,s);ctx.beginPath();ctx.moveTo(0,-50);
    ctx.bezierCurveTo(22,-20,38,0,38,22);ctx.arc(0,22,38,0,Math.PI,false);ctx.bezierCurveTo(-38,0,-22,-20,0,-50);ctx.closePath();
    ctx.fillStyle=col;ctx.fill();ctx.beginPath();ctx.arc(-12,20,9,0,Math.PI*2);ctx.fillStyle="rgba(255,255,255,.55)";ctx.fill();ctx.restore()}

  var CREAM="#F7F8FA", TERRA="#366688", INK="#1B3347", MINT="#89D0B1", PINK="#F4BBD1", SKY="#5AA6E5";
  function front(){
    var c=document.createElement("canvas");c.width=1024;c.height=1440;var x=c.getContext("2d");
    var g=x.createLinearGradient(0,0,1024,1440);g.addColorStop(0,"#FFFFFF");g.addColorStop(1,"#EEEEEE");x.fillStyle=g;x.fillRect(0,0,1024,1440);
    // top seal texture
    x.fillStyle="rgba(0,0,0,.035)";for(var i=0;i<1024;i+=10){x.fillRect(i,0,5,110)}
    x.strokeStyle="rgba(31,39,51,.18)";x.lineWidth=4;x.setLineDash([14,10]);x.beginPath();x.moveTo(40,170);x.lineTo(984,170);x.stroke();x.setLineDash([]);
    drop(x,512,360,1.5,SKY);
    x.fillStyle=INK;x.textAlign="center";
    x.font="600 112px Fraunces, Georgia, serif";x.fillText("Preserve It",512,560);
    x.font="700 76px 'IBM Plex Sans Arabic', sans-serif";x.fillText("بريزيرف إت",512,664);
    x.fillStyle="rgba(31,39,51,.25)";x.fillRect(392,712,240,3);
    x.fillStyle="#4A5463";x.font="500 44px 'Plus Jakarta Sans', sans-serif";x.fillText("Freeze-dried breast milk",512,790);
    x.font="500 44px 'IBM Plex Sans Arabic', sans-serif";x.fillText("حليب أم مجفّد بالتجميد",512,856);
    // band
    x.fillStyle=MINT;x.beginPath();x.moveTo(0,930);x.lineTo(470,900);x.lineTo(470,975);x.lineTo(0,1000);x.fill();x.fillStyle=PINK;x.beginPath();x.moveTo(500,898);x.lineTo(1024,866);x.lineTo(1024,945);x.lineTo(500,973);x.fill();x.fillStyle=TERRA;x.beginPath();x.moveTo(0,1030);x.lineTo(1024,980);x.lineTo(1024,1440);x.lineTo(0,1440);x.fill();
    x.fillStyle="#FFF";x.font="700 50px 'Plus Jakarta Sans', sans-serif";x.fillText("ONE MOTHER · ONE BATCH",512,1120);
    x.font="700 52px 'IBM Plex Sans Arabic', sans-serif";x.fillText("أم واحدة · دفعة واحدة",512,1200);
    x.font="500 38px 'Plus Jakarta Sans', sans-serif";x.globalAlpha=.85;x.fillText("100 g  ·  Made in Kuwait",512,1300);x.globalAlpha=1;
    return c;
  }
  function back(){
    var c=document.createElement("canvas");c.width=1024;c.height=1440;var x=c.getContext("2d");
    x.fillStyle=CREAM;x.fillRect(0,0,1024,1440);
    x.fillStyle="rgba(0,0,0,.035)";for(var i=0;i<1024;i+=10){x.fillRect(i,0,5,110)}
    x.fillStyle=INK;x.textAlign="left";x.font="700 48px 'Plus Jakarta Sans', sans-serif";x.fillText("Batch record",90,260);
    var rows=[["Mother ID","PI-M-0187"],["Batch","PI-2611-042"],["Processed","03 / 11 / 2026"],["Volume in","1,420 ml"],["Moisture","verified < 3%"]];
    x.font="500 38px 'Plus Jakarta Sans', sans-serif";
    rows.forEach(function(r,k){var y=350+k*82;x.fillStyle="#7A8391";x.fillText(r[0],90,y);x.fillStyle=INK;x.textAlign="right";x.fillText(r[1],934,y);x.textAlign="left";
      x.fillStyle="rgba(31,39,51,.12)";x.fillRect(90,y+26,844,2)});
    // QR-like block
    x.fillStyle=INK;var s=18,ox=90,oy=830;for(var a=0;a<14;a++)for(var b=0;b<14;b++){if(((a*7+b*13+a*b)%5)<2||(a<3&&b<3)||(a>10&&b<3)||(a<3&&b>10))x.fillRect(ox+a*s,oy+b*s,s-2,s-2)}
    x.font="500 34px 'Plus Jakarta Sans', sans-serif";x.fillStyle="#4A5463";x.fillText("Scan to trace this pouch",380,900);
    x.font="500 34px 'IBM Plex Sans Arabic', sans-serif";x.fillText("امسحي الرمز لتتبّع هذا الكيس",380,950);
    x.fillStyle=SKY;x.fillRect(0,1240,1024,200);x.fillStyle=TERRA;x.fillRect(0,1300,1024,140);
    return c;
  }
  function sachet(band){
    var c=document.createElement("canvas");c.width=256;c.height=1024;var x=c.getContext("2d");
    x.fillStyle=CREAM;x.fillRect(0,0,256,1024);x.fillStyle=band;x.fillRect(0,700,256,324);
    drop(x,128,170,.75,SKY);x.save();x.translate(128,470);x.rotate(-Math.PI/2);x.fillStyle=INK;x.textAlign="center";
    x.font="600 64px Fraunces, Georgia, serif";x.fillText("Preserve It",0,22);x.restore();
    x.fillStyle=band===TERRA?"#FFF":INK;x.textAlign="center";x.font="700 40px 'Plus Jakarta Sans', sans-serif";x.fillText("4 oz",128,880);
    return c;
  }
  function tex(c){var t=new T.CanvasTexture(c);t.encoding=T.sRGBEncoding;t.anisotropy=8;return t}

  function pouchGeo(W,H,D){
    var g=new T.BoxGeometry(W,H,D,44,60,6),p=g.attributes.position;
    for(var i=0;i<p.count;i++){
      var x=p.getX(i),y=p.getY(i),z=p.getZ(i),nx=Math.abs(x/(W/2)),ny=y/(H/2);
      var fx=Math.sqrt(Math.max(0,1-Math.pow(nx,6)));
      var fy= ny>0.72 ? Math.max(0,1-Math.pow((ny-0.72)/0.28,2)) : (ny<-0.82 ? 0.82+0.18*(1-Math.pow((-ny-0.82)/0.18,2)) : 1);
      var f=0.06+0.94*fx*fy;
      p.setZ(i,z*f);
      if(ny<-0.6){p.setX(i,x*(1+0.04*(-ny-0.6)))}
    }
    g.computeVertexNormals();return g;
  }

  var renderer=new T.WebGLRenderer({antialias:true,alpha:true});
  renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,2));
  renderer.outputEncoding=T.sRGBEncoding;
  stage.insertBefore(renderer.domElement,stage.firstChild);
  var scene=new T.Scene(),cam=new T.PerspectiveCamera(32,1,.1,50);cam.position.set(0,.15,6.4);
  scene.add(new T.HemisphereLight(0xffffff,0xcfd8e0,.85));
  var key=new T.DirectionalLight(0xffffff,.85);key.position.set(-3,4,5);scene.add(key);
  var rim=new T.DirectionalLight(0xdcecff,.55);rim.position.set(4,1,-4);scene.add(rim);

  var group=new T.Group();group.position.x=-.38;scene.add(group);
  var side=new T.MeshStandardMaterial({color:0xEEEEEE,roughness:.6});
  var mats=[side,side,side,side,null,null];
  function build(){
    mats[4]=new T.MeshStandardMaterial({map:tex(front()),roughness:.55,metalness:.04});
    mats[5]=new T.MeshStandardMaterial({map:tex(back()),roughness:.55,metalness:.04});
    var pouch=new T.Mesh(pouchGeo(1.6,2.25,.62),mats);group.add(pouch);
    var bands=[PINK,MINT];
    for(var k=0;k<2;k++){var sm=new T.MeshStandardMaterial({map:tex(sachet(bands[k])),roughness:.5});var sMats=[side,side,side,side,sm,sm];var s=new T.Mesh(pouchGeo(.36,1.55,.09),sMats);s.position.set(1.15+k*.42,-.36,-.35-k*.25);s.rotation.y=-.35;group.add(s)}
    if(fb)fb.style.display="none";
  }
  var fontsReady=(document.fonts&&document.fonts.load)?Promise.all([
    document.fonts.load("600 40px Fraunces"),document.fonts.load("700 40px 'IBM Plex Sans Arabic'"),document.fonts.load("500 40px 'Plus Jakarta Sans'")]).catch(function(){}):Promise.resolve();
  var timeout=new Promise(function(r){setTimeout(r,1800)});
  Promise.race([fontsReady,timeout]).then(build);

  function size(){var w=stage.clientWidth,h=stage.clientHeight;renderer.setSize(w,h,false);cam.aspect=w/h;cam.updateProjectionMatrix()}
  size();window.addEventListener("resize",size);

  var dragging=false,lx=0,vel=0,rotY=-.45,idle=0,reduce=window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var el=renderer.domElement;el.style.touchAction="pan-y";el.style.cursor="grab";
  el.addEventListener("pointerdown",function(e){dragging=true;lx=e.clientX;el.setPointerCapture(e.pointerId);el.style.cursor="grabbing"});
  el.addEventListener("pointermove",function(e){if(!dragging)return;var dx=e.clientX-lx;lx=e.clientX;vel=dx*.01;rotY+=vel;idle=0});
  function up(){dragging=false;el.style.cursor="grab"}
  el.addEventListener("pointerup",up);el.addEventListener("pointercancel",up);

  var visible=true;
  if("IntersectionObserver" in window){new IntersectionObserver(function(es){visible=es[0].isIntersecting}).observe(stage)}
  var t0=performance.now();
  (function loop(now){
    requestAnimationFrame(loop);if(!visible)return;
    var t=(now-t0)/1000;
    if(!dragging){vel*=.94;rotY+=vel;idle+=1/60;if(!reduce&&idle>1.2)rotY+=.0045}
    group.rotation.y=rotY;group.position.x=-.38;group.position.y=reduce?0:Math.sin(t*1.1)*.05;group.rotation.x=reduce?0:Math.sin(t*.7)*.03;
    renderer.render(scene,cam);
  })(t0);
})();
