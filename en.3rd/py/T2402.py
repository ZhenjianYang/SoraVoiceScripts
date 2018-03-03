from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2402   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2402.x',
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
        'Clem',                                 # 9
        'Polly',                                # 10
        'Mary',                                 # 11
        'Daniel',                               # 12
        'Chicken',                              # 13
        'Chicken',                              # 14
        'Chicken',                              # 15
        'Target Camera',                        # 16
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
        'ED6_DT07/CH02500 ._CH',             # 01
        'ED6_DT07/CH02630 ._CH',             # 02
        'ED6_DT07/CH02640 ._CH',             # 03
        'ED6_DT07/CH01720 ._CH',             # 04
        'ED6_DT07/CH02593 ._CH',             # 05
        'ED6_DT07/CH02503 ._CH',             # 06
        'ED6_DT07/CH02633 ._CH',             # 07
        'ED6_DT07/CH02643 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH02590P._CP',             # 00
        'ED6_DT07/CH02500P._CP',             # 01
        'ED6_DT07/CH02630P._CP',             # 02
        'ED6_DT07/CH02640P._CP',             # 03
        'ED6_DT07/CH01720P._CP',             # 04
        'ED6_DT07/CH02593P._CP',             # 05
        'ED6_DT07/CH02503P._CP',             # 06
        'ED6_DT07/CH02633P._CP',             # 07
        'ED6_DT07/CH02643P._CP',             # 08
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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


    ScpFunction(
        "Function_0_1F2",          # 00, 0
        "Function_1_23B",          # 01, 1
        "Function_2_24E",          # 02, 2
        "Function_3_3CB",          # 03, 3
        "Function_4_51E",          # 04, 4
        "Function_5_544",          # 05, 5
        "Function_6_5C7",          # 06, 6
        "Function_7_BE4",          # 07, 7
        "Function_8_F2F",          # 08, 8
        "Function_9_F57",          # 09, 9
        "Function_10_21D5",        # 0A, 10
        "Function_11_225D",        # 0B, 11
    )


    def Function_0_1F2(): pass

    label("Function_0_1F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_217")
    OP_A3(0x2505)
    Event(0, 9)
    Jump("loc_23A")

    label("loc_217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_228")
    OP_A3(0x2504)
    Event(0, 7)
    Jump("loc_23A")

    label("loc_228")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_23A")

    Return()

    # Function_0_1F2 end

    def Function_1_23B(): pass

    label("Function_1_23B")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE5A20, 0x230067)
    Return()

    # Function_1_23B end

    def Function_2_24E(): pass

    label("Function_2_24E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_273")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3B5")

    label("loc_273")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28C")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3B5")

    label("loc_28C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A5")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3B5")

    label("loc_2A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BE")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3B5")

    label("loc_2BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D7")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3B5")

    label("loc_2D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F0")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3B5")

    label("loc_2F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_309")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3B5")

    label("loc_309")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_322")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3B5")

    label("loc_322")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33B")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3B5")

    label("loc_33B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_354")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3B5")

    label("loc_354")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36D")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3B5")

    label("loc_36D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_386")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3B5")

    label("loc_386")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39F")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3B5")

    label("loc_39F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B5")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3B5")

    label("loc_3CA")

    Return()

    # Function_2_24E end

    def Function_3_3CB(): pass

    label("Function_3_3CB")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)
    OP_8D(0xFE, -8760, 13210, 8700, 24630, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3F9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51D")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E2")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2238), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_PUSH_LONG, 0x339A), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x21FC), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x6036), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B7")
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x0, 0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_4A4():
        OP_94(0x0, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A4)
    Jump("loc_4DA")

    label("loc_4B7")


    def lambda_4BD():
        OP_8D(0xFE, -8760, 13210, 8700, 24630, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4BD)
    Sleep(200)

    label("loc_4DA")

    Sleep(30)
    Jump("loc_51A")

    label("loc_4E2")

    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51A")
    OP_44(0xFE, 0x2)

    def lambda_502():
        OP_8D(0xFE, -8760, 13210, 8700, 24630, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_502)

    label("loc_51A")

    Jump("loc_3F9")

    label("loc_51D")

    Return()

    # Function_3_3CB end

    def Function_4_51E(): pass

    label("Function_4_51E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_539")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_4_51E")

    label("loc_539")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_51E end

    def Function_5_544(): pass

    label("Function_5_544")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C6")
    OP_43(0xFE, 0x2, 0x0, 0x4)
    OP_22(0x191, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x38B, 1)"), scpexpr(EXPR_END)), "loc_5C6")
    TalkBegin(0xFE)
    OP_A2(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x8B\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFE)

    label("loc_5C6")

    Return()

    # Function_5_544 end

    def Function_6_5C7(): pass

    label("Function_6_5C7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x14E, 750, 0, 25880, 90)
    SetChrPos(0x11, 2100, 0, 26320, 270)
    SetChrPos(0x13, 2150, 0, 25320, 270)
    OP_4A(0x11, 255)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_6D(740, 0, 2000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(24000, 0)
    OP_6E(588, 0)
    OP_C4(0x0, 0x800)
    Sleep(2000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "\x18\x07\x0CIt was almost time for Matron Theresa's birthday.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #2
        (
            "\x18\x07\x0CThe children were keenly aware of this fact, too.\x01",
            "One by one, they finished their chores early and\x01",
            "gathered to decide what to do for it.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #3
        (
            "\x18\x07\x0CAfter all the matron always did for them, they\x01",
            "wanted to make it an occasion to remember.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #4
        (
            "\x18\x07\x0CBut they still hadn't decided what to get her as\x01",
            "a present.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #5
        (
            "\x18\x07\x0CThere had to be something out there that was\x01",
            "perfect for her--something that would make her\x01",
            "really happy...but what?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_1D(0xF)
    OP_C8(0x200, 0x46, "C_PLAC05._CH", 0x1, 0x7D0)
    FadeToBright(2000, 0)

    def lambda_887():
        OP_6D(740, 500, 32800, 10000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_887)

    def lambda_89F():
        OP_6C(38000, 10000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_89F)
    WaitChrThread(0x17, 0x0)
    OP_0D()
    OP_C4(0x1, 0x800)
    Fade(1000)
    OP_6D(1600, 500, 25800, 0)
    OP_67(0, 7540, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x17, 0x0)
    Sleep(1000)

    ChrTalk(    #6
        0x14E,
        (
            "#1710FCan you finish watering the plants, then,\x01",
            "Daniel?\x02\x03",

            "You can take care of the flower beds, Polly.\x02\x03",

            "#1718FAs for me, I'll go help with the cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x13,
        (
            "#1720FThen we're gonna decide on what to get the\x01",
            "matron as a present?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x14E,
        (
            "#1711FYep! ♪\x02\x03",

            "#1718FSo let's hop to it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x13,
        "#1721FRight!\x02",
    )


    ChrTalk(    #10
        0x11,
        "#1732FOkay!\x02",
    )

    OP_56(0x1)
    OP_59()

    def lambda_A40():
        OP_8E(0xFE, 0x1964, 0xFA, 0x5460, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_A40)
    Sleep(300)

    def lambda_A60():
        OP_8E(0xFE, 0x32C8, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A60)
    Sleep(2000)
    OP_6D(750, 500, 25800, 2500)
    OP_8C(0x14E, 180, 500)
    Sleep(500)

    ChrTalk(    #11
        0x14E,
        (
            "#1710F#5PNow this just leaves Clem...\x02\x03",

            "#1715FWhere IS he? He should be back by now...\x01",
            "This isn't the first time he's taken forever\x01",
            "coming back home, either.\x02\x03",

            "#1716FI wish he'd grow up...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14E, 0, 400)
    Sleep(500)

    def lambda_B69():
        OP_6D(-400, 500, 32800, 6000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_B69)

    def lambda_B81():
        OP_8E(0xFE, 0xFFFFFFD8, 0x0, 0x7BAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_B81)
    WaitChrThread(0x14E, 0x1)
    Sleep(200)
    OP_70(0x0, 0x13)
    OP_73(0x0)
    Sleep(200)

    def lambda_BB5():
        OP_8E(0xFE, 0xFFFFFFD8, 0x0, 0x837C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_BB5)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    NewScene("ED6_DT21/T2412   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_5C7 end

    def Function_7_BE4(): pass

    label("Function_7_BE4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x14E, 0, 0, 33000, 180)
    SetChrPos(0x11, -600, 60, 25300, 1)
    SetChrPos(0x13, 560, 0, 25420, 0)
    SetChrPos(0x10, 100, 0, 27020, 180)
    OP_4A(0x11, 255)
    OP_4A(0x13, 255)
    OP_4A(0x10, 255)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_6D(200, 500, 31800, 0)
    OP_67(0, 6960, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_62(0x10, 0x0, 1600, 0x26, 0x27, 0xC8, 0x0)
    OP_43(0x10, 0x1, 0x0, 0x8)
    FadeToBright(2000, 0)
    OP_0D()
    OP_70(0x0, 0x13)
    OP_73(0x0)
    Sleep(200)

    def lambda_CD0():
        OP_8E(0xFE, 0x0, 0x0, 0x7A44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_CD0)
    WaitChrThread(0x14E, 0x1)

    ChrTalk(    #12
        0x14E,
        "#1714F#1POh! You're back, Clem.\x02",
    )

    CloseMessageWindow()
    OP_72(0x0, 0x8)
    ExitThread()
    OP_6F(0x0, 19)
    OP_70(0x0, 0x0)
    OP_22(0x7, 0x0, 0x64)

    def lambda_D2E():
        OP_6D(200, 500, 27600, 2000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_D2E)

    def lambda_D46():
        OP_8E(0xFE, 0x64, 0x0, 0x6FA4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_D46)
    WaitChrThread(0x14E, 0x1)

    ChrTalk(    #13
        0x14E,
        (
            "#1718F#1PWell? Did you manage to buy the decorations\x01",
            "we need for Matron's birthday?\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x2, 0x7, 0x96, 0x1)
    Sleep(1000)
    OP_63(0x14E)
    Sleep(400)

    ChrTalk(    #14
        0x14E,
        (
            "#1717FNo, you didn't! Don't tell me you didn't buy\x01",
            "ANYTHING?!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_63(0x10)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 0, 500)
    Sleep(500)

    ChrTalk(    #15
        0x10,
        (
            "#772FWell, I was gonna...\x02\x03",

            "#771F...but I ended up hearing this real\x01",
            "interesting story instead!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x0)
    Sleep(1000)

    def lambda_EBD():
        OP_6B(3080, 4000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_EBD)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_63(0x14E)
    OP_20(0x7D0)
    OP_21()
    OP_C4(0x0, 0x800)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x00Several hours earlier...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)
    OP_C4(0x1, 0x800)
    NewScene("ED6_DT21/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_BE4 end

    def Function_8_F2F(): pass

    label("Function_8_F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F56")
    OP_95(0x10, 0x0, 0x12C, 0x0, 0x12C, 0x1388)
    Sleep(1000)
    Jump("Function_8_F2F")

    label("loc_F56")

    Return()

    # Function_8_F2F end

    def Function_9_F57(): pass

    label("Function_9_F57")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4A(0x11, 255)
    OP_4A(0x13, 255)
    OP_4A(0x10, 255)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x14E, 0x4)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x14E, 0x40)
    SetChrChipByIndex(0x10, 5)
    SetChrChipByIndex(0x11, 6)
    SetChrChipByIndex(0x14E, 7)
    SetChrChipByIndex(0x13, 8)
    SetChrPos(0x14E, 8630, 200, 27230, 270)
    SetChrPos(0x11, 8710, 200, 28420, 270)
    SetChrPos(0x13, 8720, 200, 25650, 270)
    SetChrPos(0x10, 6100, 200, 26960, 90)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_6D(7300, 400, 27260, 0)
    OP_67(0, 7180, -10000, 0)
    OP_6B(2780, 0)
    OP_6C(320000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)

    def lambda_1056():
        OP_6B(2680, 2000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1056)
    OP_0D()
    WaitChrThread(0x17, 0x1)

    ChrTalk(    #17
        0x14E,
        "#1719FI've never heard of that before...\x02",
    )

    CloseMessageWindow()
    OP_22(0xF, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0xA, 0xB, 0xC8, 0x5)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #18
        0x14E,
        "#1903FIt sounds so dreamy... ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        "#771FSee? I told you it was amazing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        "#1732FIt must be so pretty! And so cool...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x14E,
        (
            "#1719FI wish I could find a pretty magical stone like\x01",
            "that...\x02\x03",

            "#1718FHeehee. Mr. O'Neil tells the best stories,\x01",
            "doesn't he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x13,
        "#1721FYeah! That was a great story!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        "#770F...\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x10, 0)
    OP_95(0x10, 0xFFFFFF88, 0xC8, 0x0, 0x12C, 0x1388)
    OP_22(0xA4, 0x0, 0x64)

    ChrTalk(    #24
        0x10,
        (
            "#771F#3SOkay! Move your butt, Daniel!#2S\x02\x03",

            "#3SWe're gonna go find a happiness stone!#2S\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #25
        0x13,
        "#1723FWhaaat?!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 600)
    ClearChrFlags(0x10, 0x4)
    OP_96(0x10, 0x13D8, 0x0, 0x6720, 0xC8, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)

    def lambda_12BF():
        OP_8E(0xFE, 0x1004, 0x0, 0x65F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_12BF)
    SetChrChipByIndex(0x13, 3)
    ClearChrFlags(0x13, 0x4)
    OP_96(0x13, 0x224C, 0x0, 0x6040, 0xC8, 0x1388)
    OP_22(0xA4, 0x0, 0x3C)
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)
    Sleep(300)

    ChrTalk(    #26
        0x14E,
        (
            "#1714FW-Wait a second, Clem! Where do you think\x01",
            "you're going?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_22(0xA4, 0x0, 0x3C)
    SetChrPos(0x14E, 9400, 0, 26800, 270)
    ClearChrFlags(0x14E, 0x4)
    SetChrChipByIndex(0x14E, 65535)
    SetChrFlags(0x14E, 0x40)
    Sleep(1000)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 90, 500)
    Sleep(400)

    ChrTalk(    #27
        0x10,
        (
            "#772FWhere do you THINK? The only tall mountains\x01",
            "around here're the Krone mountains!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 0, 500)
    Sleep(400)

    def lambda_1406():
        OP_8E(0xFE, 0x1004, 0x0, 0x69DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1406)
    WaitChrThread(0x10, 0x1)

    ChrTalk(    #28
        0x10,
        (
            "#770FKloe said they were the tallest point in Liberl,\x01",
            "too...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 90, 500)
    Sleep(400)

    ChrTalk(    #29
        0x10,
        (
            "#771FIf we're gonna find ourselves a happiness\x01",
            "stone anywhere, it's gotta be there!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 500)
    Sleep(400)

    def lambda_14D9():
        OP_8E(0xFE, 0x1004, 0x0, 0x65F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_14D9)
    WaitChrThread(0x10, 0x1)

    ChrTalk(    #30
        0x10,
        "#772FAnd we're gonna find one! We are!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 90, 500)

    ChrTalk(    #31
        0x10,
        (
            "#771F#3SI'm gonna be an invincible guy just like\x01",
            "Mr. O'Neil was!#2S\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0xC8)
    CloseMessageWindow()
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x10, 0x13, 0xC8, 0x1)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #32
        0x14E,
        (
            "#1716FUmm... Clem, I understand why you're so \x01",
            "desperate to find one. Really, I do...\x02\x03",

            "But Mr. O'Neil's stories are...well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        (
            "#770FYou just wait here with Polly, Mary.\x01",
            "We'll be back before you know it!\x02\x03",

            "#771F#3SLet's get movin', Daniel! #2S\x02",
        )
    )

    CloseMessageWindow()

    def lambda_16A0():
        OP_6D(5800, 200, 26340, 1000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_16A0)

    def lambda_16B8():
        OP_6C(312000, 1000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_16B8)

    def lambda_16C8():
        OP_8E(0xFE, 0x258, 0x0, 0x5780, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_16C8)
    SetChrSubChip(0x11, 2)

    def lambda_16E8():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_16E8)

    ChrTalk(    #34 op#A
        0x14E,
        "#1714F#15AWait, Clem!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0x1)

    def lambda_1716():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1716)

    ChrTalk(    #35 op#A
        0x13,
        "#1723F#20A#4PWait for me!\x02",
    )

    CloseMessageWindow()

    def lambda_1747():
        OP_8E(0xFE, 0x258, 0x0, 0x5780, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1747)

    ChrTalk(    #36 op#A
        0x13,
        "#1723F#25A#4PI wanna be an invincible guy, too!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 0x1)

    def lambda_179C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_179C)
    OP_44(0x14E, 0x1)
    Sleep(2000)

    def lambda_17B7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_17B7)

    def lambda_17C9():
        OP_8E(0xFE, 0x9C4, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_17C9)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 90, 500)
    Sleep(200)
    OP_8C(0x14E, 270, 500)
    Sleep(400)

    ChrTalk(    #37
        0x10,
        (
            "#772FJust make sure the matron doesn't find out\x01",
            "about what we're planning for her present,\x01",
            "Mary!\x02\x03",

            "#770FIt's gotta be a surprise!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x14E,
        "#1715FI know that!\x02",
    )

    CloseMessageWindow()

    def lambda_189F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_189F)

    def lambda_18B1():
        OP_8E(0xFE, 0xFFFFFE70, 0x0, 0x5208, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_18B1)

    ChrTalk(    #39
        0x14E,
        "#1715FBut listen to me, Clem! Mr. O'Neil's stories are...\x02",
    )

    Sleep(1000)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #40
        0x14E,
        "#1717F#3SLISTEN TO ME!#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0xC8)
    CloseMessageWindow()
    Sleep(500)
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2400)
    OP_63(0x14E)
    Sleep(500)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x13, 0x80)

    def lambda_1973():
        OP_6D(7660, 400, 24340, 3000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1973)

    def lambda_198B():
        OP_6C(35000, 3000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_198B)

    def lambda_199B():
        OP_8E(0xFE, 0x25E4, 0x0, 0x68B0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_199B)
    WaitChrThread(0x14E, 0x1)

    def lambda_19BB():
        OP_8E(0xFE, 0x25E4, 0x0, 0x5E88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_19BB)
    WaitChrThread(0x14E, 0x1)

    def lambda_19DB():
        OP_8E(0xFE, 0x1DEC, 0x0, 0x5F14, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_19DB)
    WaitChrThread(0x14E, 0x1)
    WaitChrThread(0x17, 0x0)

    ChrTalk(    #41
        0x14E,
        (
            "#1716F*sigh* He's so stupid...\x02\x03",

            "Both for not realizing Mr. O'Neil's stories are all\x01",
            "made up and for not listening to me trying to tell\x01",
            "him...\x02\x03",

            "#1712FWorking some of the Testaments into one doesn't\x01",
            "make the rest of what he's saying credible...\x02\x03",

            "#1712FIt doesn't matter how long he spends trying to find\x01",
            "a happiness stone. He's not going to!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x2)
    Sleep(1600)
    OP_63(0x14E)

    ChrTalk(    #42
        0x14E,
        (
            "#1719F(Still...)\x02\x03",

            "#1903F(I wish they really did exist. They sound so\x01",
            "lovely...)\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0xA4, 0x0, 0x3C)
    SetChrPos(0x11, 9300, 0, 27800, 225)
    ClearChrFlags(0x11, 0x4)
    SetChrChipByIndex(0x11, 1)
    Sleep(1000)
    OP_43(0x11, 0x2, 0x0, 0xA)
    OP_43(0x14E, 0x2, 0x0, 0xB)
    WaitChrThread(0x11, 0x2)

    ChrTalk(    #43
        0x11,
        (
            "#1733FMary?\x02\x03",

            "Mary? Earth to Mary?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x14E, 0x2)

    def lambda_1C31():
        OP_8F(0xFE, 0x1DB0, 0xA0, 0x5BF4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1C31)
    WaitChrThread(0x11, 0x1)
    OP_63(0x14E)

    def lambda_1C54():
        OP_9E(0xFE, 0x14, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14E, 3, lambda_1C54)
    Sleep(500)

    def lambda_1C73():
        OP_8F(0xFE, 0x1D4C, 0xA0, 0x5A00, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1C73)

    def lambda_1C8E():
        OP_95(0xFE, 0x0, 0x12C, 0x0, 0x12C, 0x1388)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_1C8E)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x2, 0x7, 0x96, 0x1)
    Sleep(1000)
    OP_63(0x14E)
    OP_8C(0x14E, 180, 500)
    Sleep(500)

    ChrTalk(    #44
        0x14E,
        (
            "#1714F#1POh, sorry!\x02\x03",

            "#1716FD-Don't make me jump like that... You really\x01",
            "scared me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x11,
        (
            "#1730FThey went away now, but we still dunno\x01",
            "what to do for the matron's present.\x02\x03",

            "What're we gonna do?\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x10, 0x13, 0xC8, 0x1)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #46
        0x14E,
        (
            "#1712F#1PI'm surprised that story didn't have any\x01",
            "effect on you...\x02\x03",

            "#1712FIt might not be real, but I thought it was\x01",
            "pretty touching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x11,
        "#1733FTouchy?\x02",
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #48
        0x14E,
        "#1713F#1PU-Umm...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14E, 0, 500)
    Sleep(500)

    ChrTalk(    #49
        0x14E,
        (
            "#1716F#1P(She'll never be quite all there, will she?)\x02\x03",

            "#1715F(This is why I need to look out for everyone!)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14E, 180, 500)
    Sleep(500)

    ChrTalk(    #50
        0x14E,
        (
            "#1710F#1PLet's just let Clem and Daniel do what they want!\x01",
            "Clem's not going to listen to us even if we go\x01",
            "after him, anyway.\x02\x03",

            "Which means we're going to have to think up a\x01",
            "present ourselves.\x02\x03",

            "#1719FIf only I knew what would be good enough...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x2)
    Sleep(1600)
    OP_63(0x14E)
    OP_22(0x163, 0x0, 0x46)
    Sleep(2500)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xFA, 0x1)
    Sleep(500)
    OP_63(0x14E)

    ChrTalk(    #51
        0x14E,
        (
            "#1710F#1PShall we go and have a look along the shore?\x02\x03",

            "There might be some pretty shells there.\x02\x03",

            "#1711FIf we collect enough of them, we might even be\x01",
            "able to make a necklace for her.\x02\x03",

            "That sounds like it might make for a good present,\x01",
            "right?\x02\x03",

            "#1718FOkay! Let's get going!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x11,
        "#1732FOkaaay!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    ClearChrFlags(0x14E, 0x4)
    ClearChrFlags(0x14E, 0x40)
    SetChrChipByIndex(0x14E, 65535)
    AddParty(0x4E, 0xFF, 0xFF)
    SetChrPos(0x14F, 7500, 160, 23040, 0)
    SetChrPos(0x14, -4730, 350, 18080, 0)
    SetChrPos(0x15, -4860, 390, 24170, 142)
    SetChrPos(0x16, 3970, 200, 17310, 307)
    OP_4B(0x14, 255)
    OP_4B(0x15, 255)
    OP_4B(0x16, 255)
    OP_A2(0x2F17)
    EventEnd(0x0)
    Return()

    # Function_9_F57 end

    def Function_10_21D5(): pass

    label("Function_10_21D5")


    def lambda_21DB():
        OP_8E(0xFE, 0x25E4, 0x0, 0x6C98, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_21DB)
    WaitChrThread(0x11, 0x1)

    def lambda_21FB():
        OP_8E(0xFE, 0x25E4, 0x0, 0x60B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_21FB)
    WaitChrThread(0x11, 0x1)

    def lambda_221B():
        OP_8E(0xFE, 0x2120, 0x0, 0x5A00, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_221B)
    WaitChrThread(0x11, 0x1)

    def lambda_223B():
        OP_8E(0xFE, 0x1D4C, 0xA0, 0x5A00, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_223B)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 0, 500)
    Return()

    # Function_10_21D5 end

    def Function_11_225D(): pass

    label("Function_11_225D")

    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x3)
    Sleep(2400)
    OP_63(0x14E)
    Sleep(1000)
    OP_22(0xF, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0xA, 0xB, 0xC8, 0x0)
    Sleep(2000)
    Return()

    # Function_11_225D end

    SaveToFile()

Try(main)
