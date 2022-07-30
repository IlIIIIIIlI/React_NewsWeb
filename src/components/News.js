import axios from "axios"
import { useEffect, useState } from "react"
// we provide a link which could jump to the content
import { Link } from "react-router-dom"

// remember to export the component, or it cannot be called.
export default function News() {

    // create state for store data from api
    const [data, setData] = useState([])

    // must have this for inspection
    useEffect(() => {
        getNews()
    }, [])

    // get news from our django rest framework
    // attention!! you need to write CORS allowed in the settings of django
    function getNews() {
        const url = "http://3.25.113.121:8000/api/news"
        axios.get(url).then((res) => {
            console.log(res)
            setData(res.data)
        }).catch((err) => {
            console.log(err)
        })
    }
    return (
        <>
            {/* map the data subsection, as many as the number of our scraping data */}
            {data.map((item) => (
                <article >

                    <img src={item.newsdetail && item.newsdetail.news_image} alt="" id="featuredico" />
                    <h1>{item.newsdetail && item.newsdetail.title}</h1>
                    <p>{item.newsdetail && item.newsdetail.announce_text}</p>
                    {/* <a>Read Me</a> */}
                    {/* we give a ref for link to redirecting to another page, url with the id */}
                    <Link to={`${item.id}`}> Press to know more</Link>
                </article>

            ))}

        </>

    )
}
