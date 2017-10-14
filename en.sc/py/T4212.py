from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4212   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4212.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Dayan',                                # 9
        'Tooker',                               # 10
        'Helmuth',                              # 11
        'Duke Dunan',                           # 12
        'Phillip',                              # 13
        'Capital Citizen',                      # 14
        'Capital Citizen',                      # 15
        'Capital Citizen',                      # 16
        'Senator Walter',                       # 17
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
        'ED6_DT07/CH01570 ._CH',             # 00
        'ED6_DT07/CH01560 ._CH',             # 01
        'ED6_DT07/CH01220 ._CH',             # 02
        'ED6_DT07/CH02140 ._CH',             # 03
        'ED6_DT07/CH02470 ._CH',             # 04
        'ED6_DT07/CH01120 ._CH',             # 05
        'ED6_DT07/CH01020 ._CH',             # 06
        'ED6_DT07/CH01200 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01570P._CP',             # 00
        'ED6_DT07/CH01560P._CP',             # 01
        'ED6_DT07/CH01220P._CP',             # 02
        'ED6_DT07/CH02140P._CP',             # 03
        'ED6_DT07/CH02470P._CP',             # 04
        'ED6_DT07/CH01120P._CP',             # 05
        'ED6_DT07/CH01020P._CP',             # 06
        'ED6_DT07/CH01200P._CP',             # 07
    )

    DeclNpc(
        X                   = -68100,
        Z                   = 0,
        Y                   = -32320,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x111,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = -65500,
        Z                   = 0,
        Y                   = -41540,
        Direction           = 279,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -61160,
        Z                   = 0,
        Y                   = -35270,
        Direction           = 86,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -62490,
        Z                   = 0,
        Y                   = -31190,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -62170,
        Z                   = 0,
        Y                   = -33200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -63350,
        Z                   = 0,
        Y                   = -33470,
        Direction           = 21,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -65060,
        Z                   = 0,
        Y                   = -31070,
        Direction           = 73,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -64550,
        Z                   = 0,
        Y                   = -32810,
        Direction           = 48,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -65099,
        Z                   = 0,
        Y                   = -44670,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )


    ScpFunction(
        "Function_0_20A",          # 00, 0
        "Function_1_2D6",          # 01, 1
        "Function_2_2FC",          # 02, 2
        "Function_3_677",          # 03, 3
        "Function_4_971",          # 04, 4
        "Function_5_A82",          # 05, 5
        "Function_6_E4D",          # 06, 6
        "Function_7_1319",         # 07, 7
        "Function_8_1397",         # 08, 8
        "Function_9_1417",         # 09, 9
        "Function_10_1463",        # 0A, 10
        "Function_11_152C",        # 0B, 11
    )


    def Function_0_20A(): pass

    label("Function_0_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_22D")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_2B2")

    label("loc_22D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_292")
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xB, -62830, 0, -30860, 220)
    ClearChrFlags(0xB, 0x10)
    SetChrPos(0xC, -61160, 0, -34980, 335)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x9, -65500, 0, -43300, 165)
    SetChrFlags(0x9, 0x10)
    Jump("loc_2B2")

    label("loc_292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2A1")
    SetChrFlags(0xA, 0x80)
    Jump("loc_2B2")

    label("loc_2A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2B2")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)

    label("loc_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D5")
    SetMapFlags(0x10000000)
    Event(0, 11)

    label("loc_2D5")

    Return()

    # Function_0_20A end

    def Function_1_2D6(): pass

    label("Function_1_2D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F2")
    OP_B1("t4212_y")
    Jump("loc_2FB")

    label("loc_2F2")

    OP_B1("t4212_n")

    label("loc_2FB")

    Return()

    # Function_1_2D6 end

    def Function_2_2FC(): pass

    label("Function_2_2FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_436")

    ChrTalk(    #0
        0xFE,
        (
            "Ever since orbments stopped working\x01",
            "a lot of citizens have been petitioning\x01",
            "for aid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "If the duke wasn't here, we'd have\x01",
            "a hard time getting to all of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "Still, though...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "The economic damage in just the capital alone\x01",
            "from the aftereffects of the orbal shutdown\x01",
            "will be terrible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_673")

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_567")

    ChrTalk(    #4
        0xFE,
        (
            "Phew! Well, that solves the mystery\x01",
            "of the forged budgets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "It seems the missing funds were used\x01",
            "in the development of the Orgueille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "If they'd finished that thing in time\x01",
            "for the coup d'etat, I wonder how\x01",
            "things would have turned out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "...It's horrifying to even think about.\x02",
    )

    CloseMessageWindow()
    Jump("loc_673")

    label("loc_567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_673")

    ChrTalk(    #8
        0xFE,
        "We're still cleaning up after the coup d'etat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Right now I'm investigating the Intelligence\x01",
            "Division's budgets and their real expenses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "From the looks of it, there are signs the\x01",
            "budget was manipulated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "Where could this money have gone to...\x02",
    )

    CloseMessageWindow()

    label("loc_673")

    TalkEnd(0xFE)
    Return()

    # Function_2_2FC end

    def Function_3_677(): pass

    label("Function_3_677")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_799")

    ChrTalk(    #12
        0xFE,
        (
            "As I said, we are currently investigating\x01",
            "the cause of the orbal shutdown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "As Queen Alicia is currently otherwise occupied,\x01",
            "I'm afraid you will not be able to meet with her\x01",
            "right this moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "As soon as we know anything, we will\x01",
            "contact the embassy immediately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96D")

    label("loc_799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_860")

    ChrTalk(    #15
        0xFE,
        (
            "It's great to hear that Captain\x01",
            "Kanone was captured...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Now we've got to pass a budget\x01",
            "to repair harbor facilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "Aaaaaahhh, Sweet Aidios, please let this\x01",
            "be the end of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96D")

    label("loc_860")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_96D")

    ChrTalk(    #18
        0xFE,
        (
            "My duties are slowly normalizing,\x01",
            "but I'm still quite busy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "As ever, there are still many inquiries\x01",
            "from the citizenry about the coup d'etat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I'm in charge of various kinds of reparations,\x01",
            "but there's just a mountain of problems to\x01",
            "get through.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96D")

    TalkEnd(0xFE)
    Return()

    # Function_3_677 end

    def Function_4_971(): pass

    label("Function_4_971")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_A7E")

    ChrTalk(    #21
        0xFE,
        (
            "Ah, I imagine my wife's enjoying non-stop\x01",
            "fishing by now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "At this rate, not only am I going to be worthless\x01",
            "as a man, but my position as her husband will\x01",
            "be in danger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "All right! If I just train in secret, I'm sure\x01",
            "I can catch up to my wife!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A7E")

    TalkEnd(0xFE)
    Return()

    # Function_4_971 end

    def Function_5_A82(): pass

    label("Function_5_A82")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_C82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B95")

    ChrTalk(    #24
        0xB,
        (
            "#223FYou are...\x02\x03",

            "#220FIf you wish to meet with Her Highness or Klaudia,\x01",
            "you likely won't be able to for a while.\x02\x03",

            "If you want to know the details,\x01",
            "you should ask Hilda.\x02\x03",

            "I'm sorry, but I have been busy all\x01",
            "morning dealing with petitioners, so...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_C7F")

    label("loc_B95")


    ChrTalk(    #25
        0xB,
        (
            "#220FIf you wish to meet with Her Highness or Klaudia,\x01",
            "you likely won't be able to for a while.\x02\x03",

            "If you want to know the details,\x01",
            "you should ask Hilda.\x02\x03",

            "I'm sorry, but I have been busy all\x01",
            "morning dealing with petitioners, so...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7F")

    Jump("loc_E49")

    label("loc_C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_E49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DED")

    ChrTalk(    #26
        0xB,
        (
            "#222FHmmmmm...\x02\x03",

            "To think such unknown and mysterious\x01",
            "people are traveling about in Liberl...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1011F(Wow. Don't think I've ever seen such a\x01",
            "serious look on his face.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x105,
        (
            "#040F(It seems like this recent event has made my\x01",
            "uncle much more aware of the existence of\x01",
            "the society.)\x02\x03",

            "(Perhaps he has his own thoughts\x01",
            "on the matter.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1669)
    Jump("loc_E49")

    label("loc_DED")


    ChrTalk(    #29
        0xB,
        (
            "#222FTo think such unknown and mysterious\x01",
            "people are traveling about in Liberl...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E49")

    TalkEnd(0xFE)
    Return()

    # Function_5_A82 end

    def Function_6_E4D(): pass

    label("Function_6_E4D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1047")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE3")

    ChrTalk(    #30
        0xFE,
        (
            "#721FMy, my, why if it isn't young Joshua\x01",
            "and Miss Estelle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        (
            "#1040FPhillip, it's been quite some time.\x02\x03",

            "Ever since the birthday celebrations, I believe,\x01",
            "but...I'm glad to see you're well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "#720FYes, thank you.\x02\x03",

            "While you were away, Miss Estelle has\x01",
            "been most good to His Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        "#1044FEstelle has...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#1008FAww, I didn't do anything that big.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        "#1040F...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20F1)
    Jump("loc_1044")

    label("loc_FE3")


    ChrTalk(    #36
        0xFE,
        (
            "#720FThe young master has finally found the\x01",
            "will to work.\x02\x03",

            "I hope he can keep it up, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1044")

    Jump("loc_1315")

    label("loc_1047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1315")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12DA")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #37
        0xFE,
        "#720FMy, my, why if it isn't Miss Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#1000FPhillip...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "#720FAllow me to offer my sincerest\x01",
            "gratitude for rescuing the duke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1018FNo, thank you for looking after everyone,\x01",
            "Phillip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "#722FNo, not at all.\x02\x03",

            "I fear I am most pitiable. That is\x01",
            "the most I could do, unfortunately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1015FBut, it's because you were there that we could\x01",
            "go off to the harbor without having to worry\x01",
            "about everyone, so...\x02\x03",

            "#1001FIn that sense, the fact that the duke\x01",
            "was saved was thanks to you, Phillip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "#721FMiss Estelle... What gracious words.\x01",
            "I am not worthy.\x02\x03",

            "#720FI hope the duke finds this a chance\x01",
            "to change...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x166A)
    Jump("loc_1315")

    label("loc_12DA")


    ChrTalk(    #44
        0xFE,
        (
            "#720FI hope the duke finds this a chance\x01",
            "to change...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1315")

    TalkEnd(0xFE)
    Return()

    # Function_6_E4D end

    def Function_7_1319(): pass

    label("Function_7_1319")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1393")

    ChrTalk(    #45
        0xFE,
        "Duke Dunan's a better person than I'd thought.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "But, his hairstyle is as terrible as the\x01",
            "rumors say...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1393")

    TalkEnd(0xFE)
    Return()

    # Function_7_1319 end

    def Function_8_1397(): pass

    label("Function_8_1397")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1413")

    ChrTalk(    #47
        0xFE,
        (
            "Knowing the throne is doing its best to\x01",
            "respond to the situation is a relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "We gotta do our best too.\x02",
    )

    CloseMessageWindow()

    label("loc_1413")

    TalkEnd(0xFE)
    Return()

    # Function_8_1397 end

    def Function_9_1417(): pass

    label("Function_9_1417")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_145F")

    ChrTalk(    #49
        0xFE,
        (
            "I see... Seems the queen's got a lot\x01",
            "to think about too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_145F")

    TalkEnd(0xFE)
    Return()

    # Function_9_1417 end

    def Function_10_1463(): pass

    label("Function_10_1463")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1528")

    ChrTalk(    #50
        0xFE,
        (
            "I am Walter, a senator with the\x01",
            "Republic's Parliament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Is... Is it not reasonable to expect\x01",
            "a more decisive answer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "When exactly will I be able to contact my\x01",
            "home country?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1528")

    TalkEnd(0xFE)
    Return()

    # Function_10_1463 end

    def Function_11_152C(): pass

    label("Function_11_152C")

    EventBegin(0x0)
    OP_6D(-62620, 0, -30760, 0)
    OP_67(0, 5140, -10000, 0)
    OP_6B(2970, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -62430, 0, -40080, 0)
    SetChrPos(0x102, -63520, 0, -40530, 0)
    SetChrPos(0xF8, -61650, 0, -40780, 0)
    SetChrPos(0xF9, -62780, 0, -41900, 0)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #53
        0xD,
        (
            "Ever since orbments stopped, nights are\x01",
            "dark and cold, and it's hard to cook...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xF,
        "Every day is just unbearable!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xE,
        (
            "#1PHow does the throne intend to respond\x01",
            "to this situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xB,
        (
            "#225F#6PAh, if you will allow me...\x02\x03",

            "#222FThe Orbal Shutdown Phenomenon is currently\x01",
            "being investigated primarily under the\x01",
            "jurisdiction of the Royal Army.\x02\x03",

            "We have no other details on the situation\x01",
            "at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xF,
        "That's... That's absurd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xB,
        (
            "#222F#6PNow, calm yourself. Certainly there\x01",
            "is much we do not know...\x02\x03",

            "This is exactly why it is the intent of\x01",
            "Queen Alicia to support the citizens as\x01",
            "much as possible.\x02\x03",

            "#225FFor example, the East Block's\x01",
            "History Museum has been opened\x01",
            "to the public for free.\x02\x03",

            "#220FFurthermore, with the queen's promise\x01",
            "of support, dining establishments are\x01",
            "staying open as long as possible.\x02\x03",

            "By doing so, we hope the citizenry will\x01",
            "reclaim their calm.\x02\x03",

            "Also, in case of emergency, we have\x01",
            "plans to use the Grand Arena as an\x01",
            "evacuation site, and...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(-61920, 0, -38980, 0)
    OP_67(0, 6840, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #59
        0x101,
        (
            "#1004F#4PWhoa. Is this real life? The duke seems\x01",
            "like he's actually saying really reasonable\x01",
            "things...\x02\x03",

            "#1015FI know, is it like the Martial Arts Competition\x01",
            "where he's being forced to say it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x102,
        (
            "#1040F#2PNo... Unlike that greeting, this isn't\x01",
            "a situation where all he has to do is\x01",
            "say something arranged in advance...\x02\x03",

            "He's clearly speaking his own words\x01",
            "based on his own will and thoughts.\x02\x03",

            "I suppose something acted as a trigger\x01",
            "to start changing the duke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#1015F#4PHmmm...\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_A2(0x20F0)
    OP_4B(0xB, 255)
    OP_4B(0xC, 255)
    OP_4B(0xD, 255)
    OP_4B(0xE, 255)
    OP_4B(0xF, 255)
    EventEnd(0x0)
    Return()

    # Function_11_152C end

    SaveToFile()

Try(main)
