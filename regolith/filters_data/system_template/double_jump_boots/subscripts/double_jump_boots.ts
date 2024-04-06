//@ts-check
import {
	world,
	system,
	EntityEquippableComponent,
	EquipmentSlot,
	Player,
} from "@minecraft/server";

/**
 * Used to keep track of the double jump state of the player.
 */
enum DoubleJumpState {
	ON_GROUND,
	FIRST_JUMP_PRESSED,
	FIRST_JUMP_RELEASE,
	DOUBLE_JUMP_USED,
}

/**
 * Used to keep track of the players who try to use the double jump.
 */
class DoubleJumpController {
	/** Maps player IDs to the double jump states of the players. */
	private playerStates: Map<string, DoubleJumpState>;

	constructor() {
		this.playerStates = new Map();
	}

	tick() {
		for (let player of world.getAllPlayers()) {
			// Chek if player has boots
			const inventory = player.getComponent(
				EntityEquippableComponent.componentId
			) as EntityEquippableComponent;
			let hasBoots = false;
			if (inventory !== undefined) {
				hasBoots =
					inventory.getEquipment(EquipmentSlot.Feet)?.typeId ==
					"nusiq:double_jump_boots";
			}

			// If has boots tick the player, otherwise remove from the map
			if (hasBoots) {
				this.tickPlayer(player);
			} else {
				this.playerStates.delete(player.id);
			}
		}
	}

	private tickPlayer(player: Player) {
		const state = this.playerStates.get(player.id);

		// Register unknown players
		if (state === undefined) {
			this.playerStates.set(player.id, DoubleJumpState.ON_GROUND);
		}

		// If on ground, change state and return
		if (player.isOnGround) {
			this.playerStates.set(player.id, DoubleJumpState.ON_GROUND);
			return;
		}
		// else: Player is not on ground
		switch (state) {
			case DoubleJumpState.ON_GROUND:
				if (player.isJumping) {
					this.playerStates.set(player.id, DoubleJumpState.FIRST_JUMP_PRESSED);
				} else {
					// Player can drop from a ledge and still double jump
					this.playerStates.set(player.id, DoubleJumpState.FIRST_JUMP_RELEASE);
				}
				break;
			case DoubleJumpState.FIRST_JUMP_PRESSED:
				if (!player.isJumping) {
					this.playerStates.set(player.id, DoubleJumpState.FIRST_JUMP_RELEASE);
				}
				break;
			case DoubleJumpState.FIRST_JUMP_RELEASE:
				if (player.isJumping) {
					// Perform the double jump and update the state
					this.playerStates.set(player.id, DoubleJumpState.DOUBLE_JUMP_USED);
					const { x, y, z } = player.getViewDirection();
					const verticalLength = Math.sqrt(x * x + z * z);
					const horizontalLength = Math.sqrt(
						verticalLength * verticalLength + y * y
					);
					player.applyKnockback(
						x,
						z,
						horizontalLength * 6,
						verticalLength * 0.5
					);
				}
				break;
		} // case DOUBLE_JUMP_USEd: pass
	}
}

// THE BODY OF THE SCRIPT
const doubleJumpController = new DoubleJumpController();
function main() {
	doubleJumpController.tick();
}
system.runInterval(main, 1);
