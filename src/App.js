import News from "./components/News";
import NewsDetail from "./components/NewsDetail"
import { Routes, Route } from 'react-router-dom'

function App() {
  return (
    <div>
      <header>
        <h1><a href="index.html">Andy yang like News!</a></h1>

      </header>


      <div id="secwrapper">

        <section>
          {/* this part will use the component under the src/components/News.js folder, not html */}
          {/* remember to import the component*/}
          <Routes>
            <Route path="/" element={<News />} />
            <Route path=":id" element={<NewsDetail />} />
          </Routes>
        </section>
      </div>
      <footer>
        <p>Copyright &copy 2022 Chenoi by Quechen Yang. All Rights Reserved.</p>
      </footer>


    </div>
  );
}

export default App;
