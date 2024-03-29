import discord
from utils.general import is_user_authorized, create_embed

async def delete_response(interaction: discord.Interaction, bot_info: discord.AppInfo, post: dict, view: discord.ui.View):
	"""
	Returns the base response to delete a post

	Args
	----
		- interaction (discord.Interaction): The interaction to respond to
		- bot_info (discord.AppInfo): The bot's application info
		- post (dict): The post to delete
	"""

	if not is_user_authorized(interaction.user.id, bot_info):
		return await interaction.response.send_message(
			embed = create_embed(
				"Error",
				"You do not have permission to delete posts.\nPlease ask an administrator for access if you believe this to be in error.",
				'error'
			),
			ephemeral = True
		)

	return await interaction.response.send_message(
		embed = create_embed(
			"Confirmation",
			"Are you sure you want to delete this post?",
			'info'
		),
		view = view(post = post, bot_info = bot_info),
		ephemeral = True
	)

async def edit_response(interaction: discord.Interaction, bot_info: discord.AppInfo, post: dict, view: discord.ui.View):
	"""
	Returns the modal to edit a post

	Args
	----
		- interaction (discord.Interaction): The interaction to respond to
		- bot_info (discord.AppInfo): The bot's application info
		- post (dict): The post to edit
	"""

	if not is_user_authorized(interaction.user.id, bot_info):
		return await interaction.response.send_message(
			embed = create_embed(
				"Error",
				"You do not have permission to edit posts.\nPlease ask an administrator for access if you believe this to be in error.",
				'error'
			),
			ephemeral = True
		)

	return await interaction.response.send_modal(view(post = post))
