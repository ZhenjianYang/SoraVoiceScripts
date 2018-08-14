from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '克拉姆',                               # 9
        '波利',                                 # 10
        '玛丽',                                 # 11
        '达尼艾尔',                             # 12
        '鸡',                                   # 13
        '鸡',                                   # 14
        '鸡',                                   # 15
        '目标用照相机',                         # 16
        '',                                     # 17
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
        "Function_6_5CD",          # 06, 6
        "Function_7_AC9",          # 07, 7
        "Function_8_DD6",          # 08, 8
        "Function_9_DFE",          # 09, 9
        "Function_10_1E26",        # 0A, 10
        "Function_11_1EAE",        # 0B, 11
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CC")
    OP_43(0xFE, 0x2, 0x0, 0x4)
    OP_22(0x191, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x38B, 1)"), scpexpr(EXPR_END)), "loc_5CC")
    TalkBegin(0xFE)
    OP_A2(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x8B\x03\x07\x00。\x02",
    )

    Jump("loc_5B4")

    label("loc_5B4")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFE)

    label("loc_5CC")

    Return()

    # Function_5_544 end

    def Function_6_5CD(): pass

    label("Function_6_5CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
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
        "\x18\x07\x0C很快就是老师的生日了。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #2
        (
            "\x18\x07\x0C孩子们都提早干完了活，\x01",
            "秘密地做着准备。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #3
        (
            "\x18\x07\x0C一直承蒙老师的照顾，\x01",
            "所以在我们开的生日晚会上，\x01",
            "希望能让她好好开心一下。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #4
        (
            "\x18\x07\x0C但是礼物还没决定。\x01",
            "唔，选什么才好呢……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #5
        (
            "\x18\x07\x0C有什么适合老师的，\x01",
            "最棒的礼物…………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_1D(0xF)
    OP_C8(0x200, 0x46, "C_PLAC05._CH", 0x1, 0x7D0)
    FadeToBright(2000, 0)

    def lambda_7BA():
        OP_6D(740, 500, 32800, 10000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_7BA)

    def lambda_7D2():
        OP_6C(38000, 10000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_7D2)
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
            "#1710F那么，达尼艾尔\x01",
            "要完成浇水的工作哦。\x02\x03",

            "波利负责花坛。\x02\x03",

            "#1718F我就去给老师\x01",
            "帮忙做饭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x13,
        (
            "#1720F然后我们就来决定\x01",
            "老师的生日礼物吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x14E,
        (
            "#1711F是啊⊙ \x02\x03",

            "#1718F所以要迅速\x01",
            "把工作完成哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x13,
        "#1721F嗯，知道啦！\x02",
    )


    ChrTalk(    #10
        0x11,
        "#1732F明白了～。\x02",
    )

    OP_56(0x1)
    OP_59()

    def lambda_95D():
        OP_8E(0xFE, 0x1964, 0xFA, 0x5460, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_95D)
    Sleep(300)

    def lambda_97D():
        OP_8E(0xFE, 0x32C8, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_97D)
    Sleep(2000)
    OP_6D(750, 500, 25800, 2500)
    OP_8C(0x14E, 180, 500)
    Sleep(500)

    ChrTalk(    #11
        0x14E,
        (
            "#1710F#5P好了，接着是克拉姆……\x02\x03",

            "#1715F好慢啊～。\x01",
            "肯定又在哪里闲逛了吧。\x02\x03",

            "#1716F真是的，\x01",
            "总是长不大的孩子……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14E, 0, 400)
    Sleep(500)

    def lambda_A4E():
        OP_6D(-400, 500, 32800, 6000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_A4E)

    def lambda_A66():
        OP_8E(0xFE, 0xFFFFFFD8, 0x0, 0x7BAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_A66)
    WaitChrThread(0x14E, 0x1)
    Sleep(200)
    OP_70(0x0, 0x13)
    OP_73(0x0)
    Sleep(200)

    def lambda_A9A():
        OP_8E(0xFE, 0xFFFFFFD8, 0x0, 0x837C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_A9A)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    NewScene("ED6_DT21/T2412   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_5CD end

    def Function_7_AC9(): pass

    label("Function_7_AC9")

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

    def lambda_BB5():
        OP_8E(0xFE, 0x0, 0x0, 0x7A44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_BB5)
    WaitChrThread(0x14E, 0x1)

    ChrTalk(    #12
        0x14E,
        "#1714F#1P啊，克拉姆。\x02",
    )

    CloseMessageWindow()
    OP_72(0x0, 0x8)
    ExitThread()
    OP_6F(0x0, 19)
    OP_70(0x0, 0x0)
    OP_22(0x7, 0x0, 0x64)

    def lambda_C10():
        OP_6D(200, 500, 27600, 2000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_C10)

    def lambda_C28():
        OP_8E(0xFE, 0x64, 0x0, 0x6FA4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_C28)
    WaitChrThread(0x14E, 0x1)

    ChrTalk(    #13
        0x14E,
        (
            "#1718F#1P怎么了？\x01",
            "有没有把生日晚会的装饰物\x01",
            "都买好啊？\x02",
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
            "#1717F啊，克拉姆怎么空着手啊！\x01",
            "你怎么什么都没买啊！？\x02",
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
            "#772F这个嘛……\x02\x03",

            "#771F嘿嘿，\x01",
            "我打听到了很不得了的事哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x0)
    Sleep(1000)

    def lambda_D6E():
        OP_6B(3080, 4000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_D6E)
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
        "\x07\x00几小时前――\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)
    OP_C4(0x1, 0x800)
    NewScene("ED6_DT21/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_AC9 end

    def Function_8_DD6(): pass

    label("Function_8_DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DFD")
    OP_95(0x10, 0x0, 0x12C, 0x0, 0x12C, 0x1388)
    Sleep(1000)
    Jump("Function_8_DD6")

    label("loc_DFD")

    Return()

    # Function_8_DD6 end

    def Function_9_DFE(): pass

    label("Function_9_DFE")

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

    def lambda_EFD():
        OP_6B(2680, 2000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_EFD)
    OP_0D()
    WaitChrThread(0x17, 0x1)

    ChrTalk(    #17
        0x14E,
        "#1719F幸福之石…………\x02",
    )

    CloseMessageWindow()
    OP_22(0xF, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0xA, 0xB, 0xC8, 0x5)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #18
        0x14E,
        "#1903F哇啊，好棒哦～……㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        "#771F是吧，很厉害吧！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        (
            "#1732F好漂亮～。\x01",
            "好酷～。\x02",
        )
    )

    Jump("loc_FCB")

    label("loc_FCB")

    CloseMessageWindow()

    ChrTalk(    #21
        0x14E,
        (
            "#1719F闪闪发亮的魔法石，\x01",
            "……真令人憧憬啊～……\x02\x03",

            "#1718F呵呵，欧尼尔叔叔\x01",
            "还真会讲故事呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x13,
        (
            "#1721F嗯嗯，\x01",
            "我真是感动得不行！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        "#770F………………\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x10, 0)
    OP_95(0x10, 0xFFFFFF88, 0xC8, 0x0, 0x12C, 0x1388)
    OP_22(0xA4, 0x0, 0x64)

    ChrTalk(    #24
        0x10,
        (
            "#771F#3S好，走吧。达尼艾尔！#2S\x02\x03",

            "#3S我们去寻找\x01",
            "幸福之石！#2S\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #25
        0x13,
        "#1723F咦咦……！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 600)
    ClearChrFlags(0x10, 0x4)
    OP_96(0x10, 0x13D8, 0x0, 0x6720, 0xC8, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)

    def lambda_1158():
        OP_8E(0xFE, 0x1004, 0x0, 0x65F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1158)
    SetChrChipByIndex(0x13, 3)
    ClearChrFlags(0x13, 0x4)
    OP_96(0x13, 0x224C, 0x0, 0x6040, 0xC8, 0x1388)
    OP_22(0xA4, 0x0, 0x3C)
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)
    Sleep(300)

    ChrTalk(    #26
        0x14E,
        (
            "#1714F慢、慢着，克拉姆！？\x01",
            "你要去哪里啊！\x02",
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
            "#772F那还用说，\x01",
            "说到这附近的高山\x01",
            "不就是古罗尼连峰吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 0, 500)
    Sleep(400)

    def lambda_1279():
        OP_8E(0xFE, 0x1004, 0x0, 0x69DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1279)
    WaitChrThread(0x10, 0x1)

    ChrTalk(    #28
        0x10,
        (
            "#770F科洛丝姐姐\x01",
            "也说过那是\x01",
            "利贝尔最高的山……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 90, 500)
    Sleep(400)

    ChrTalk(    #29
        0x10,
        (
            "#771F那座山里，\x01",
            "可能就有幸福之石哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 500)
    Sleep(400)

    def lambda_131C():
        OP_8E(0xFE, 0x1004, 0x0, 0x65F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_131C)
    WaitChrThread(0x10, 0x1)

    ChrTalk(    #30
        0x10,
        "#772F……不是『可能』，而是一定会找出来的。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 90, 500)

    ChrTalk(    #31
        0x10,
        (
            "#771F#3S因为我们可是\x01",
            "不屈不挠的男子汉啊！#2S\x02",
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
            "#1716F我说克拉姆啊，\x01",
            "你的心情我很能理解。\x02\x03",

            "……但是欧尼尔叔叔的话啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        (
            "#770F玛丽和波利\x01",
            "就在这里等好了。\x02\x03",

            "#771F#3S走吧达尼艾尔！#2S\x02",
        )
    )

    CloseMessageWindow()

    def lambda_148E():
        OP_6D(5800, 200, 26340, 1000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_148E)

    def lambda_14A6():
        OP_6C(312000, 1000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_14A6)

    def lambda_14B6():
        OP_8E(0xFE, 0x258, 0x0, 0x5780, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_14B6)
    SetChrSubChip(0x11, 2)

    def lambda_14D6():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_14D6)

    ChrTalk(    #34 op#A
        0x14E,
        "#1714F#15A啊，克拉姆！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0x1)

    ChrTalk(    #35 op#A
        0x13,
        "#1723F#20A#4P等等啊克拉姆——！\x02",
    )

    CloseMessageWindow()

    def lambda_153A():
        OP_8E(0xFE, 0x258, 0x0, 0x5780, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_153A)

    ChrTalk(    #36 op#A
        0x13,
        "#1723F#25A#4P我也是不屈不挠的男子汉吗～？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 0x1)
    OP_44(0x14E, 0x1)
    Sleep(2000)

    def lambda_1599():
        OP_8E(0xFE, 0x9C4, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1599)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 90, 500)
    Sleep(200)
    OP_8C(0x14E, 270, 500)
    Sleep(400)

    ChrTalk(    #37
        0x10,
        (
            "#772F玛丽，\x01",
            "生日礼物的事要瞒着老师啊。\x02\x03",

            "#770F注意别穿帮哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x14E,
        (
            "#1715F那、那种事\x01",
            "我早就知道啦！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_164C():
        OP_8E(0xFE, 0xFFFFFE70, 0x0, 0x5208, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_164C)

    ChrTalk(    #39
        0x14E,
        (
            "#1715F倒是你，克拉姆。\x01",
            "欧尼尔叔叔的话啊……\x02",
        )
    )

    Sleep(1000)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #40
        0x14E,
        "#1717F#3S好好听人家说话啦！#2S\x02",
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

    def lambda_1713():
        OP_6D(7660, 400, 24340, 3000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1713)

    def lambda_172B():
        OP_6C(35000, 3000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_172B)

    def lambda_173B():
        OP_8E(0xFE, 0x25E4, 0x0, 0x68B0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_173B)
    WaitChrThread(0x14E, 0x1)

    def lambda_175B():
        OP_8E(0xFE, 0x25E4, 0x0, 0x5E88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_175B)
    WaitChrThread(0x14E, 0x1)

    def lambda_177B():
        OP_8E(0xFE, 0x1DEC, 0x0, 0x5F14, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_177B)
    WaitChrThread(0x14E, 0x1)
    WaitChrThread(0x17, 0x0)

    ChrTalk(    #41
        0x14E,
        (
            "#1716F……唉，\x01",
            "克拉姆真是大笨蛋。\x02\x03",

            "欧尼尔叔叔的话\x01",
            "都是骗人的啦。\x02\x03",

            "#1712F虽然圣典里\x01",
            "的确也有这个故事，\x01",
            "但是一定不是真的……\x02\x03",

            "#1712F幸福之石这种东西啊，\x01",
            "就算再怎么找也找不到的啦！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x2)
    Sleep(1600)
    OP_63(0x14E)

    ChrTalk(    #42
        0x14E,
        (
            "#1719F（…………不过，）\x02\x03",

            "#1903F（幸福之石啊……\x01",
            "  听起来好棒哦～……）\x02",
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
            "#1733F玛丽～。\x02\x03",

            "玛丽？\x01",
            "……走神了吗～？\x02",
        )
    )

    Jump("loc_1962")

    label("loc_1962")

    CloseMessageWindow()
    WaitChrThread(0x14E, 0x2)

    def lambda_196E():
        OP_8F(0xFE, 0x1DB0, 0xA0, 0x5BF4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_196E)
    WaitChrThread(0x11, 0x1)
    OP_63(0x14E)

    def lambda_1991():
        OP_9E(0xFE, 0x14, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14E, 3, lambda_1991)
    Sleep(500)

    def lambda_19B0():
        OP_8F(0xFE, 0x1D4C, 0xA0, 0x5A00, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_19B0)

    def lambda_19CB():
        OP_95(0xFE, 0x0, 0x12C, 0x0, 0x12C, 0x1388)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_19CB)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x2, 0x7, 0x96, 0x1)
    Sleep(1000)
    OP_63(0x14E)
    OP_8C(0x14E, 180, 500)
    Sleep(500)

    ChrTalk(    #44
        0x14E,
        (
            "#1714F#1P啊，波利！\x02\x03",

            "#1716F吓、吓我一大跳～。\x01",
            "别吓唬人啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x11,
        (
            "#1730F克拉姆他们\x01",
            "走掉了啊～。\x02\x03",

            "礼物的事情，\x01",
            "都还没决定呢～。\x02",
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
            "#1712F#1P波、波利，\x01",
            "……真是意外地冷静呢。\x02\x03",

            "#1712F虽然我觉得\x01",
            "那是个挺感人的故事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x11,
        "#1733F哎？\x02",
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #48
        0x14E,
        "#1713F#1P这、这个……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14E, 0, 500)
    Sleep(500)

    ChrTalk(    #49
        0x14E,
        (
            "#1716F#1P（波利真是的，\x01",
            "　实在很迟钝啊。）\x02\x03",

            "#1715F（……嗯，\x01",
            "  我还是得振作才行啊！）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14E, 180, 500)
    Sleep(500)

    ChrTalk(    #50
        0x14E,
        (
            "#1710F#1P克拉姆他们就不管啦！\x01",
            "反正说了他们也不听的。\x02\x03",

            "生日礼物的事，\x01",
            "就靠我们俩来想吧。\x02\x03",

            "#1719F唔，送什么好呢……\x02",
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
            "#1710F#1P波利，去海边看看吧。\x02\x03",

            "到平时去的海边，\x01",
            "收集些漂亮的贝壳怎么样呢……\x02\x03",

            "#1711F把很多贝壳穿起来\x01",
            "就可以做成项链了。\x02\x03",

            "嗯，很棒的礼物吧！？\x02\x03",

            "#1718F好，就去海边吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x11,
        "#1732F明白了～。\x02",
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

    # Function_9_DFE end

    def Function_10_1E26(): pass

    label("Function_10_1E26")


    def lambda_1E2C():
        OP_8E(0xFE, 0x25E4, 0x0, 0x6C98, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1E2C)
    WaitChrThread(0x11, 0x1)

    def lambda_1E4C():
        OP_8E(0xFE, 0x25E4, 0x0, 0x60B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1E4C)
    WaitChrThread(0x11, 0x1)

    def lambda_1E6C():
        OP_8E(0xFE, 0x2120, 0x0, 0x5A00, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1E6C)
    WaitChrThread(0x11, 0x1)

    def lambda_1E8C():
        OP_8E(0xFE, 0x1D4C, 0xA0, 0x5A00, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1E8C)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 0, 500)
    Return()

    # Function_10_1E26 end

    def Function_11_1EAE(): pass

    label("Function_11_1EAE")

    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x3)
    Sleep(2400)
    OP_63(0x14E)
    Sleep(1000)
    OP_22(0xF, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0xA, 0xB, 0xC8, 0x0)
    Sleep(2000)
    Return()

    # Function_11_1EAE end

    SaveToFile()

Try(main)
