import classes from "./Footer.module.css"

const Footer = () => {
    return (
        <footer className={classes.footer}>
           <img src={"itmo-logo.png"} alt={"itmo-logo"}/>
           <img src={"sber-logo.png"} alt={"sber-logo"}/>
           <img src={"itmo-logo.png"} alt={"itmo-logo"}/>
           <img src={"itmo-logo.png"} alt={"itmo-logo"}/>
        </footer>
    );
};

export default Footer;