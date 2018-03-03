from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4138   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4138.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
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
        'Major Vander',                         # 9
        'Olivier',                              # 10
        'Ambassador Crainagh',                  # 11
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


    AddCharChip(
        'ED6_DT07/CH02190 ._CH',             # 00
        'ED6_DT07/CH00030 ._CH',             # 01
        'ED6_DT27/CH03710 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH02190P._CP',             # 00
        'ED6_DT07/CH00030P._CP',             # 01
        'ED6_DT27/CH03710P._CP',             # 02
    )

    DeclNpc(
        X                   = 1160,
        Z                   = 4000,
        Y                   = 16920,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_122",          # 00, 0
        "Function_1_13F",          # 01, 1
        "Function_2_174",          # 02, 2
    )


    def Function_0_122(): pass

    label("Function_0_122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_13E")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_13E")

    Return()

    # Function_0_122 end

    def Function_1_13F(): pass

    label("Function_1_13F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_157")
    OP_B1("t4138_n")
    Jump("loc_160")

    label("loc_157")

    OP_B1("t4138_y")

    label("loc_160")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_173")
    OP_82(0x80, 0x0)
    OP_64(0x1, 0x1)

    label("loc_173")

    Return()

    # Function_1_13F end

    def Function_2_174(): pass

    label("Function_2_174")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    Sleep(500)
    OP_1D(0x11)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #0
        (
            "\x07\x05Some time had passed since the crisis involving\x01",
            "the Aureole came to an end.\x02\x03",

            "One by one, many of those who fought to bring it\x01",
            "to an end set off from the land of Liberl to \x01",
            "begin new lives...\x02\x03",

            "And today, yet another of their group was ready\x01",
            "to leave the kingdom behind as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, 2610, 0, 72170, 225)
    SetChrPos(0x11, 1380, 0, 72520, 180)
    SetChrPos(0x12, 1430, 0, 70600, 0)
    OP_6D(3610, 0, 73730, 0)
    OP_67(0, 4450, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(277, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #1
        0x12,
        (
            "#1100FI-I can't believe that you...\x02\x03",

            "I mean, my deepest apologies for not noticing that\x01",
            "you were His Highness Prince Olivert sooner!\x02\x03",

            "While I may not have had the opportunity to see\x01",
            "you in public before now, I realize that is no\x01",
            "excuse... I do hope you will forgive my ignorance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x11,
        (
            "#030F#5PHaha. There's no need to be so apologetic, \x01",
            "Ambassador.\x02\x03",

            "If anyone deserves to be blamed here, it's me for\x01",
            "falsifying my identity, and not you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x12,
        (
            "#1100FI-I thank you for your mercy...\x02\x03",

            "Still, I can hardly believe that you went so far\x01",
            "just to come here and enjoy yourself.\x02\x03",

            "It's just as well you came out of it all safely,\x01",
            "or this could have become a major international\x01",
            "incident.\x02\x03",

            "I dread to think what would have happened to me\x01",
            "in that case... You were really playing with \x01",
            "fire this time, Your Highness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x11,
        (
            "#030F#5PHeh. Still, thanks to that, I was able to get the\x01",
            "kind of firsthand knowledge about this country\x01",
            "that no amount of books could have given me.\x02\x03",

            "Regardless, this won't be the last this country\x01",
            "sees of me, so I hope I'll be able to count on\x01",
            "you on future visits, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #5
        0x12,
        "#1100FWh-What?!\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(    #6
        0x11,
        (
            "#030F#5PPerhaps next time I could even involve you more\x01",
            "directly in the proceedings. What say you to a\x01",
            "little hot springs trip together?\x02\x03",

            "Heh. We could even invite Ambassador Cochrane to\x01",
            "join us.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #7
        0x12,
        "#1100FY-Your Highness...\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #8
        0x10,
        (
            "#270F#2P*cough* Ambassador, if I may...\x02\x03",

            "Please don't take every one of his worthless jokes\x01",
            "at face value, or this meeting will take the rest\x01",
            "of the day.\x02\x03",

            "I think it would be best to get right to the point\x01",
            "and discuss the request regarding our return home\x01",
            "that we made  earlier.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 45, 400)

    ChrTalk(    #9
        0x12,
        (
            "#1100FY-Yes, of course... I'll arrange an airship at\x01",
            "once.\x02\x03",

            "I should be able to have one of the high-speed\x01",
            "airships for diplomats arranged for tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        "#030F#5PHeh. You have our thanks.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 0, 400)

    ChrTalk(    #11
        0x12,
        (
            "#1100FIt's an honor to be able to do anything to help\x01",
            "you, Your Highness.\x02\x03",

            "Besides, I think you're right that in these times,\x01",
            "returning on a military airship would be an unwise\x01",
            "move...\x02\x03",

            "Especially with how tense the situation at the\x01",
            "border is...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrFlags(0x12, 0x80)
    SetChrPos(0x11, 61690, 0, 10180, 90)
    SetChrPos(0x10, 59140, 0, 10300, 90)
    OP_6D(61850, 0, 11710, 0)
    OP_67(0, 4780, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(277, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #12
        0x10,
        (
            "#270F#6PSo, regarding what the ambassador said...\x02\x03",

            "What exactly is it that you're on the alert for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x11,
        (
            "#030F#2PHeh. I just want to avoid the possibility of any\x01",
            "unfortunate accidents.\x02\x03",

            "What I did will have caused the hawk faction in\x01",
            "the Empire to completely lose face.\x02\x03",

            "There's just no telling what they'll choose to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "#270F#6PIn other words...\x02\x03",

            "You think there's a possibility that there may be\x01",
            "an attempt on your life disguised as an accident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        (
            "#030F#2PMy instinct is that the chancellor is far too \x01",
            "patient a man to try doing something so rash.\x02\x03",

            "Still, if I was in his position, I can't deny the\x01",
            "possibility I may try to use this opportunity.\x02\x03",

            "Once that thought occurred to me, no precaution\x01",
            "seemed too great, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "#270F#6P...\x02\x03",

            "The 7th Armored Division I serve is your ally,\x01",
            "as you well know.\x02\x03",

            "If anything were to happen, they would be right\x01",
            "there for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        "#030F#2PWell, that's certainly reassuring to know...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 400)
    Sleep(300)

    ChrTalk(    #18
        0x11,
        (
            "#030F#2PBut as I'm sure you know, acting rashly in the\x01",
            "current situation is just what our enemy would\x01",
            "want us to do.\x02\x03",

            "It's similar to street fights in a sense -- the\x01",
            "first one to draw their weapon is the one in the\x01",
            "wrong.\x02\x03",

            "If I decide to rely on brute force, they'll have\x01",
            "every reason to decry me as a rebellious traitor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "#270F#6PI suppose you're right...\x02\x03",

            "Sometimes trying too hard to defend yourself can\x01",
            "end up cornering you instead.\x02\x03",

            "Perhaps sometimes the best method of self-defense\x01",
            "is to do nothing at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        (
            "#030F#2PHeh. Indeed.\x02\x03",

            "As long as our enemy doesn't know what we plan to\x01",
            "do, they can't do anything to counter it, either.\x02\x03",

            "First, we need to return to Heimdallr and tell\x01",
            "His Majesty the truth of all that happened here.\x02\x03",

            "We can decide what we're going to after seeing\x01",
            "what kind of a reaction we get.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    Sleep(500)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_174 end

    SaveToFile()

Try(main)
