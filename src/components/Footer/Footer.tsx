import classes from "./Footer.module.css"

const Footer = () => {
    return (
        <footer className={classes.footer}>
            <img src={"russia-logo.png"} alt={"russia-logo"}/>
            <img src={"sber-logo.png"} alt={"sber-logo"}/>
            <img src={"itmo-logo.png"} alt={"itmo-logo"}/>
            <img src={"ya-profi.png"} alt={"yaprofi-logo"}/>
        </footer>
    );
};

export default Footer;