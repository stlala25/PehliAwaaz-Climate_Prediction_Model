import styles from '../style';
import {intropoints} from '../constants';



const Hero = () => (
    <section id="home" className={`flex md:flex-row flex-col ${styles.paddingY}`}>
    <div className={`flex-1 ${styles.flexStart} flex-col xl:px-0 sm:px-16 px-6 `}>
     
      
      {/* navlink template for reference */}

      <div className={`list-none justify-end items-center grid sm:grid-cols-3  gap-1 ` }>
      {intropoints.map( (point,index) => (
        <li 
           key={point.id}
           className={`font-poppins font-normal cursor-pointer  ${index==point.length-1 ? 'mr-0' : 'mr-10'} text-white max-w-xs mx-auto  rounded-lg overflow-hidden shadow-3xl bg-slate-950 p-4 mt-10 mb-10 content-center 
           `}
        >
         <div className='flex flex-col justify-center align-middle text-center  '>
            <p className={`sm:text-[30px] text-[20px] font-bold`}>{point.title}</p>
            <p className={`sm:font-[9px] font-[5px]`}>{point.content}</p>

         </div>

          
         
        </li>
      ) )}
    </div>
    
  
      
    </div>

    {/* <div className={`flex-1 flex ${styles.flexCenter} md:my-0 my-10 relative `}>
        
         <div className="absolute z-[0] w-[40%] h-[35%] top-0 pink__gradient "></div>
         <div className="absolute z-[1] w-[80%] h-[85%] bottom-40 rounded-full white__gradient "></div>
         <div className="absolute z-[0] w-[50%] h-[50%] right-20 bottom-20  blue__gradient "></div>
    </div> */}
    </section>
)
 
    
  


export default Hero