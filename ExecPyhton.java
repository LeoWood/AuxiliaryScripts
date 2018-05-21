import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class ExecPyhton{
	public static void main(String[] args){
		Process p;
		//利用CMD命令调用python，包含两个参数
		String cmd="python ExecByJava.py \"Hello\" \"World\"";
		try{
			p = Runtime.getRuntime().exec(cmd);
			InputStream fis=p.getInputStream();
			InputStreamReader isr=new InputStreamReader(fis);
			BufferedReader br=new BufferedReader(isr);
			String line=null;
            while((line=br.readLine())!=null){
            	System.out.println(line);
            } 
		}
		catch (IOException e){
			e.printStackTrace();
		}
	}
}