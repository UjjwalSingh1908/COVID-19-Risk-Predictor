export class Book {
constructor(title, author, description,pages)
  {
   this.title= title;
   this.author= author;
   this.description= description;
   this.pages= pages;
   let this.currentPage= 0;
   let this. read= false;
  }
  const readBook= (page)=>
   {
     if (page<1 || page> this.pages){
       return 0;
     }
     elseif (page>=1 && page< this.pages) {
       this.currentPage= page;
       return 1;
     }
     else{
       this.currentPage= page;
       this.read= true;
       return 1;
     }
   }
}
const book1= new readBook("Gulliver's Travel","Jonathan Swift","Gulliver, a surgeon and sea captain who visits remote regions of the world, and it describes four adventures. ",350);
const book2= new readBook("Macbeth", "William Shakespeare"," Macbeth hears that he is going to be king; he and Lady Macbeth kill people so he can become king; both of them die.",200);
const book3= new readBook("Harry Potter", "J.K. Rowling"," The novels chronicle the lives of a young wizard, Harry Potter, and his friends Hermione Granger and Ron Weasley, all of whom are students at Hogwarts School of Witchcraft and Wizardry.",500);
export const books = [book1, book2, book3];
