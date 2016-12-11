<?php
	extract($_GET);
	if($value=="res"){
		$jsonRep=json_decode(file_get_contents("../data/rest_search.json"));
		$jsonRep2=json_decode(file_get_contents("../data/restname_id.json"));
		$newJson=array();
		foreach($jsonRep as $id=>$val){
			foreach($jsonRep2 as $id2=>$name){
				$smallJson=array();
				if($id==$id2){
					foreach($val[1] as $dish=>$ratings){
						$smallJson[ucwords($dish)]=$ratings;
					}
					$newJson[ucwords($name)]=$smallJson;
					break;
				}
			}
		}
		echo json_encode($newJson);
	}
	if($value=="dish"){
		$jsonRep=json_decode(file_get_contents("../data/dish_search.json"));
		$jsonRep2=json_decode(file_get_contents("../data/restname_id.json"));
		$newJson=array();
		foreach($jsonRep as $dish=>$val){
			$dishRest=array();
			foreach($val as $rest){
				$newRest=array();
				foreach($jsonRep2 as $id=>$name){
					if($id==$rest[0]){
						$newRest[]=ucwords($name);
						foreach($rest as $index=>$item){
							if($index!=0)
								$newRest[]=$item;
						}
						$dishRest[]=$newRest;
						break;
					}

				}
			}
			$newJson[ucwords($dish)]=$dishRest;
		}
		echo json_encode($newJson);
	}
?>


