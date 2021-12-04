let search_status=document.querySelector("#search-status")
let  table_body=document.querySelector("#table-body")

async function handleClick(e){
    if(institute.value==="0" || batch.value==="0"){
        alert("Choose any batch or institute first")
    }
    else{
        try{
        let res=await fetch(`/test/check/user/status/paper/?i_id=${institute.value}&b_id=${batch.value}`)
        res=await res.json()
            console.log(res)
        if(res.status){
            if(res["user_status"]){
                s=""
                res['paper'].forEach((data)=>{
                    console.log(new Date(data.start))
                    s+=`<tr>
<td>${data.id}</td>
<td>${data.name}</td>
<td>${data.marks}</td>
<td>${data.number}</td>
<td>${data.start}</td>
<td>${data.end}</td>
<td>
${new Date(data.start)<=new Date() && new Date()<=new Date(data.end) && !data.status?`<a href="/test/start/test?id=${data.id}">Start Test</a>`:new Date(data.start)>new Date() && !data.status?"Test Not Start Yet":data.status?`<a href="/test/result/user/?id=${data.id}">Result</a>`:"<a style='color: red;text-decoration: none'>Test Missed</a>"}
</td>
</tr>`
                })
                table_body.innerHTML=s;

            }
            else{
                table_body.innerHTML=`<tr>
            You Are Not Verify By Institute In This Batch Yet
            </tr>`
            }
        }
    else{
        alert("Server Error....")
        }}
        catch (e){
            alert(`Server Error....${e}`)
        }
    }
}








search_status.addEventListener("click",handleClick)
