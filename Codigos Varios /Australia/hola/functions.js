


  var firebaseConfig = {
    apiKey: "AIzaSyD0guV4npelBDdP5M0CH9r2RUM5CISvfoI",
    authDomain: "australia-df87c.firebaseapp.com",
    databaseURL: "https://australia-df87c.firebaseio.com",
    projectId: "australia-df87c",
    storageBucket: "australia-df87c.appspot.com",
    messagingSenderId: "471915571225",
    appId: "1:471915571225:web:49ee362f1cf57dea7fe288",
    measurementId: "G-K6YLCGDC90"
  };
  // Initialize Firebase
  var fire = firebase.initializeApp(firebaseConfig);





  const addBtn = document.getElementById('addBtn');
  const updateBtn = document.getElementById('updateBtn');
  const removeBtn = document.getElementById('removeBtn');


  var db = firebase.firestore();
var storage = firebase.storage();


var unploader = document.getElementById('unploader');
var fileButton = document.getElementById('fileButton');


fileButton.addEventListener('change',function(e){

var file = e.target.files[0];
console.log(file);
var storageRef = firebase.storage().ref('photos/'+ file.name);

var task = storageRef.put(file);


task.on('state_changed',
function progress(snapshot)

{ var percentage =(snapshot.bytesTransferred / snapshot.totalBytes) *100;
uploader.value = percentage ;
},function error(err) {},
function complete(){} );





}


);






  addBtn.addEventListener('click', e => {





    e.preventDefault();

    var fecha = new Date();
    var date = fecha.getDate()+"\n/ "+(fecha.getMonth()+1)+"\n/ "+fecha.getFullYear();

    var time =fecha.getHours()+"\n: "+fecha.getMinutes()+"\n: "+fecha.getSeconds();






    // Add a new document in collection "cities"

    db.collection("Todo").doc(document.querySelector('input[name="SiteAddres"]').value).set({


SiteAddres:document.querySelector('input[name="SiteAddres"]').value,
      CustomerName: document.querySelector('input[name="CustomerName"]').value,
      Selectanappliance: document.querySelector('input[name="Selectanappliance"]').value ,
      ProductMake_Model: document.querySelector('input[name="ProductMake/Model"]').value,
      ProductMeasusements_depth : document.querySelector('input[name="ProductMeasusements(depth)"]').value,
      ProductMeasusements_Height : document.querySelector('input[name="ProductMeasusements(Height)"]').value,
      ProductMeasusements_width : document.querySelector('input[name="ProductMeasusements(width)"]').value,
      Cut_outMeasusements_depth : document.querySelector('input[name="Cut-outMeasusements(depth)"]').value,
      Cut_outMeasusements_Height : document.querySelector('input[name="Cut-outMeasusements(Height)"]').value,
      Cut_outMeasusements_width : document.querySelector('input[name="Cut-outMeasusements(width)"]').value,
      Cut_outMeasusements_width : document.querySelector('input[name="Cut-outMeasusements(width)"]').value,
      Fault_Description :document.querySelector('input[name="FaultDescription').value,
      Cost : document.querySelector('input[name="Cost"]').value,
    //x  InspectionDate_Time :document.querySelector('input[name="InspectionDate/Time"]').value,
      LocationGPS:document.querySelector('input[name="GPS"]').value,
      Inspection_Date:  date,
      Inspection_Time:   time


  })
  .then(function() {
      console.log("Document successfully written!");
  })
  .catch(function(error) {
      console.error("Error writing document: ", error);
  });






  });
