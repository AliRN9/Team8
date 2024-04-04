import Request from "./components/Request/Request.tsx";
import classes from "./App.module.css"
import Footer from "./components/Footer/Footer.tsx";

const App = () => {
    return (
        <div className={classes.app}>
            <Request />
            <Footer />
        </div>
    );
};

export default App;