function favorite(book_id,checked){
        axios.post('/favorite/update',{
            book_id: book_id,
            checked: checked
        }).then((res) => {
            if (res.data.status === 200) {
                window.location.reload()
            }else{
                window.location.href = '/login'        
            }
        })
}


