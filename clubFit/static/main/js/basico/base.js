
var dataConfirm;
var functionConfirm;
function openConfirm(data, functionGo){
	dataConfirm = data;
	functionConfirm = functionGo;
	$("#mi-modal").modal('show');
}
function actionConfirm(confirm){
	if(confirm){
		eval(functionConfirm+"("+dataConfirm+")");
	}
	$("#mi-modal").modal('hide');
}

//funcion para acortar el llamado de un elemento
function gId(id)
{
	return document.getElementById(id);
}
function pintarOpcion()
{

	
	var vista = gId("vistaActual").value;
	
	if(vista =="codigosAdministrador" || vista =="reporteGraficoAdmin")
	{
		vista="indexAdministrador";
	}
	else if(vista =="codigosVendedor" || vista =="reporteGraficoVende")
	{
		vista="indexVendedor";
	}
	gId("O_"+vista).style.backgroundColor="#f2f2f2";
	gId("F_"+vista).style.display="block";
	gId("O_"+vista).scrollIntoView();
}

//funcion para hacer un ajax basico
function ajaxBasic(data, url, action)
{
	
	
	if(window.XMLHttpRequest)
	{
		conexion = new XMLHttpRequest();
	}
	else if(window.ActiveXObject)
	{
		conexion = new ActiveXObject("Microsoft.XMLHTTP");
	}
	
		
	if(conexion) 
	{
		conexion.onreadystatechange = function()
		{
			if(conexion.readyState == 4)
			{
				if(conexion.status == 200)
				{	
					
					
					if(typeof action != "undefined")
					{
						//action(conexion.responseText);
						var respuesta = JSON.parse(conexion.responseText);
						
						window[action](respuesta,"respuesta");
					}
				}
				else
				{
					console.log("Error");
					
				}
					
			}
		};
		
		conexion.open("POST", url);
		conexion.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
		conexion.setRequestHeader('X-CSRFToken', csrfcookie());
		var datos = JSON.stringify(data);
		conexion.send(datos);
		
		
	}
	
}

//funcion que extrae el token de django
var csrfcookie = function()
{
	//funcion que opcione el token de django
	
	var cookieValue = null,
		name = 'csrftoken';
	if (document.cookie && document.cookie !== '')
	{
		var cookies = document.cookie.split(';');
		console.log(cookies);
		for (var i = 0; i < cookies.length; i++)
		{
			
			var cookie = cookies[i].trim();
			
			if (cookie.substring(0, name.length + 1) == (name + '='))
			{
				
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				console.log(cookieValue);
				break;
			}
		}
	}
	
	return cookieValue;
};


document.addEventListener('click', function() {
	
	document.activeElement.focus();
});


function changeToUpperCase(t) {
   var eleVal = document.getElementById(t.id);
   eleVal.value= eleVal.value.toUpperCase();
}


