from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0701_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0701_1 ._SN',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_342",          # 01, 1
        "Function_2_B07",          # 02, 2
        "Function_3_1BC0",         # 03, 3
        "Function_4_2973",         # 04, 4
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 42160, 4000, 32689, 135)
    SetChrPos(0x103, 41220, 4000, 31800, 90)
    SetChrPos(0xF8, 41110, 4000, 32970, 135)
    SetChrPos(0xF9, 42320, 4000, 33710, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_124")
    SetChrPos(0xF9, 41110, 4000, 32970, 135)
    SetChrPos(0xF8, 42320, 4000, 33710, 135)

    label("loc_124")

    TurnDirection(0xFE, 0x101, 0)
    OP_6D(42900, 4000, 32590, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #0
        0xFE,
        (
            "What is going on with this fog?\x01",
            "I may as well be swimming, the way\x01",
            "things are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#1000FUm, excuse me.\x01",
            "Can I have a moment?\x02\x03",

            "I need to ask you something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "Oh, sure, what's up?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "\x07\x05Estelle explained that she was looking for a wheat-colored\x01",
            "cat.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #4
        0xFE,
        "A cat, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "Afraid I haven't seen it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#1000FHuh? Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "The one who saw it was probably Skip.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Ask him what's up.\x01",
            "He should be down by the warehouses.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x74, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_342(): pass

    label("Function_1_342")

    EventBegin(0x0)
    OP_8C(0xFE, 135, 0)
    Fade(1000)
    SetChrPos(0x101, 36380, 0, 50200, 90)
    SetChrPos(0x103, 35330, 0, 49670, 90)
    SetChrPos(0xF8, 34610, 0, 50660, 90)
    SetChrPos(0xF9, 33650, 0, 49980, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C3")
    SetChrPos(0xF9, 34610, 0, 50660, 90)
    SetChrPos(0xF8, 33650, 0, 49980, 90)

    label("loc_3C3")

    OP_4A(0xFE, 255)
    OP_6D(37130, 0, 50200, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #9
        0xFE,
        "This freakin' fog! The HUMIDITY!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "I'm going to need to get everything set\x01",
            "up to withstand this. But we might as well\x01",
            "be underwater, the way things are...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1011FUm, excuse me.\x01",
            "Can I have a moment?\x02\x03",

            "I need to ask you something.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #12
        0xFE,
        "Hmm? Sure, what is it?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "\x07\x05Estelle explained that she was looking for a wheat-colored\x01",
            "cat.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #14
        0xFE,
        "Oh, yeah, that cat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Yeah, I saw it.\x01",
            "Around noon today.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_602")

    ChrTalk(    #16
        0x105,
        "#040FSo during midday.\x02",
    )

    CloseMessageWindow()
    Jump("loc_68A")

    label("loc_602")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62E")

    ChrTalk(    #17
        0x107,
        "#060FSo midday, then?\x02",
    )

    CloseMessageWindow()
    Jump("loc_68A")

    label("loc_62E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_664")

    ChrTalk(    #18
        0x104,
        "#030FHere around midday? Hmm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_68A")

    label("loc_664")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_68A")

    ChrTalk(    #19
        0x108,
        "#070FMidday, then.\x02",
    )

    CloseMessageWindow()

    label("loc_68A")


    ChrTalk(    #20
        0x101,
        (
            "#1002FWhich lines up perfectly with what Ida\x01",
            "told us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x103,
        (
            "#020FDo you know where the cat is now,\x01",
            "or where it was headed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "No idea, sorry. Today's been kind of crazy.\x01",
            "Where would it even have...mmm, yeah, I dunno.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "Sorry, I haven't seen it since then,\x01",
            "and I have no idea where it might've gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "Cats kinda go where they please, y'know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1016FYeah, I guess they do...\x02\x03",

            "#1015FBut, well, that's it for us, then.\x01",
            "Our trail of clues stops right here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "Well, hold on, there. Why not ask Quint?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "He just went into town for dinner.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x103,
        "#023FQuint?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "Yeah, he's the Cecilia's helmsman.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "He was talking about the cat, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#1006FCool! Time to find Quint, then.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_98D")

    ChrTalk(    #32
        0x106,
        (
            "#050FLet's go.\x01",
            "He's at the restaurant in town, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABA")

    label("loc_98D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E9")

    ChrTalk(    #33
        0x108,
        (
            "#070FLet's see if we can catch him.\x01",
            "The restaurant in town, I assume?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABA")

    label("loc_9E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A63")

    ChrTalk(    #34
        0x104,
        (
            "#030FLet us have the helmsman steer us true,\x01",
            "then. I would imagine he is at the\x01",
            "restaurant in town.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABA")

    label("loc_A63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ABA")

    ChrTalk(    #35
        0x105,
        (
            "#040FYes, let's. I believe I saw a restaurant\x01",
            "near the town square?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABA")


    ChrTalk(    #36
        0x103,
        "#020FThank you for the help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "No problem. Good luck!\x02",
    )

    CloseMessageWindow()
    OP_28(0x74, 0x1, 0x10)
    OP_28(0x74, 0x1, 0x20)
    EventEnd(0x0)
    Return()

    # Function_1_342 end

    def Function_2_B07(): pass

    label("Function_2_B07")

    EventBegin(0x0)
    OP_8C(0xFE, 180, 0)
    Fade(1000)
    SetChrPos(0x101, 30460, 0, 3220, 270)
    SetChrPos(0xF7, 31440, 0, 3750, 270)
    SetChrPos(0xF8, 31360, 0, 2610, 270)
    SetChrPos(0xF9, 32270, 0, 3270, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B88")
    SetChrPos(0xF9, 31360, 0, 2610, 270)
    SetChrPos(0xF8, 32270, 0, 3270, 270)

    label("loc_B88")

    OP_6D(29790, 0, 2710, 0)
    OP_67(0, 6680, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(213000, 0)
    OP_6E(262, 0)
    OP_4A(0xFE, 255)
    OP_0D()

    ChrTalk(    #38
        0xFE,
        "Ahhhh, so relaxing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#1003F#6PSeriously? *sigh*\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #40
        0xFE,
        "Ooooh! Who have we here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1007F#6PYou're Zosimov, right?\x01",
            "We've been looking for you.\x02\x03",

            "What on earth are you doing\x01",
            "over here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Isn't it obvious? I'm spending a relaxing\x01",
            "evening in the woods! Sort of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "You see, when you're on a ship all the\x01",
            "time, you begin to long for greenery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "So sometimes I just like to kick back\x01",
            "and relax among the trees like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1019F#6PYeah. Of all the forests in Rolent,\x01",
            "this is clearly the best place to get\x01",
            "some 'greenery.' Sure. Why not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x103,
        (
            "#026FWell, for better or worse, we've found\x01",
            "Zosimov.\x02\x03",

            "#020FLet's hurry and finish our business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1002F#6PYeah, gladly.\x02\x03",

            "#1015FSo, uh, we did want to ask you a\x01",
            "few things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "Ohoooo! Ask away.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #49
        (
            "\x07\x05Estelle explained that she was looking for a wheat-colored\x01",
            "cat.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #50
        0xFE,
        "Ah, looking for a cat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x103,
        "#020FWe heard from Quint that you saw one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "I certainly did!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "It was just a bit past noon today.\x01",
            "I was offloading some luggage from the\x01",
            "ship's hold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "Quite an annoying critter,\x01",
            "making a fuss and meowing constantly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1015F#6PThe ship's hold, okay.\x02\x03",

            "#1002FWait, so the cat was INSIDE the ship?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "Well, 'ship's hold' can't mean too much\x01",
            "else, can it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "I suppose the ship could try to 'hold'\x01",
            "the cat another way, but I doubt that'd\x01",
            "end well for the cat OR the ship.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1189")

    ChrTalk(    #58
        0x106,
        (
            "#051FInside the ship, of course.\x02\x03",

            "No wonder we couldn't find her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12E3")

    label("loc_1189")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11E8")

    ChrTalk(    #59
        0x108,
        (
            "#070FYes, inside the ship...\x02\x03",

            "#071FHaha, no wonder we couldn't find her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12E3")

    label("loc_11E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1286")

    ChrTalk(    #60
        0x104,
        (
            "#030FAh, but of course. Inside the Cecilia.\x02\x03",

            "It's no wonder our search was fruitless.\x01",
            "Our quarry is in the one place we did\x01",
            "not search!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12E3")

    label("loc_1286")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12E3")

    ChrTalk(    #61
        0x105,
        (
            "#043FInside the ship, I see.\x02\x03",

            "#047FNo wonder we weren't able to find her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_130C")

    ChrTalk(    #62
        0x107,
        "#067FHeehee! Yeah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_138C")

    label("loc_130C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1334")

    ChrTalk(    #63
        0x105,
        "#040FHaha, quite.\x02",
    )

    CloseMessageWindow()
    Jump("loc_138C")

    label("loc_1334")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1369")

    ChrTalk(    #64
        0x104,
        "#030FHeh, finally! As it were.\x02",
    )

    CloseMessageWindow()
    Jump("loc_138C")

    label("loc_1369")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_138C")

    ChrTalk(    #65
        0x108,
        "#070FHaha, yes.\x02",
    )

    CloseMessageWindow()

    label("loc_138C")


    ChrTalk(    #66
        0x103,
        (
            "#020FAnd that makes the rest simple.\x02\x03",

            "We just need to search the ship.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #67
        0x101,
        "#1006F#4PShouldn't take long, yeah.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #68
        0x101,
        "#1006F#6PWell, thanks for everything, Zosimov!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "Glad to be of...help.\x01",
            "But...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "Er... What to do...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1011F#6PHuh?\x02\x03",

            "Are we missing something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x103,
        "#023FThat's what it sounds like. What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "It's just... Let me ask again, to be sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "You're looking for a 'wheat-colored' cat,\x01",
            "yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1011F#6PYeah, we...\x01",
            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #76
        0x101,
        "#1004F#6POh, no WAY!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "Ah, you've guessed?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "Yes, you are looking for a wheat-colored cat.\x01",
            "But...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "The cat I saw was black as pitch!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_163A")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1678")

    label("loc_163A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1661")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1678")

    label("loc_1661")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1678")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_169F")
    OP_62(0xF6, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_16DD")

    label("loc_169F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C6")
    OP_62(0xF6, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_16DD")

    label("loc_16C6")

    OP_62(0xF6, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_16DD")

    Sleep(120)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1709")
    OP_62(0xF7, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1747")

    label("loc_1709")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1730")
    OP_62(0xF7, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1747")

    label("loc_1730")

    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1747")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176E")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_17AC")

    label("loc_176E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1795")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_17AC")

    label("loc_1795")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_17AC")

    Sleep(2000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17EA")

    ChrTalk(    #80
        0x106,
        "#551FMention that sooner, will ya?\x02",
    )

    CloseMessageWindow()
    Jump("loc_18AA")

    label("loc_17EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_182B")

    ChrTalk(    #81
        0x108,
        "#075FWell, that could have come up sooner.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18AA")

    label("loc_182B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1866")

    ChrTalk(    #82
        0x104,
        "#031FHahaha! An excellent punchline!\x02",
    )

    CloseMessageWindow()
    Jump("loc_18AA")

    label("loc_1866")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18AA")

    ChrTalk(    #83
        0x105,
        (
            "#045FW-Well, that certainly turns things\x01",
            "around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18AA")


    ChrTalk(    #84
        0xFE,
        (
            "I'm sorry... The relevance of that detail\x01",
            "didn't strike me until just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "I am certain there's a cat on board,\x01",
            "however!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "Why not take a look anyway? Perhaps your\x01",
            "cat has taken a tar bath, or gotten covered\x01",
            "in soot somewhere along the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#1007F#6PThat's a good point...\x02\x03",

            "There is an off chance it's still Aryll.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A50")

    ChrTalk(    #88
        0x107,
        (
            "#560FY-Yeah! Maybe!\x02\x03",

            "Or maybe the black kitty is a friend of\x01",
            "Aryll's!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A50")


    ChrTalk(    #89
        0x103,
        (
            "#025FYes, that's true.\x01",
            "We have no other clues, so we\x01",
            "might as well follow this one.\x02\x03",

            "#020FThat black cat may also be a friend to\x01",
            "Aryll. We should investigate.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B27")

    ChrTalk(    #90
        0x108,
        "#070FYes, let's take a look.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BB7")

    label("loc_1B27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B63")

    ChrTalk(    #91
        0x104,
        "#030FQuite. Let us take flight, then!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BB7")

    label("loc_1B63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B99")

    ChrTalk(    #92
        0x106,
        "#551FNo other real choice here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BB7")

    label("loc_1B99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BB7")

    ChrTalk(    #93
        0x107,
        "#560FYeah!\x02",
    )

    CloseMessageWindow()

    label("loc_1BB7")

    OP_28(0x74, 0x1, 0x100)
    EventEnd(0x0)
    Return()

    # Function_2_B07 end

    def Function_3_1BC0(): pass

    label("Function_3_1BC0")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 43090, 4000, 33470, 180)
    SetChrPos(0x103, 42250, 4000, 34000, 180)
    SetChrPos(0xF8, 42150, 4000, 35100, 180)
    SetChrPos(0xF9, 43120, 4000, 34660, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C3A")
    SetChrPos(0xF9, 42150, 4000, 35100, 180)
    SetChrPos(0xF8, 43120, 4000, 34660, 180)

    label("loc_1C3A")

    TurnDirection(0xFE, 0x101, 0)
    OP_4A(0xFE, 255)
    OP_6D(43090, 4000, 33130, 0)
    OP_67(0, 8370, -10000, 0)
    OP_6B(2930, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_1CE5")

    ChrTalk(    #94
        0xFE,
        "Hey, found the kitty yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        "#1011FWe actually wanted to ask you about that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DB2")

    label("loc_1CE5")


    ChrTalk(    #96
        0xFE,
        "Hmm? Is something up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "You're out rather late. You bracers seem\x01",
            "to have it awfully rough as well, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#1016FWe all do, right now.\x02\x03",

            "#1000FBut that aside, we have a favor\x01",
            "we'd like to ask you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB2")


    ChrTalk(    #99
        0xFE,
        "Oh? And what would that be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x103,
        "#020F#3PWe'd like to search inside the Cecilia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        "Wait. So...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "You want to go inside the Cecilia?\x01",
            "In the cabin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#1015FUh. Yeah?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_1F55")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #104
        (
            "\x07\x05Estelle explained the course of events and the results\x01",
            "of their investigations, and conveyed that there was a\x01",
            "possibility the cat might be on the ship.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #105
        0xFE,
        (
            "I see...\x01",
            "I do understand, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2092")

    label("loc_1F55")


    ChrTalk(    #106
        0xFE,
        "Well, I can't okay that so easily.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "You need to give me a reason.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#1002FUm, well...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #109
        (
            "\x07\x05Estelle explained the course of events and the results\x01",
            "of their investigations, and conveyed that there was a\x01",
            "possibility the cat might be on the ship.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #110
        0xFE,
        "I see... A cat on board.\x02",
    )

    CloseMessageWindow()

    label("loc_2092")


    ChrTalk(    #111
        0xFE,
        (
            "I'm afraid I can't give permission to\x01",
            "board on my own, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "I'm really sorry, but...you'll have to\x01",
            "leave now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1019FErm. What?\x02\x03",

            "I kinda didn't expect to get told off...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "Told off nothing! I can't allow what\x01",
            "I can't allow. Company policy. No exceptions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "Begging won't get you anywhere.\x01",
            "Just head on home.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 400)
    Sleep(400)
    OP_8C(0x101, 270, 400)

    ChrTalk(    #116
        0x101,
        (
            "#4P#1003FFor the love of...\x01",
            "Guess we have no choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x103,
        "#026F#3PWe're not quite done yet.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0x101, 0x20)

    def lambda_2262():
        OP_8C(0xFE, 180, 100)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2262)
    OP_8E(0x103, 0xA6B8, 0xFA0, 0x7C38, 0x3E8, 0x0)
    OP_8C(0x103, 90, 400)
    WaitChrThread(0x101, 0x3)
    ClearChrFlags(0x101, 0x20)
    OP_62(0x103, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #118
        0x103,
        (
            "#520F#3PNooooow.\x01",
            "Why are you being so hardheaded, hmm?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    ChrTalk(    #119
        0xFE,
        "Wh-Wh...\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE)

    ChrTalk(    #120
        0xFE,
        "Wh-What the...?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2366")
    OP_62(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x104)

    ChrTalk(    #121
        0x104,
        "#037F(Oooooh, yes!)\x02",
    )

    CloseMessageWindow()

    label("loc_2366")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23AE")
    OP_62(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x106)

    ChrTalk(    #122
        0x106,
        "#552F(Oooooh, boy...)\x02",
    )

    CloseMessageWindow()

    label("loc_23AE")


    ChrTalk(    #123
        0x103,
        (
            "#027F#3PNow. Why don't you think about it loooong\x01",
            "and haaaard?\x02\x03",

            "If a cat really is on board, that's\x01",
            "trouble for you, too, isn't it?\x02\x03",

            "What happens if it ruins the seats?\x01",
            "Wouldn't that be a tragedy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "W-Well, that is...y-yeah, sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "But, I, I mean...\x01",
            "I can't let you in without permission...\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x103, 0xA708, 0xFA0, 0x7C38, 0x3E8, 0x0)

    ChrTalk(    #126
        0x103,
        (
            "#027F#3PDooon't worry about that.\x01",
            "We won't cause any problems.\x02\x03",

            "Just let us in for a little bit.\x02\x03",

            "#525FSo...what do you say? You'll do it...\x01",
            "for me...won't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_9E(0xFE, 0x32, 0x0, 0x1F4, 0x5DC)

    ChrTalk(    #127
        0xFE,
        "☆△＝`○☆ッ～～!!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #128
        0x101,
        (
            "#1013F(Sch-Sch-Scheraaaaaa!\x01",
            "Using your, your ASSETS like a\x01",
            "weapon like that is so...something!)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26B2")
    OP_62(0x104, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #129
        0x104,
        (
            "#039F(Ooooooh!!\x01",
            "My envy is fathomless!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26E2")

    ChrTalk(    #130
        0x107,
        "#562F(Oooooh, Scheraaaaa...)\x02",
    )

    CloseMessageWindow()

    label("loc_26E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2704")

    ChrTalk(    #131
        0x105,
        "#540F.   .   .\x02",
    )

    CloseMessageWindow()

    label("loc_2704")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2744")

    ChrTalk(    #132
        0x106,
        (
            "#551F(Ssseriously...\x01",
            "That really necessary?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2744")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27B3")

    ChrTalk(    #133
        0x108,
        (
            "#071F(Haha! Well, one's attractiveness can be\x01",
            "used in a 'martial art' of sorts, I suppose.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27B3")

    OP_8F(0x103, 0xA514, 0xFA0, 0x7C38, 0x3E8, 0x0)

    ChrTalk(    #134
        0x103,
        "#526F#3PSo? Do we have an understanding?\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #135
        0xFE,
        "Uh, I, I...I guess!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "But, I... Oh, man, this could get me...\x01",
            "Look, just for a minute, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "A-And never tell anyone about ANY of this!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x103,
        "#021F#3PHeehee! Of course.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_71(0xA, 0x4)
    OP_8C(0xFE, 90, 0)
    ClearChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, 43100, 4000, 30900, 90)
    SetChrPos(0x103, 42250, 4000, 34000, 180)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #139
        0xFE,
        "#6POkay, there.\x02",
    )

    CloseMessageWindow()
    OP_8E(0xFE, 0xA848, 0xFA0, 0x7D3C, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #140
        0xFE,
        "Get in, quick!\x02",
    )

    CloseMessageWindow()
    OP_28(0x74, 0x1, 0x200)
    EventEnd(0x0)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_3_1BC0 end

    def Function_4_2973(): pass

    label("Function_4_2973")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2988")
    Return()

    label("loc_2988")

    EventBegin(0x1)
    OP_4A(0x9, 255)
    TurnDirection(0x9, 0x0, 0)
    OP_6D(41340, 4000, 35650, 1000)

    ChrTalk(    #141
        0x9,
        "Hey! Where are you going?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x9,
        (
            "Hurry up and get inside, before\x01",
            "somebody sees!\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    OP_4B(0x9, 255)
    OP_8C(0x9, 270, 0)
    Return()

    # Function_4_2973 end

    SaveToFile()

Try(main)
