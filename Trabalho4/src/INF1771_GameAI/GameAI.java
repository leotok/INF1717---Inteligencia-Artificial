package INF1771_GameAI;
import INF1771_GameAI.Map.*;
import java.util.ArrayList;
import java.util.List;
import INF1771_GameAI.Estado;


public class GameAI
{
	Position player = new Position();
	String state = "ready";
	String dir = "north";
	long score = 0;
	int energy = 0;
	
	int rows = 35;
	int col = 60;
	
	Estado estadoPlayer = Estado.Procurando_ouro;
	List<Position> powerUpList = new ArrayList<Position>();
	boolean inimigoAVista = false;
	
	char[][] observacoes = new char [rows][col];

	/**
	 * Refresh player status
	 * @param x			player position x
	 * @param y			player position y
	 * @param dir		player direction
	 * @param state		player state
	 * @param score		player score
	 * @param energy	player energy
	 */
	
	public void LimpaObservacoes() {
		System.out.println("Limpou observacos");
		for(int i = 0; i < rows; i++) {
			for(int j = 0; j < col; j++){
				observacoes[i][j] = '?';
			}
		}
	}
	
	public void SetStatus(int x, int y, String dir, String state, long score, int energy)
	{
		player.x = x;
		player.y = y;
		this.dir = dir.toLowerCase();

		this.state = state;
		this.score = score;
		this.energy = energy;
	}

	/**
	 * Get list of observable adjacent positions
	 * @return List of observable adjacent positions 
	 */
	public List<Position> GetObservableAdjacentPositions()
	{
		List<Position> ret = new ArrayList<Position>();

		ret.add(new Position(player.x - 1, player.y));
		ret.add(new Position(player.x + 1, player.y));
		ret.add(new Position(player.x, player.y - 1));
		ret.add(new Position(player.x, player.y + 1));

		return ret;
	}
	
	public List<Position> GetObservableAdjacentPositionsToPosition(Position p)
	{
		List<Position> ret = new ArrayList<Position>();

		ret.add(new Position(p.x - 1, p.y));
		ret.add(new Position(p.x + 1, p.y));
		ret.add(new Position(p.x, p.y - 1));
		ret.add(new Position(p.x, p.y + 1));

		return ret;
	}

	/**
	 * Get list of all adjacent positions (including diagonal)
	 * @return List of all adjacent positions (including diagonal)
	 */
	public List<Position> GetAllAdjacentPositions()
	{
		List<Position> ret = new ArrayList<Position>();

		ret.add(new Position(player.x - 1, player.y - 1));
		ret.add(new Position(player.x, player.y - 1));
		ret.add(new Position(player.x + 1, player.y - 1));

		ret.add(new Position(player.x - 1, player.y));
		ret.add(new Position(player.x + 1, player.y));

		ret.add(new Position(player.x - 1, player.y + 1));
		ret.add(new Position(player.x, player.y + 1));
		ret.add(new Position(player.x + 1, player.y + 1));

		return ret;
	}

	/**
	 * Get next forward position
	 * @return next forward position
	 */
	public Position NextPosition()
	{
		Position ret = null;
		if(dir.equals("north"))
			ret = new Position(player.x, player.y - 1);
		else if(dir.equals("east"))
			ret = new Position(player.x + 1, player.y);
		else if(dir.equals("south"))
			ret = new Position(player.x, player.y + 1);
		else if(dir.equals("west"))
			ret = new Position(player.x - 1, player.y);

		return ret;
	}

	/**
	 * Player position
	 * @return player position
	 */
	public Position GetPlayerPosition()
	{
		return player;
	}

	/**
	 * Set player position
	 * @param x		x position
	 * @param y		y position
	 */
	public void SetPlayerPosition(int x, int y)
	{
		player.x = x;
		player.y = y;

	}

	/**
	 * Observations received
	 * @param o	 list of observations
	 */
	
	public void PreencheObservacoesEmvolta(char obs) {
		
		Position p = GetPlayerPosition();
		boolean jaObservou = false;
		Position pJaObservada = null;
		List<Position> lst = GetObservableAdjacentPositions();
		
		for(Position ap : lst) {
			if(ap.x >= 0 && ap.x <= 59 && ap.y >= 0 && ap.y <= 34) {
				if(getObservacaoPosicao(ap) == Character.toUpperCase(obs)){
					// ja foi marcada com ctz
					return;
				}
				else if(getObservacaoPosicao(ap) == obs) {
					jaObservou = true;
					pJaObservada = ap;
					break;
				}
			}
		}
		
		if(jaObservou){
			System.out.printf("Ja observou!\n");
			// marca a casa com ctz e descmarca as outras
			char novaObs = Character.toUpperCase(obs);
			this.observacoes[pJaObservada.y][pJaObservada.x] = novaObs;
			
			List<Position> adjacentesJaObs = GetObservableAdjacentPositionsToPosition(pJaObservada);
			for(Position ap: adjacentesJaObs) {
				List<Position> adjAdj = GetObservableAdjacentPositionsToPosition(ap);
				for(Position aap: adjAdj) {
					if(aap.x >= 0 && aap.x <= 59 && aap.y >= 0 && aap.y <= 34){
						if(getObservacaoPosicao(aap) == obs) {
							this.observacoes[aap.y][aap.x] = '_';
						}
					}
				}
			}
		}
		else {
			System.out.printf("Nova obs\n");
			if(dir.equals("north")) {
				if(p.y > 0) this.observacoes[p.y - 1][p.x] = obs;
				if(p.x < 59) this.observacoes[p.y][p.x + 1] = obs;
				if(p.x > 0) this.observacoes[p.y][p.x - 1] = obs;
			}
			else if(dir.equals("south")){
				if(p.y < 34) this.observacoes[p.y + 1][p.x] = obs;
				if(p.x < 59) this.observacoes[p.y][p.x + 1] = obs;
				if(p.x > 0) this.observacoes[p.y][p.x - 1] = obs;
			}
			else if(dir.equals("east")) {
				if(p.y > 0) this.observacoes[p.y - 1][p.x] = obs;
				if(p.y < 34) this.observacoes[p.y + 1][p.x] = obs;
				if(p.y < 59) this.observacoes[p.y][p.x + 1] = obs;
			}
			else if(dir.equals("west")){
				if(p.y > 0) this.observacoes[p.y - 1][p.x] = obs;
				if(p.y < 34) this.observacoes[p.y + 1][p.x] = obs;
				if(p.y > 0) this.observacoes[p.y][p.x - 1] = obs;
			}
		}
	}
	
	public void PreencheObservacoesNaPosicao(char obs) {
		
		Position p = GetPlayerPosition();
		
		this.observacoes[p.y][p.x] = obs;
	}
	
	public void PreencheObservacoesNaFrente(char obs) {
		
		Position p = GetPlayerPosition();
		
		if(dir.equals("north")) {
			if(p.y >= 0) this.observacoes[p.y - 1][p.x] = obs;
		}
		else if(dir.equals("south")) {
			if(p.y < 35) this.observacoes[p.y + 1][p.x] = obs;
		}
		else if(dir.equals("east")) {
			if(p.x < 60) this.observacoes[p.y][p.x + 1] = obs;
		}
		else if(dir.equals("west")) {
			if(p.x >= 0) this.observacoes[p.y][p.x - 1] = obs;
		}
	}
	
	public boolean containsPosition(Position p, List<Position> lst) {
		for(Position pp: lst) {
			if(pp.x == p.x && pp.y == p.y){
				return true;
			}
		}
		return false;
	}
	
	
	public void GetObservations(List<String> o)
	{

		for (String s : o)
		{
			System.out.printf("Observacoes: %s\n", s);
			if(s.equals("blocked")){
				PreencheObservacoesNaFrente('t'); //travado: t -? T-ctz
//			} else if(s.equals("steps")){
//				PreencheObservacoesEmvolta('s'); // steps: s-? S-ctz
			} else if(s.equals("breeze")){
				PreencheObservacoesEmvolta('v'); //vento: v-? V-ctz
			} else if(s.equals("flash")){
				PreencheObservacoesEmvolta('f'); //flash: f-? F-ctz
			} else if(s.equals("blueLight")){
				if(this.containsPosition(this.player, this.powerUpList) == false){
					System.out.println("novo powerup!\n");
					this.powerUpList.add(this.player);
				}
				PreencheObservacoesNaPosicao('b'); //blue: b-? B-ctz
			} else if(s.equals("redLight")){
				PreencheObservacoesNaPosicao('r'); //red: r-? R-ctz
			} else if(s.equals("greenLight")){
				PreencheObservacoesNaPosicao('g'); //green: g-? G-ctz
			} else if(s.equals("weakLight")){
				PreencheObservacoesNaPosicao('w'); //weak: w-? W-ctz
			}
			
			if(s.toLowerCase().contains("enemy")){
				this.inimigoAVista = true;
			}
			else this.inimigoAVista = false;
		}

	}

	/**
	 * No observations received
	 */
	public void GetObservationsClean()
	{
		Position p = GetPlayerPosition();
		Position np = this.NextPosition();
		
		this.observacoes[p.y][p.x] = '_'; // vazio 
		if(np.x >= 0 && np.x <= 59 && np.y >= 0 && np.y <= 34){
			if(this.observacoes[np.y][np.x] == '?') this.observacoes[np.y][np.x] = '_';
		}
		
		//talvez nao possa colocar vazio em volta por causa das paredes q nao da observacao
		
//		List<Position> lst = GetObservableAdjacentPositions();
//		
//		for(Position ap: lst) {
//			if(ap.x >= 0 && ap.x <= 59 && ap.y >= 0 && ap.y <= 34){
//				if(getObservacaoPosicao(ap) == '?'){
//					this.observacoes[ap.y][ap.x] = '_';
//				}
//			}
//		}
	}

	public char getObservacaoPosicao(Position p) {
		return this.observacoes[p.y][p.x];
	}
	/**
	 * Get Decision
	 * @return command string to new decision
	 */
	public String GetDecision()
	{
		for(int i = 0; i < rows; i++) {
			System.out.println(observacoes[i]);
		}
	
		Position p = GetPlayerPosition();
		Position np = NextPosition();
		System.out.printf("INFO:");
		System.out.printf("\nx: %d y: %d, dir: %s\n", p.x, p.y, this.dir);
		
		// maquina de estados
		
		switch(this.estadoPlayer) {
		
		case Procurando_ouro:
			
			if(observacoes[p.y][p.x] == 'b' || observacoes[p.y][p.x] == 'r' || observacoes[p.y][p.x] == 'g' || observacoes[p.y][p.x] == 'w'){
				System.out.println("pegar_item");
				return "pegar_ouro";
			}
			if(np.x >= 0 && np.x <= 59 && np.y >= 0 && np.y <= 34) {
				char obs = getObservacaoPosicao(np);
				System.out.println(obs);
				
				if(this.inimigoAVista || obs == 's') {
					System.out.println("atacar inimigo a vista");
					this.estadoPlayer = Estado.Atacando;
					return "atacar";
				}
				if(obs == '_') {
					this.estadoPlayer = Estado.Procurando_ouro;
					System.out.println("andar");
					return "andar";
				}
				else if(obs == 'f' || obs == 'F') {
					this.estadoPlayer = Estado.Desviando_ameaca1;
					System.out.println("andar_re");
					return "andar_re";
				}
				else if(obs == 'v' || obs == 'V') {
					this.estadoPlayer = Estado.Desviando_ameaca1;
					System.out.println("andar_re");
					return "andar_re";
				}
				else if(obs == 't' || obs == 'T') {
					this.estadoPlayer = Estado.Procurando_ouro;
					System.out.println("virar_direita parede!");
					return "virar_direita";
				}
				else {
					this.estadoPlayer = Estado.Procurando_ouro;
					System.out.println("andar pq sim");
					return "andar";
				}
			}
			
		case Desviando_ameaca1:
			this.estadoPlayer = Estado.Desviando_ameaca2;
			System.out.println("virar_direita");
			return "virar_direita";
			
		case Desviando_ameaca2:
			this.estadoPlayer = Estado.Procurando_ouro;
			System.out.println("andar");
			return "andar";
			
		case Procurando_Powerup:
			
		case Atacando:
			char obs = getObservacaoPosicao(np);
			if(this.inimigoAVista || obs == 's') {
				System.out.println("atacar inimigo a vista");
				this.estadoPlayer = Estado.Atacando;
				return "atacar";
			}
			else {
				this.estadoPlayer = Estado.Procurando_ouro;
				System.out.println("andar");
				return "andar";	
			}
		default:
			System.out.println("Nada para fazer");
			return "";
		}	

	}
}
