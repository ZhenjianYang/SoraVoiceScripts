from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C2200   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2200.x',
        MapIndex            = 84,
        MapDefaultBGM       = "ed60031",
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
        'Seig',                                 # 9
        'Black-Clad Man',                       # 10
        'Black-Clad Man',                       # 11
        'Vogt',                                 # 12
        'Camera',                               # 13
        'Manoria Byroad',                       # 14
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
        Unknown_3A              = 84,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
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
        'ED6_DT07/CH02320 ._CH',             # 00
        'ED6_DT07/CH01330 ._CH',             # 01
        'ED6_DT07/CH01000 ._CH',             # 02
        'ED6_DT07/CH00440 ._CH',             # 03
        'ED6_DT07/CH00441 ._CH',             # 04
        'ED6_DT06/CH20053 ._CH',             # 05
        'ED6_DT06/CH20085 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH02320P._CP',             # 00
        'ED6_DT07/CH01330P._CP',             # 01
        'ED6_DT07/CH01000P._CP',             # 02
        'ED6_DT07/CH00440P._CP',             # 03
        'ED6_DT07/CH00441P._CP',             # 04
        'ED6_DT06/CH20053P._CP',             # 05
        'ED6_DT06/CH20085P._CP',             # 06
    )

    DeclNpc(
        X                   = 800,
        Z                   = 6130,
        Y                   = -13810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -11460,
        Z                   = 0,
        Y                   = 1930,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -10100,
        Z                   = 0,
        Y                   = 2930,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 620,
        Z                   = 550,
        Y                   = -2470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xC5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1330,
        Z                   = -430,
        Y                   = -46450,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1E6",          # 00, 0
        "Function_1_248",          # 01, 1
        "Function_2_287",          # 02, 2
        "Function_3_29D",          # 03, 3
        "Function_4_A36",          # 04, 4
        "Function_5_A4F",          # 05, 5
        "Function_6_124C",         # 06, 6
        "Function_7_133D",         # 07, 7
        "Function_8_1429",         # 08, 8
    )


    def Function_0_1E6(): pass

    label("Function_0_1E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1FE")
    OP_72(0x2, 0x8)
    Jump("loc_1FE")

    label("loc_1FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_20C")
    Event(0, 5)
    Jump("loc_214")

    label("loc_20C")

    ClearMapFlags(0x40000000)
    AddParty(0xFF, 0xFF)

    label("loc_214")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_220"),
        (SWITCH_DEFAULT, "loc_236"),
    )


    label("loc_220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_233")
    OP_A2(0x438)
    Event(0, 3)

    label("loc_233")

    Jump("loc_236")

    label("loc_236")

    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_1E6 end

    def Function_1_248(): pass

    label("Function_1_248")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDDD20, 0x30050)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_266")

    label("loc_266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_273")
    OP_A3(0x3FA)
    Jump("loc_278")

    label("loc_273")

    OP_71(0xA, 0x4)

    label("loc_278")

    OP_B0(0x0, 0x78)
    OP_1C(0x0, 0x0, 0x8)
    OP_22(0x1C5, 0x1, 0x64)
    Return()

    # Function_1_248 end

    def Function_2_287(): pass

    label("Function_2_287")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_287")

    label("loc_29C")

    Return()

    # Function_2_287 end

    def Function_3_29D(): pass

    label("Function_3_29D")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(3700, 2600, -22200, 0)
    OP_6B(4000, 0)
    OP_6C(333000, 0)
    SetChrPos(0x8, 2780, 2600, -22200, 0)
    SetChrPos(0x101, 3920, -540, -27770, 0)
    SetChrPos(0x102, 2820, -530, -28580, 0)
    SetChrPos(0x105, 3690, -460, -29430, 0)
    SetChrPos(0x106, 4740, -440, -28690, 0)
    StopSound(0x7D00, 0x27100, 0x0)

    def lambda_32F():
        OP_6D(0, 8800, 6500, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_32F)

    def lambda_347():
        OP_6C(57000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_347)

    def lambda_357():
        OP_67(0, 11290, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_357)

    def lambda_36F():
        OP_6B(10000, 5000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_36F)
    FadeToBright(2000, 0)
    StopSound(0x7D00, 0x57E40, 0x1388)
    ClearChrFlags(0x8, 0x80)
    OP_8E(0x8, 0x253A, 0x2EE0, 0x1018, 0x36B0, 0x0)
    OP_43(0x8, 0x1, 0x0, 0x4)
    OP_97(0x8, 0x0, 0x1964, 0xFFF6D840, 0x36B0, 0x1)
    OP_44(0x8, 0xFF)
    Fade(1000)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    SetChrFlags(0x8, 0x80)
    OP_6D(3940, -520, -28440, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #0
        0x101,
        "#002FJust as I thought...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x106,
        (
            "#057FThe Varenne Lighthouse...\x01",
            "It belongs to the city of Ruan.\x02\x03",

            "If I remember right, there's a\x01",
            "man who lives here all alone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x105,
        (
            "#042FThis appears to be the place.\x02\x03",

            "I'm almost positive that the ones who\x01",
            "attacked Matron Theresa and the children are\x01",
            "here in this building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        (
            "#012FWhich means that there's a high\x01",
            "chance the perpetrators have\x01",
            "taken over the lighthouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#002FAnd from the looks of it...that\x01",
            "seems to be the only entrance.\x02\x03",

            "I guess that all there is left to do\x01",
            "is to check it out for ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x105,
        "#042FYes...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x105, 400)

    ChrTalk(    #6
        0x106,
        (
            "#052F#4PNow hold on there a minute,\x01",
            "girl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x105,
        (
            "#049FI want to see the truth with my\x01",
            "own eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x106,
        (
            "#055F#4PWhat the hell are you talking\x01",
            "about?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x106, 400)

    ChrTalk(    #9
        0x105,
        (
            "#043FI want to know why someone would do\x01",
            "such a horrible thing like that...\x02\x03",

            "#043FSo please...take me with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x106,
        (
            "#055F#4PI can see where you're coming\x01",
            "from, but...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7AA():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7AA)

    def lambda_7B8():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7B8)
    Sleep(400)

    ChrTalk(    #11
        0x101,
        (
            "#006F#3POh, come on!\x01",
            "Don't act all stingy now!\x02\x03",

            "#006FThe only reason we knew about this\x01",
            "place to begin with was because of\x01",
            "Kloe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        (
            "#010F#3PAnd I can guarantee she can\x01",
            "handle herself.\x02\x03",

            "So, at least, you don't have to\x01",
            "worry about her getting in the\x01",
            "way.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #13
        0x105,
        "#048FEstelle, Joshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x106,
        (
            "#053F#4PFine...\x01",
            "Have your way.\x02\x03",

            "#057FBut I hope you remember that\x01",
            "these guys are the ones who\x01",
            "put Carna out of commission.\x02\x03",

            "Make sure you don't let down\x01",
            "your guard.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x106, 400)

    ChrTalk(    #15
        0x105,
        "#040FI'll keep that in mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#006F#3PWell, I guess it's decided then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        (
            "#012F#3PAll right... Let's hurry and check\x01",
            "the place out.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x3E, 0x1, 0x20)
    EventEnd(0x0)
    Return()

    # Function_3_29D end

    def Function_4_A36(): pass

    label("Function_4_A36")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A4E")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_4_A36")

    label("loc_A4E")

    Return()

    # Function_4_A36 end

    def Function_5_A4F(): pass

    label("Function_5_A4F")

    OP_72(0xA, 0x4)
    EventBegin(0x0)
    OP_6D(130, 21350, 6270, 0)
    OP_6C(270000, 0)
    OP_6B(3770, 0)
    OP_72(0x2, 0x8)
    SetChrChipByIndex(0x9, 4)
    SetChrChipByIndex(0xA, 4)
    SetChrChipByIndex(0x106, 5)
    SetChrPos(0x9, 5080, 25000, 6100, 0)
    SetChrPos(0xA, 5080, 25000, 6100, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x106, 0x80)
    SetChrPos(0x101, 5080, 25000, 6100, 0)
    SetChrPos(0x102, 5080, 25000, 6100, 0)
    SetChrPos(0x105, 5080, 25000, 6100, 0)
    SetChrPos(0x106, 5080, 25000, 6100, 0)
    OP_6F(0x1, 40)
    OP_70(0x1, 0x50)

    def lambda_B1B():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B1B)

    def lambda_B2B():
        OP_6D(-2320, 25000, -1320, 6000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_B2B)
    SetChrPos(0x9, 5080, 25000, 6100, 0)
    SetChrPos(0xA, 5080, 25000, 6100, 0)
    OP_43(0x9, 0x1, 0x0, 0x6)
    Sleep(1000)
    OP_43(0xA, 0x1, 0x0, 0x6)
    Sleep(2500)
    OP_43(0x106, 0x1, 0x0, 0x7)
    Sleep(300)
    OP_43(0x101, 0x1, 0x0, 0x6)
    Sleep(300)
    OP_43(0x102, 0x1, 0x0, 0x6)
    Sleep(300)
    OP_43(0x105, 0x1, 0x0, 0x6)
    Sleep(1750)
    OP_4A(0x106, 1)
    OP_51(0x106, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x106, 5)
    SetChrSubChip(0x106, 0)
    Sleep(50)
    OP_44(0x101, 0xFF)
    OP_51(0x101, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    Sleep(50)
    OP_44(0x102, 0xFF)
    OP_51(0x102, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    Sleep(50)
    OP_44(0x105, 0xFF)
    OP_51(0x105, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    Fade(1000)
    OP_6D(-240, 25000, -1010, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    OP_0D()

    ChrTalk(    #18
        0x102,
        "#014FA rope?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#005FThese guys were seriously\x01",
            "prepared for anything!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x106,
        (
            "#057F...\x02\x03",

            "I'm leaving you to take care of\x01",
            "that idiot steward and the rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#004FWhat...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 800)

    ChrTalk(    #22
        0x106,
        (
            "#054FI'm going after these guys!\x02\x03",

            "The rest of you report to Jean and\x01",
            "ask him for further instructions!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x106, 270, 800)
    OP_4B(0x106, 1)

    ChrTalk(    #23
        0x105,
        "#044FAh...!\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[All right, me too!]\x01",               # 0
            "[D-Did you just see that...?]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E26"),
        (1, "loc_EFE"),
        (SWITCH_DEFAULT, "loc_FD6"),
    )


    label("loc_E26")


    ChrTalk(    #24
        0x101,
        "#005FAll right, me too!\x02",
    )

    CloseMessageWindow()

    def lambda_E49():
        OP_8E(0xFE, 0xFFFFF768, 0x61A8, 0xFFFFFBB4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E49)
    Sleep(260)
    OP_44(0x101, 0xFF)
    SetChrSubChip(0x101, 6)

    ChrTalk(    #25
        0x102,
        (
            "#012FHold on, Estelle. Didn't you just\x01",
            "hear what Agate said?\x02\x03",

            "#012FWe can't just forget about Gilbert\x01",
            "and those guys from the Raven Gang.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FD6")

    label("loc_EFE")


    ChrTalk(    #26
        0x101,
        (
            "#004FD-Did you just see that...?\x02\x03",

            "#004FShouldn't we go after those\x01",
            "guys too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        (
            "#012FNo... Didn't you just hear what\x01",
            "Agate said?\x02\x03",

            "#012FWe can't just forget about Gilbert\x01",
            "and those guys from the Raven Gang.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FD6")

    label("loc_FD6")


    ChrTalk(    #28
        0x105,
        (
            "#043FThat's right...\x02\x03",

            "And though I think Gilbert got what\x01",
            "was coming to him, he is still hurt.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x101, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #29
        0x101,
        (
            "#002FOh, all right...\x02\x03",

            "#007FI hate to say this, but I guess we'll\x01",
            "have to leave the rest up to Agate.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(2000, 0, -1)
    OP_24(0x1C5, 0x5F)
    Sleep(200)
    OP_24(0x1C5, 0x5A)
    Sleep(200)
    OP_24(0x1C5, 0x55)
    Sleep(200)
    OP_24(0x1C5, 0x50)
    Sleep(200)
    OP_24(0x1C5, 0x4B)
    Sleep(200)
    OP_24(0x1C5, 0x46)
    Sleep(200)
    OP_24(0x1C5, 0x41)
    Sleep(200)
    OP_23(0x1C5)
    OP_0D()
    OP_21()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #30
        (
            "\x07\x05Thus, in the end, Estelle and the others were able to take back the stolen\x01",
            "money without incident.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #31
        (
            "\x07\x05By the time the mayor's steward and the group of delinquents were safely\x01",
            "locked up in the Manoria windmill shed, morning had already broken...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    ClearMapFlags(0x40000000)
    OP_28(0x3E, 0x1, 0x80)
    OP_28(0x3E, 0x1, 0x100)
    Sleep(1000)
    SetMapFlags(0x100000)
    OP_22(0xD, 0x0, 0x64)
    Sleep(2500)
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T2300   ._SN", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_A4F end

    def Function_6_124C(): pass

    label("Function_6_124C")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x1C70, 0x61A8, 0x16B2, 0x1770, 0x0)
    OP_8E(0xFE, 0x1BC6, 0x61A8, 0x97E, 0x1770, 0x0)
    OP_8E(0xFE, 0xED8, 0x61A8, 0xFFFFFBB4, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFF894, 0x61A8, 0xFFFFFBB4, 0x1770, 0x0)
    OP_96(0xFE, 0xFFFFF484, 0x6590, 0xFFFFF8E4, 0x3E8, 0x1770)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 1)
    SetChrFlags(0xFE, 0x20)
    OP_8F(0xFE, 0xFFFFF1E6, 0x61A8, 0xFFFFF7CC, 0xFA0, 0x0)
    OP_8F(0xFE, 0xFFFFF1E6, 0x5DC0, 0xFFFFF7CC, 0x1770, 0x0)
    OP_8F(0xFE, 0xFFFFF1E6, 0x59D8, 0xFFFFF7CC, 0x1F40, 0x0)
    OP_8F(0xFE, 0xFFFFF1E6, 0x5208, 0xFFFFF7CC, 0x2710, 0x0)
    OP_8F(0xFE, 0xFFFFF1E6, 0x1388, 0xFFFFF7CC, 0x32C8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_6_124C end

    def Function_7_133D(): pass

    label("Function_7_133D")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x1C70, 0x61A8, 0x16B2, 0x1770, 0x0)
    OP_8E(0xFE, 0x1BC6, 0x61A8, 0x97E, 0x1770, 0x0)
    OP_8E(0xFE, 0xED8, 0x61A8, 0xFFFFFBB4, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFF894, 0x61A8, 0xFFFFFBB4, 0x1770, 0x0)
    OP_96(0xFE, 0xFFFFF484, 0x6590, 0xFFFFF8E4, 0x3E8, 0x1770)
    OP_8C(0xFE, 45, 400)
    SetChrFlags(0xFE, 0x20)
    OP_8F(0xFE, 0xFFFFF1E6, 0x61A8, 0xFFFFF7CC, 0xFA0, 0x0)
    OP_8F(0xFE, 0xFFFFF1E6, 0x5DC0, 0xFFFFF7CC, 0x1770, 0x0)
    OP_8F(0xFE, 0xFFFFF1E6, 0x59D8, 0xFFFFF7CC, 0x1F40, 0x0)
    OP_8F(0xFE, 0xFFFFF1E6, 0x5208, 0xFFFFF7CC, 0x2710, 0x0)
    OP_8F(0xFE, 0xFFFFF1E6, 0x1388, 0xFFFFF7CC, 0x32C8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_7_133D end

    def Function_8_1429(): pass

    label("Function_8_1429")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_8_1429 end

    SaveToFile()

Try(main)
