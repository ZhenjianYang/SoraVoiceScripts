from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2400   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2400.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        'Matron Theresa',                       # 9
        'Daniel',                               # 10
        'Mary',                                 # 11
        'Clem',                                 # 12
        'Sieg',                                 # 13
        'Targeting Camera',                     # 14
        'Chicken',                              # 15
        'Chicken',                              # 16
        'Chicken',                              # 17
        'Gull Seaside Way',                     # 18
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
        'ED6_DT07/CH02590 ._CH',             # 00
        'ED6_DT07/CH02640 ._CH',             # 01
        'ED6_DT07/CH02630 ._CH',             # 02
        'ED6_DT07/CH02570 ._CH',             # 03
        'ED6_DT07/CH02320 ._CH',             # 04
        'ED6_DT06/CH20051 ._CH',             # 05
        'ED6_DT07/CH00040 ._CH',             # 06
        'ED6_DT07/CH00041 ._CH',             # 07
        'ED6_DT07/CH01720 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH02590P._CP',             # 00
        'ED6_DT07/CH02640P._CP',             # 01
        'ED6_DT07/CH02630P._CP',             # 02
        'ED6_DT07/CH02570P._CP',             # 03
        'ED6_DT07/CH02320P._CP',             # 04
        'ED6_DT06/CH20051P._CP',             # 05
        'ED6_DT07/CH00040P._CP',             # 06
        'ED6_DT07/CH00041P._CP',             # 07
        'ED6_DT07/CH01720P._CP',             # 08
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 33500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 6000,
        Z                   = 200,
        Y                   = 22200,
        Direction           = 180,
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
        X                   = 5800,
        Z                   = 0,
        Y                   = 23600,
        Direction           = 180,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 22900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 800,
        Z                   = 6000,
        Y                   = -13810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 1060,
        Z                   = 0,
        Y                   = -23220,
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


    DeclEvent(
        X                   = -1880,
        Y                   = 2000,
        Z                   = 4450,
        Range               = 2800,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0x14B4,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    ScpFunction(
        "Function_0_252",          # 00, 0
        "Function_1_2D9",          # 01, 1
        "Function_2_2EC",          # 02, 2
        "Function_3_302",          # 03, 3
        "Function_4_455",          # 04, 4
        "Function_5_4E1",          # 05, 5
        "Function_6_507",          # 06, 6
        "Function_7_1CE5",         # 07, 7
        "Function_8_1D32",         # 08, 8
        "Function_9_1DE6",         # 09, 9
        "Function_10_1E92",        # 0A, 10
        "Function_11_2882",        # 0B, 11
        "Function_12_28AD",        # 0C, 12
        "Function_13_28F1",        # 0D, 13
        "Function_14_2968",        # 0E, 14
        "Function_15_29DD",        # 0F, 15
    )


    def Function_0_252(): pass

    label("Function_0_252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_25C")
    Jump("loc_28B")

    label("loc_25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_266")
    Jump("loc_28B")

    label("loc_266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 0)), scpexpr(EXPR_END)), "loc_270")
    Jump("loc_28B")

    label("loc_270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_27A")
    Jump("loc_28B")

    label("loc_27A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_284")
    Jump("loc_28B")

    label("loc_284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_28B")

    label("loc_28B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_299")
    OP_A3(0x3FA)
    Event(0, 10)

    label("loc_299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_2B0")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 14)

    label("loc_2B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_2C7")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FC)
    Event(0, 15)

    label("loc_2C7")

    OP_51(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_252 end

    def Function_1_2D9(): pass

    label("Function_1_2D9")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE5A20, 0x30067)
    Return()

    # Function_1_2D9 end

    def Function_2_2EC(): pass

    label("Function_2_2EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_301")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2EC")

    label("loc_301")

    Return()

    # Function_2_2EC end

    def Function_3_302(): pass

    label("Function_3_302")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)
    OP_8D(0xFE, -8760, 13210, 8700, 24630, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_330")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_454")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_419")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2238), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_PUSH_LONG, 0x339A), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x21FC), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x6036), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EE")
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x0, 0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_3DB():
        OP_94(0x0, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DB)
    Jump("loc_411")

    label("loc_3EE")


    def lambda_3F4():
        OP_8D(0xFE, -8760, 13210, 8700, 24630, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F4)
    Sleep(200)

    label("loc_411")

    Sleep(30)
    Jump("loc_451")

    label("loc_419")

    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_451")
    OP_44(0xFE, 0x2)

    def lambda_439():
        OP_8D(0xFE, -8760, 13210, 8700, 24630, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_439)

    label("loc_451")

    Jump("loc_330")

    label("loc_454")

    Return()

    # Function_3_302 end

    def Function_4_455(): pass

    label("Function_4_455")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E0")
    OP_43(0xFE, 0x2, 0x0, 0x5)
    OP_22(0x191, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x38B, 1)"), scpexpr(EXPR_END)), "loc_4E0")
    TalkBegin(0xFE)
    OP_A2(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x07\x00Found \x07\x02Fresh Eggs\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFE)

    label("loc_4E0")

    Return()

    # Function_4_455 end

    def Function_5_4E1(): pass

    label("Function_5_4E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4FC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_5_4E1")

    label("loc_4FC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_4E1 end

    def Function_6_507(): pass

    label("Function_6_507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE4")
    OP_A2(0x410)
    EventBegin(0x0)
    TurnDirection(0xB, 0x9, 0)
    TurnDirection(0x9, 0xB, 0)
    TurnDirection(0xA, 0xB, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_563")
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_57A")

    label("loc_563")

    OP_62(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    label("loc_57A")


    def lambda_580():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_580)
    OP_6D(5200, 0, 22840, 2000)
    AddParty(0x35, 0xFF)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x136, 0x1)
    SetChrPos(0x101, -690, 0, 17260, 45)
    SetChrPos(0x102, -130, 0, 16010, 45)
    SetChrPos(0x136, 0, 0, 31800, 90)
    SetChrFlags(0x136, 0x80)

    ChrTalk(    #1
        0xA,
        (
            "I swear...\x01",
            "Clem, where did you go?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xA,
        (
            "Miss Kloe is gonna be worried\x01",
            "about you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xB,
        (
            "#770FHa ha... No she won't.\x02\x03",

            "Not after I show her the awesome\x01",
            "thing I got.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        "What'd ya get, Clem?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xB,
        (
            "#771FHa ha... Now don't freak out or\x01",
            "anything.\x02\x03",

            "I just borrowed it from some crazy\x01",
            "lady I ran into.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "...Who are you calling crazy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xB,
        "#774FWha...\x02",
    )

    CloseMessageWindow()

    def lambda_749():

        label("loc_749")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_749")

    QueueWorkItem2(0x101, 2, lambda_749)

    def lambda_75A():

        label("loc_75A")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_75A")

    QueueWorkItem2(0x102, 2, lambda_75A)

    def lambda_76B():

        label("loc_76B")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_76B")

    QueueWorkItem2(0xB, 1, lambda_76B)

    def lambda_77C():

        label("loc_77C")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_77C")

    QueueWorkItem2(0x9, 1, lambda_77C)

    def lambda_78D():

        label("loc_78D")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_78D")

    QueueWorkItem2(0xA, 1, lambda_78D)

    def lambda_79E():
        OP_8E(0xFE, 0x654, 0x0, 0x56E0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_79E)

    def lambda_7B9():
        OP_8E(0xFE, 0x618, 0x0, 0x5276, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7B9)
    TurnDirection(0xB, 0x101, 400)
    OP_6D(3750, 0, 22850, 1000)
    WaitChrThread(0x101, 0x1)
    OP_95(0xB, 0x0, 0x0, 0x0, 0x3E8, 0x2710)
    OP_62(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0xB, 0xB4, 0x1F4, 0xBB8, 0x0)

    ChrTalk(    #8
        0xB,
        "#774FAck! What are you doing here?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#006FHmph... I'm a bracer.\x01",
            "Give me a little credit.\x02\x03",

            "Wherever a delinquent like you goes,\x01",
            "we'll figure it out in no time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xB,
        (
            "#772FDamn it! Well, you're not catching\x01",
            "me!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xB, 0x15F4, 0x64, 0x52F8, 0x1B58, 0x0)
    OP_8E(0xB, 0x2468, 0xC8, 0x529E, 0x1B58, 0x0)
    OP_8E(0xB, 0x21CA, 0xFFFFFF38, 0x4AA6, 0x1B58, 0x0)

    ChrTalk(    #11
        0x101,
        "#005FHey! Get back here!\x02",
    )

    CloseMessageWindow()

    def lambda_96E():
        OP_6D(5748, -175, 18851, 1000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_96E)

    def lambda_986():
        OP_8E(0xFE, 0x166C, 0x0, 0x50B4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_986)

    def lambda_9A1():
        OP_96(0xFE, 0x18EC, 0xFFFFFF38, 0x42A4, 0x5DC, 0x1B58)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9A1)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xB, 0x1)
    OP_8E(0x102, 0x10CC, 0xC8, 0x5974, 0xBB8, 0x0)
    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xD, 0x3E8)
    OP_6A(0xD)
    OP_43(0x101, 0x1, 0x0, 0x9)
    OP_43(0xB, 0x1, 0x0, 0x8)
    OP_43(0x102, 0x1, 0x0, 0x7)
    WaitChrThread(0x102, 0x1)
    Sleep(1800)
    Fade(1000)
    OP_44(0xA, 0xFF)
    OP_44(0x9, 0xFF)
    TurnDirection(0x9, 0x102, 0)
    TurnDirection(0xA, 0x102, 0)
    OP_6A(0x0)
    ClearMapFlags(0x1)
    OP_6D(4800, 185, 22555, 0)
    OP_0D()

    ChrTalk(    #12
        0xA,
        "Hey, mister...what's going on?\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x40)
    SetChrPos(0x101, -4998, 0, 29194, 0)
    SetChrPos(0xB, -1998, 0, 29194, 0)

    def lambda_AC5():
        OP_8E(0xFE, 0x2818, 0x0, 0x7D00, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_AC5)

    def lambda_AE0():
        OP_8E(0xFE, 0x256C, 0x0, 0x7C06, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AE0)

    ChrTalk(    #13
        0x9,
        (
            "Did Clem do something bad\x01",
            "again?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)

    ChrTalk(    #14
        0x102,
        "#019FUmm... Sorry to barge in like this.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0xFF)
    OP_44(0xB, 0xFF)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, 8300, 200, 31590, 90)
    SetChrPos(0x101, 7700, 0, 31590, 90)

    def lambda_B8F():

        label("loc_B8F")

        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        OP_48()
        Jump("loc_B8F")

    QueueWorkItem2(0xB, 1, lambda_B8F)

    ChrTalk(    #15
        0xB,
        "#776F#4PDammit! Let go! Lemme go!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)

    def lambda_BD3():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_BD3)

    def lambda_BE1():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BE1)

    def lambda_BEF():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BEF)
    OP_6D(8880, 0, 32490, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2640, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #16
        0xB,
        "#776F#2PI'll sue you for child abuse!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#009F#1PYou're a real brat, you know that?\x02\x03",

            "Now give me back my emblem!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xB,
        "#776F#2PYou got no proof I took it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#006F#1PWell, you're right on that one...\x01",
            "but that's nothing a quick search\x01",
            "won't fix!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D4A():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D4A)
    OP_97(0xB, 0x1E5A, 0x7B66, 0x2BF20, 0xFA0, 0x3)
    OP_44(0xB, 0xFF)
    SetChrSubChip(0xB, 0)
    OP_9E(0xB, 0x1E, 0x0, 0x190, 0x1388)

    ChrTalk(    #20
        0xB,
        (
            "#778F#1PYaaa ha ha ha...!\x02\x03",

            "Hey! Cut it out! That tickles!\x02\x03",

            "Pervert! Abuse!\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0xB, 0x1E, 0x0, 0x258, 0x1388)

    ChrTalk(    #21
        0x101,
        (
            "#006F#2PCome on, just give it up and hand\x01",
            "over what you took.\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x0, 0x10)
    OP_6F(0x0, 20)
    SetChrPos(0x136, 10, 0, 30720, 90)
    ClearChrFlags(0x136, 0x80)

    NpcTalk(    #22
        0x136,
        "Girl's Voice",
        "#2PSieg!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(9390, 0, 34800, 800)
    Sleep(500)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x40)
    SetChrPos(0xC, 0, 6000, 31900, 0)
    OP_22(0x8C, 0x0, 0x64)
    OP_8E(0xC, 0x1E14, 0x2BC, 0x7B66, 0x4E20, 0x0)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_EDF():
        OP_95(0xFE, 0x12C, 0x0, 0x0, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EDF)

    def lambda_EFD():
        OP_95(0xFE, 0x12C, 0x0, 0x0, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_EFD)
    OP_8E(0xC, 0x36A6, 0x1770, 0x8278, 0x4E20, 0x0)

    ChrTalk(    #23
        0x101,
        (
            "#004F#2PWha--?!\x02\x03",

            "What the hell was that?!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F5E():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_F5E)

    def lambda_F6C():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F6C)

    def lambda_F7A():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F7A)

    def lambda_F88():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F88)

    def lambda_F96():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F96)

    def lambda_FA4():
        OP_6D(3420, 0, 32210, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_FA4)

    def lambda_FBC():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_FBC)

    def lambda_FCC():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_FCC)
    WaitChrThread(0x0, 0x2)
    OP_92(0xC, 0x136, 0x1388, 0x2710, 0x0)
    OP_92(0xC, 0x136, 0xFA0, 0x1F40, 0x0)
    OP_92(0xC, 0x136, 0xBB8, 0x1770, 0x0)
    OP_92(0xC, 0x136, 0x7D0, 0xBB8, 0x0)
    OP_8E(0xC, 0xA, 0x3E8, 0x7B0C, 0x5DC, 0x0)

    def lambda_102D():
        OP_8C(0xFE, 135, 200)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_102D)
    SetChrChipByIndex(0x136, 5)
    SetChrSubChip(0x136, 3)
    OP_8F(0xC, 0xFFFFFFCE, 0xC8, 0x7ADA, 0x3E8, 0x0)
    WaitChrThread(0xC, 0x3)
    Sleep(100)
    Fade(250)
    SetChrFlags(0xC, 0x80)
    SetChrSubChip(0x136, 1)
    SetChrFlags(0x136, 0x20)
    OP_0D()
    Sleep(500)

    NpcTalk(    #24
        0x136,
        "Girl in Uniform",
        (
            "#046FGet away from the boy!\x02\x03",

            "Lay another hand on him and you'll\x01",
            "have me to con...\x02\x03",

            "#044F...Huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#004FHey, you're that...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #26
        0x136,
        "Girl in Uniform",
        "#044FI remember you from Manoria...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #27
        0xC,
        "Gyrfalcon",
        "#310F#3PScree?\x02",
    )

    CloseMessageWindow()
    OP_96(0xB, 0x1A40, 0x0, 0x7B0C, 0x1F4, 0x1388)
    ClearChrFlags(0xB, 0x4)
    OP_8E(0xB, 0x15EA, 0x0, 0x7BD4, 0x1B58, 0x0)

    ChrTalk(    #28
        0xB,
        (
            "#775FHelp me, Miss Kloe!\x02\x03",

            "I didn't do anything and she's\x01",
            "being mean to me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#005F'Didn't do anything,' my butt!\x01",
            "You stole my emblem!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #30
        0xB,
        "#770F#1PHeh! So where's your proof?\x02",
    )

    CloseMessageWindow()

    def lambda_1255():
        OP_8E(0xFE, 0x17B6, 0x0, 0x7C9C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1255)
    Sleep(200)
    OP_8F(0xB, 0x1194, 0x0, 0x78D2, 0x1388, 0x0)
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #31
        0xB,
        "#774F#1PAnd no tickling, this time!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        "#009FGrrrrrr...\x02",
    )

    CloseMessageWindow()

    def lambda_12CE():
        OP_6D(2050, 0, 30810, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12CE)

    def lambda_12E6():
        OP_8E(0xFE, 0xADC, 0x0, 0x6EC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12E6)
    Sleep(300)

    def lambda_1306():
        OP_8E(0xFE, 0x1040, 0x0, 0x6F7C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1306)
    Sleep(400)

    def lambda_1326():
        OP_8E(0xFE, 0x384, 0x0, 0x71D4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1326)
    Sleep(300)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x136, 0)

    ChrTalk(    #33
        0x102,
        "#010FHey, we meet again.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x136, 135, 400)

    ChrTalk(    #34
        0x136,
        (
            "#045FOh, hello...\x02\x03",

            "I'm sorry... I thought for sure\x01",
            "that a thief had broken in... \x02\x03",

            "#043FI...assume there's a reason for\x01",
            "all this?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0x1)

    ChrTalk(    #35
        0xA,
        "There sure is, Miss Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xA,
        "Clem was being bad again.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #37
        0x9,
        "Hey, is the apple pie ready yet...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x136,
        (
            "#041FYou'll have to wait a little longer.\x01",
            "It still needs time to bake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#005FYou friggin' brat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xB,
        "#776F#1PChild abuser!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xA,
        (
            "When are you gonna grow up,\x01",
            "Clem?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        "Is the pie done yet...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x136, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #43
        0x102,
        "#019FThis has gotten out of hand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x136,
        (
            "#045FOh... Ha ha...\x01",
            "Yes, I suppose it has.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #45
        0xC,
        "Gyrfalcon",
        "#311F#4PScree.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #46
        0x8,
        "Woman's Voice",
        "#3PMy... What's all the noise?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x4)
    OP_8E(0x8, 0x0, 0x0, 0x7C38, 0x5DC, 0x0)
    OP_8C(0x8, 90, 400)

    def lambda_1636():

        label("loc_1636")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1636")

    QueueWorkItem2(0xB, 1, lambda_1636)

    def lambda_1647():

        label("loc_1647")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1647")

    QueueWorkItem2(0x9, 1, lambda_1647)

    def lambda_1658():

        label("loc_1658")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1658")

    QueueWorkItem2(0xA, 1, lambda_1658)

    def lambda_1669():

        label("loc_1669")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1669")

    QueueWorkItem2(0x101, 1, lambda_1669)

    def lambda_167A():

        label("loc_167A")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_167A")

    QueueWorkItem2(0x102, 1, lambda_167A)

    def lambda_168B():

        label("loc_168B")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_168B")

    QueueWorkItem2(0x136, 1, lambda_168B)

    ChrTalk(    #47
        0x136,
        "#044FMatron Theresa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#750F#3PI don't know the full story...\x02\x03",

            "...but it sounds like Clem's\x01",
            "been up to no good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xB,
        (
            "#772FHey, no fair! I didn't do anything!\x02\x03",

            "The pervert lady just says I did!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#009FWho you callin' a pervert?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        "#750F#3POh, dear... This won't do.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xA14, 0x0, 0x771A, 0x7D0, 0x0)
    OP_8C(0x8, 90, 400)

    ChrTalk(    #52
        0x8,
        (
            "#750F#3PClem...did you really not do\x01",
            "anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xB,
        "#771FOf course not!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        "#750F#3PDo you swear to Aidios?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xB,
        "#775FI... I swear!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "#754F#3PI see...\x02\x03",

            "#750FIt's just that you dropped some kind\x01",
            "of badge in the nursery earlier...\x02\x03",

            "That wasn't yours, was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xB,
        "#772FB-But it was in my pants pocket...\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #58
        0xB,
        "#774FErr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        "#005FI TOLD you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x136,
        "#044FOh, my...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x102,
        "#010FNicely done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "#752F#3PClem... No more excuses.\x02\x03",

            "Give her back what you stole.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #63
        0xB,
        "#773F...\x02",
    )

    CloseMessageWindow()
    OP_44(0xB, 0x1)
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #64
        0xB,
        (
            "#776F#1PAll right, all right! I'll give\x01",
            "it back, so just drop it!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0x136, 0x1)

    def lambda_1A48():

        label("loc_1A48")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_1A48")

    QueueWorkItem2(0x101, 1, lambda_1A48)

    def lambda_1A59():

        label("loc_1A59")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_1A59")

    QueueWorkItem2(0x8, 1, lambda_1A59)

    def lambda_1A6A():

        label("loc_1A6A")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_1A6A")

    QueueWorkItem2(0x102, 1, lambda_1A6A)

    def lambda_1A7B():

        label("loc_1A7B")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_1A7B")

    QueueWorkItem2(0xA, 1, lambda_1A7B)

    def lambda_1A8C():

        label("loc_1A8C")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_1A8C")

    QueueWorkItem2(0x9, 1, lambda_1A8C)

    def lambda_1A9D():

        label("loc_1A9D")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_1A9D")

    QueueWorkItem2(0x136, 1, lambda_1A9D)
    OP_92(0xB, 0x101, 0x4B0, 0xFA0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #65
        "\x07\x05Clem tossed the emblem over to Estelle.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x35C, 1)
    OP_8F(0xB, 0x1194, 0x0, 0x78D2, 0xFA0, 0x0)

    ChrTalk(    #66
        0x101,
        "#004FWhoa...\x02",
    )

    CloseMessageWindow()
    OP_95(0xB, 0x0, 0x0, 0x0, 0x320, 0x1770)

    ChrTalk(    #67
        0xB,
        "#772F#1PHeh! I'm out of here!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 400)
    OP_8E(0xB, 0x1405, 0x0, 0x709E, 0x1770, 0x0)
    OP_8E(0xB, 0x1107, 0x0, 0x50A0, 0x1B58, 0x0)

    ChrTalk(    #68
        0x136,
        "#043FClem!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#750F#6PIt's all right. He'll be back when\x01",
            "he starts getting cold.\x02\x03",

            "#750FMore to the point... Why is\x01",
            "everyone standing around?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 400)
    Sleep(400)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x136, 0xFF)
    OP_44(0xA, 0x1)
    OP_44(0x9, 0x1)

    def lambda_1C5E():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C5E)

    def lambda_1C6C():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C6C)

    def lambda_1C7A():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_1C7A)
    Sleep(400)

    ChrTalk(    #70
        0x8,
        (
            "#750F#6PWhy don't you tell me the whole\x01",
            "story over a cup of tea?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2410   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1CE4")

    Return()

    # Function_6_507 end

    def Function_7_1CE5(): pass

    label("Function_7_1CE5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D31")
    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_7_1CE5")

    label("loc_1D31")

    Return()

    # Function_7_1CE5 end

    def Function_8_1D32(): pass

    label("Function_8_1D32")

    OP_8E(0xFE, 0xE9C, 0xFFFFFF38, 0x425E, 0x1B58, 0x0)
    OP_96(0xFE, 0x3F2, 0xC8, 0x425E, 0x7D0, 0x1B58)
    OP_8E(0xFE, 0xFFFFF7F4, 0x64, 0x3764, 0x1B58, 0x0)
    OP_8E(0xFE, 0xFFFFEE6C, 0xFFFFFF38, 0x3912, 0x1B58, 0x0)

    def lambda_1D8B():

        label("loc_1D8B")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1D8B")

    QueueWorkItem2(0xFE, 2, lambda_1D8B)
    Sleep(1600)
    OP_8F(0xFE, 0xFFFFEDC2, 0xFFFFFF9C, 0x4880, 0x1B58, 0x0)
    Sleep(1200)
    OP_8F(0xFE, 0xFFFFED54, 0xFFFFFF38, 0x4F2E, 0x1B58, 0x0)
    Sleep(500)
    OP_44(0xFE, 0x2)
    OP_8E(0xFE, 0xFFFFEC6E, 0x0, 0x7C06, 0x2AF8, 0x0)
    Return()

    # Function_8_1D32 end

    def Function_9_1DE6(): pass

    label("Function_9_1DE6")

    Sleep(500)
    OP_8E(0xFE, 0x4D8, 0x0, 0x532A, 0x1B58, 0x0)
    OP_8E(0xFE, 0xFFFFF984, 0xC8, 0x4B28, 0x1B58, 0x0)
    OP_96(0xFE, 0xFFFFF38A, 0xFFFFFF38, 0x4902, 0x7D0, 0x1B58)
    Sleep(1000)
    OP_8F(0xFE, 0xFFFFF3D0, 0xFFFFFF9C, 0x3796, 0x1B58, 0x0)
    Sleep(1000)
    OP_8F(0xFE, 0xFFFFF3D0, 0xFFFFFF9C, 0x3796, 0x1B58, 0x0)
    OP_8F(0xFE, 0xFFFFEE6C, 0xFFFFFF38, 0x3912, 0x1B58, 0x0)
    Sleep(500)
    OP_44(0x102, 0xFF)
    OP_44(0xFE, 0x2)
    OP_8E(0xFE, 0xFFFFEC6E, 0x0, 0x7C06, 0x2AF8, 0x0)
    Return()

    # Function_9_1DE6 end

    def Function_10_1E92(): pass

    label("Function_10_1E92")

    EventBegin(0x0)
    OP_6D(-1130, 80, 31130, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x136, 0x80)
    SetChrPos(0x101, 0, 0, 32900, 0)
    SetChrPos(0x102, 0, 0, 32900, 0)
    SetChrPos(0x136, 0, 0, 32900, 0)
    SetChrFlags(0x8, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_70(0x0, 0x14)
    OP_73(0x0)
    OP_43(0x101, 0x1, 0x0, 0xB)
    OP_43(0x102, 0x1, 0x0, 0xC)
    OP_43(0x136, 0x1, 0x0, 0xD)
    WaitChrThread(0x136, 0x1)

    ChrTalk(    #71
        0x101,
        "#000FMatron Theresa sure is a nice lady.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x102,
        "#010FYes. She's very motherly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x136,
        (
            "#041F#2PHa ha... I'm sure all the children\x01",
            "here think of her as their mother. \x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x197, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x136, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -5000, 8000, 13000, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    def lambda_2050():

        label("loc_2050")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_2050")

    QueueWorkItem2(0x101, 1, lambda_2050)

    def lambda_2061():

        label("loc_2061")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_2061")

    QueueWorkItem2(0x102, 1, lambda_2061)
    OP_8C(0x136, 180, 0)
    OP_92(0xC, 0x136, 0x1388, 0x2710, 0x0)
    OP_22(0x8C, 0x0, 0x64)
    OP_92(0xC, 0x136, 0xFA0, 0x1F40, 0x0)
    OP_92(0xC, 0x136, 0xBB8, 0x1770, 0x0)
    OP_92(0xC, 0x136, 0x7D0, 0xBB8, 0x0)
    OP_8E(0xC, 0xFFFFFD8A, 0x3E8, 0x765C, 0x5DC, 0x0)

    def lambda_20CA():
        OP_8C(0xFE, 90, 200)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_20CA)
    SetChrChipByIndex(0x136, 5)
    SetChrSubChip(0x136, 2)
    OP_8C(0x136, 135, 0)
    OP_8F(0xC, 0xFFFFFEB6, 0xC8, 0x7788, 0x3E8, 0x0)
    Fade(250)
    SetChrSubChip(0x136, 0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x136, 0x20)
    OP_0D()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(    #74
        0x136,
        "#040F#2POh, Sieg. Were you waiting for me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xC,
        "#310F#1PScree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x136,
        (
            "#040F#2PThat's right. They're not here to\x01",
            "hurt anyone.\x02\x03",

            "This is Estelle, and that's Joshua.\x02\x03",

            "You remember them, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xC,
        "#311F#1PScreee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x136,
        "#041F#2PGood boy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#004FWow... You can actually talk to\x01",
            "him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x136,
        (
            "#040F#2PWell, he doesn't actually talk\x01",
            "per se, but I can understand\x01",
            "what he's trying to say.\x02\x03",

            "We've always been able to tell\x01",
            "what the other is feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        (
            "#501FWhooaaa...\x01",
            "Bird telepathy is so...COOL!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x102,
        "#019FSounds like mutual love, to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x136,
        "#041F#2PIt is.\x02",
    )

    CloseMessageWindow()
    OP_92(0x101, 0xC, 0x320, 0x5DC, 0x0)
    Sleep(500)

    ChrTalk(    #84
        0x101,
        (
            "#501FHello, Sieg.\x02\x03",

            "#001FI'm Estelle. It's nice to meet you. ㈱\x01",
            "Now...read my mind!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xC,
        "#310F#1PScree?\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0xC)

    ChrTalk(    #86
        0xC,
        "#310F#1PScreeeeee...\x02",
    )

    CloseMessageWindow()

    def lambda_23F7():

        label("loc_23F7")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_23F7")

    QueueWorkItem2(0x101, 1, lambda_23F7)

    def lambda_2408():

        label("loc_2408")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2408")

    QueueWorkItem2(0x102, 1, lambda_2408)

    def lambda_2419():

        label("loc_2419")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2419")

    QueueWorkItem2(0x136, 1, lambda_2419)
    OP_22(0x8C, 0x0, 0x64)
    Fade(250)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x136, 0x20)
    SetChrSubChip(0x136, 2)
    OP_0D()

    def lambda_2444():
        OP_8E(0xFE, 0xFFFFD260, 0x1B58, 0x6EFA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2444)
    Sleep(400)

    def lambda_2464():
        OP_8E(0xFE, 0xFFFFD260, 0x1B58, 0x6EFA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2464)
    Sleep(400)

    def lambda_2484():
        OP_8E(0xFE, 0xFFFFD260, 0x1B58, 0x6EFA, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2484)
    Sleep(400)

    def lambda_24A4():
        OP_8E(0xFE, 0xFFFFD260, 0x1B58, 0x6EFA, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_24A4)

    ChrTalk(    #87
        0x101,
        (
            "#004FOh...\x02\x03",

            "#007F*sniffle* Are... Are my thoughts\x01",
            "too complex to read?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x102,
        (
            "#019FIf you were thinking of what\x01",
            "I think you were thinking of,\x01",
            "then...no.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x136,
        "#045F#2P*snicker*\x02",
    )

    CloseMessageWindow()
    OP_44(0x136, 0xFF)
    SetChrChipByIndex(0x136, 6)
    SetChrSubChip(0x136, 0)
    OP_8C(0x136, 135, 400)

    ChrTalk(    #90
        0x136,
        (
            "#040F#2POh, by the way, aren't you two\x01",
            "headed for Ruan?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x136, 200)
    OP_44(0x101, 0xFF)
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(    #91
        0x101,
        (
            "#006FYeah, we're planning to register\x01",
            "at the local guild.\x02\x03",

            "If we don't do that, we can't work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x136,
        (
            "#040F#2PWell, if you're going to the Ruanian\x01",
            "guild, I have a few things to do over\x01",
            "there myself.\x02\x03",

            "Maybe I could show you around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#501FReally?! That'd be great.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x102,
        (
            "#010FBut don't you have to go back\x01",
            "to school soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x136,
        (
            "#040F#2PNo, it's all right. I got special\x01",
            "permission to be out today.\x02\x03",

            "I don't have to return until after\x01",
            "nightfall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        (
            "#001FSounds like a plan, then. ♪\x02\x03",

            "Let's go to Ruan!\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xC, 0x80)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrPos(0x101, -120, 10, 29740, 180)
    SetChrPos(0x102, -120, 10, 29740, 180)
    SetChrPos(0x136, -120, 10, 29740, 180)
    OP_6D(-120, 10, 29740, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(500, 0)
    EventEnd(0x0)
    Return()

    # Function_10_1E92 end

    def Function_11_2882(): pass

    label("Function_11_2882")

    ClearChrFlags(0x101, 0x80)
    OP_8E(0x101, 0x0, 0x0, 0x724C, 0x7D0, 0x0)

    def lambda_28A1():

        label("loc_28A1")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_28A1")

    QueueWorkItem2(0xFE, 2, lambda_28A1)
    Return()

    # Function_11_2882 end

    def Function_12_28AD(): pass

    label("Function_12_28AD")

    Sleep(800)
    ClearChrFlags(0x102, 0x80)
    OP_8E(0xFE, 0x0, 0x0, 0x7BB6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5DC, 0x0, 0x7698, 0x7D0, 0x0)

    def lambda_28E5():

        label("loc_28E5")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_28E5")

    QueueWorkItem2(0xFE, 2, lambda_28E5)
    Return()

    # Function_12_28AD end

    def Function_13_28F1(): pass

    label("Function_13_28F1")

    Sleep(800)
    Sleep(800)
    ClearChrFlags(0x136, 0x80)
    OP_8E(0xFE, 0x0, 0x0, 0x7BB6, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_72(0x0, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x0, 20)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    OP_8E(0x136, 0xFFFFFF7E, 0xA, 0x7850, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_13_28F1 end

    def Function_14_2968(): pass

    label("Function_14_2968")

    EventBegin(0x0)
    OP_6D(310, 0, -160, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3840, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    FadeToBright(2000, 0)
    OP_6D(1900, 0, 36890, 10000)
    SetMapFlags(0x2000000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2411   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_2968 end

    def Function_15_29DD(): pass

    label("Function_15_29DD")

    EventBegin(0x0)
    OP_6D(3610, 0, 34400, 0)
    OP_6C(57000, 0)
    LoadEffect(0x0, "map\\\\mpfire0.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 3450, 2000, 34330, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 3650, 1000, 33330, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    FadeToBright(2000, 0)
    OP_6C(351000, 4000)
    SetMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2411   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_29DD end

    SaveToFile()

Try(main)
