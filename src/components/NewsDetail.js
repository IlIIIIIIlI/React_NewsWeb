import axios from "axios"
import { useEffect, useState } from 'react'
// allows us access to the component of url
import { useParams } from "react-router-dom"


export default function NewsDetail() {

    // create state for store data
    const [data, setData] = useState([])

    const paramsInUrl = useParams()

    function GetDetail() {
        const url = `http://3.25.113.121:8000/api/news/${paramsInUrl.id}`

        axios.get(url).then((res) => {
            console.log(res)
            setData(res.data)
        }).catch((err) => {
            console.log(err)
        })
    }
    // call the function after the component has been loaded
    useEffect(() => {
        GetDetail()
    }, [])


    return (
        <>
            <article class="singlepage" id="featured">
                <h1>{data.newsdetail && data.newsdetail.title}</h1>
                <img class="headerpic" src={data.newsdetail && data.newsdetail.news_image} alt="" id="featuredico" />

                <p>{data.newsdetail && data.newsdetail.announcement_text}</p>


                {(data.newsdetail && data.newsdetail.content) && data.newsdetail.content.map((itemInContent) => {
                    return (
                        <>
                            <h4>{itemInContent.journal && itemInContent.journal}</h4>
                            <h3 style={{ color: "red" }}>{itemInContent.quote && itemInContent.quote}</h3>
                            {/* <img src={itemInContent.medias && itemInContent.medias} />
                                {itemInContent.iframelinktwitter && <iframe src={itemInContent.iframelinktwitter && itemInContent.iframelinktwitter}></iframe>} */}

                        </>

                    )
                })}




            </article>
        </>
    )
}
