import { makeStyles } from "@mui/styles";

const useStyle = makeStyles({
  footer: {
    variant: 'h1',
    padding: '3em',
  }
});

const Footer = () => {
  const classes = useStyle(); 
    return (
        <footer>
          <div className={classes.footer}>
            Goodreads Advanced Book Search. Made with ❤️ from G53.
          </div>
        </footer>
    );
  }

  export default Footer;