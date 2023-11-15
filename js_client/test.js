const LoginForm = document.getElementById("login-form")
const content =  document.getElementById("content-container")
const SearchForm = document.getElementById("search-form")
const baseEndpoint = "http://127.0.0.1:8000/api"


if (LoginForm){
  LoginForm.addEventListener('submit', handlelogin)
}

if (SearchForm){
  SearchForm.addEventListener('submit', handlesearch)
}

function handlelogin(event) {
  event.preventDefault()
  const LoginEndpoint = `${baseEndpoint}/token/`
  let LoginFormData = new FormData(LoginForm)
  let loginObjectsData = Object.fromEntries(LoginFormData)
  let bodyStr = JSON.stringify(loginObjectsData)
  const options = {
    method:"POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: bodyStr
  }
  fetch(LoginEndpoint, options) 
  .then(response=>{
    console.log(response);
    return response.json()
  })
  .then( authData => {
    handleAuthData(authData, getProductList)
  })

  .catch(err => {
    console.log('err', err);
  })
}


function handleAuthData(authData, callback) {
  localStorage.setItem('access', authData.access)
  localStorage.setItem('refresh', authData.refresh)
  if (callback){
    callback()
  }
}

function writeToContent(data) {
  if (content) {
    content.innerHTML = "<h1> Welcome Boss, Welcomeeeeeeeeee </h1>" + "<pre>" + JSON.stringify(data, null, 4) + "</pre>"
  }
}


function getFetchOptions(method, body){
  return {
    method: method === null ? "GET" : method,
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${localStorage.getItem('access')}` 
    },

    body: body ? body : null
  }
}

function isTokenNotValid(data){
  if (data.code && data.code === "token_not_valid"){
    alert("please Login Again")
    return false
  }
  return true
}


function ValidateJWTToken() {
  const Endpoint = `${baseEndpoint}/token/verify/`
  const options = {
    method:"POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({token:localStorage.getItem('access')})
  }
  fetch(Endpoint, options)
  .then(response=>response.json()) 
  .then(x=> {
    console.log(x);
  })
}

function getProductList(){
  const productEndpoint = `${baseEndpoint}/products/`
  const options = getFetchOptions()
  fetch(productEndpoint, options)
  .then(response=>response.json())
  .then(data=>{
    const validData = isTokenNotValid(data)
    if (validData){
      writeToContent(data)
    }
    else{
      writeToContent({detail:"nikal loray hhahahaha"})
    }
  }) 

}


function handlesearch(event) {
  event.preventDefault()
  let SearchFormData = new FormData(SearchForm)
  let SearchObjectsData = Object.fromEntries(SearchFormData)
  let searchParams = new URLSearchParams(SearchObjectsData)
  const SearchEndpoint = `${baseEndpoint}/search/?${searchParams}`
  const headers = {
    "Content-Type": "application/json",
  }
  const AuthToken = localStorage.getItem('access') 
  if (AuthToken){
    headers['Authorization'] = `Bearer ${AuthToken}`
  }
  const options = {
    method:"GET",
    headers: headers
  }
  fetch(SearchEndpoint, options) 
  .then(response=>{
    return response.json()
  })
  .then(data => {
    const validData = isTokenNotValid(data)
    if (validData && content){
      if (data && data.hits){
        let htmlstr = ""
        for (let result of data.hits){
          htmlstr += `<li>${result.title}</li>`
        }
        content.innerHTML = htmlstr
        
        if (data.hits.length === 0){
          content.innerHTML = "<p>No Result Found</p>"
        }
      } else {
        content.innerHTML = "<p>No Result Found</p>"
      }

    } 
  })
}



// ValidateJWTToken()