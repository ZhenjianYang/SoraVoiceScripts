from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0400   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0400.x',
        MapIndex            = 13,
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
        'Tio',                                  # 9
        'Will',                                 # 10
        'Chere',                                # 11
        'Franz',                                # 12
        'Hannah',                               # 13
        'Cow',                                  # 14
        'Cow',                                  # 15
        'Chicken',                              # 16
        'Chicken',                              # 17
        'Chicken',                              # 18
        'Chicken',                              # 19
        'Target Camera',                        # 20
        'Milch Mainroad',                       # 21
    )

    DeclEntryPoint(
        Unknown_00              = 24100,
        Unknown_04              = 0,
        Unknown_08              = 56000,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 13,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 24100,
        Unknown_04              = 0,
        Unknown_08              = 56000,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 13,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02480 ._CH',             # 00
        'ED6_DT07/CH01060 ._CH',             # 01
        'ED6_DT07/CH01070 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01030 ._CH',             # 04
        'ED6_DT07/CH01710 ._CH',             # 05
        'ED6_DT07/CH01720 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH02480P._CP',             # 00
        'ED6_DT07/CH01060P._CP',             # 01
        'ED6_DT07/CH01070P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01030P._CP',             # 04
        'ED6_DT07/CH01710P._CP',             # 05
        'ED6_DT07/CH01720P._CP',             # 06
    )

    DeclNpc(
        X                   = 40470,
        Z                   = 0,
        Y                   = 16320,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 21900,
        Z                   = 0,
        Y                   = 25300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 25100,
        Z                   = 0,
        Y                   = 23000,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 28100,
        Z                   = 0,
        Y                   = 24800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 32800,
        Z                   = 200,
        Y                   = 40000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 39010,
        Z                   = 600,
        Y                   = 22850,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 48160,
        Z                   = 460,
        Y                   = 18800,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 0,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 38780,
        Z                   = 0,
        Y                   = 19310,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 51470,
        Z                   = 0,
        Y                   = 20950,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 51470,
        Z                   = 0,
        Y                   = 20950,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        X                   = 23910,
        Z                   = 30,
        Y                   = 66820,
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
        "Function_0_2C6",          # 00, 0
        "Function_1_432",          # 01, 1
        "Function_2_445",          # 02, 2
        "Function_3_45B",          # 03, 3
        "Function_4_47F",          # 04, 4
        "Function_5_4E3",          # 05, 5
        "Function_6_507",          # 06, 6
        "Function_7_54B",          # 07, 7
        "Function_8_698",          # 08, 8
        "Function_9_69E",          # 09, 9
        "Function_10_72A",         # 0A, 10
        "Function_11_750",         # 0B, 11
        "Function_12_11F9",        # 0C, 12
        "Function_13_17FE",        # 0D, 13
        "Function_14_1D61",        # 0E, 14
        "Function_15_239C",        # 0F, 15
        "Function_16_2580",        # 10, 16
        "Function_17_2803",        # 11, 17
        "Function_18_2813",        # 12, 18
        "Function_19_2C59",        # 13, 19
        "Function_20_2C7F",        # 14, 20
    )


    def Function_0_2C6(): pass

    label("Function_0_2C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_314")
    SetChrPos(0xB, 38770, -300, 38410, 90)
    SetChrPos(0x8, 29400, 0, 12700, 180)
    SetChrPos(0xC, 29740, -300, 39260, 90)
    SetChrPos(0xA, 36000, 0, 41000, 0)
    Jump("loc_390")

    label("loc_314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_354")
    SetChrPos(0xB, 35500, 100, 36000, 90)
    SetChrPos(0x8, 29400, 0, 12700, 180)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    Jump("loc_390")

    label("loc_354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_37C")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    Jump("loc_390")

    label("loc_37C")

    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)

    label("loc_390")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_3A0"),
        (1, "loc_3F2"),
        (SWITCH_DEFAULT, "loc_431"),
    )


    label("loc_3A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EF")
    OP_A2(0x22D)
    SetMapFlags(0x400000)
    OP_6D(24000, 0, 51000, 0)
    OP_6C(36000, 0)
    OP_6B(3000, 0)
    SetChrPos(0x102, 23000, 0, 55000, 0)
    OP_8C(0x102, 180, 0)
    Event(0, 16)

    label("loc_3EF")

    Jump("loc_431")

    label("loc_3F2")

    ClearMapFlags(0x1)
    OP_6D(17500, 0, 22800, 0)
    SetChrPos(0x102, 17000, 600, 23600, 90)
    SetChrPos(0x101, 17500, 600, 22800, 90)
    Event(0, 18)
    Jump("loc_431")

    label("loc_431")

    Return()

    # Function_0_2C6 end

    def Function_1_432(): pass

    label("Function_1_432")

    OP_16(0x2, 0xFA0, 0xFFFE8900, 0xFFFE8900, 0x30004)
    Return()

    # Function_1_432 end

    def Function_2_445(): pass

    label("Function_2_445")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_45A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_445")

    label("loc_45A")

    Return()

    # Function_2_445 end

    def Function_3_45B(): pass

    label("Function_3_45B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47E")
    OP_8D(0xFE, 19800, 21600, 24000, 30300, 3000)
    Jump("Function_3_45B")

    label("loc_47E")

    Return()

    # Function_3_45B end

    def Function_4_47F(): pass

    label("Function_4_47F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_4BF")

    label("loc_486")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4BC")
    OP_92(0xFE, 0xC, 0x3E8, 0xBB8, 0x0)
    Sleep(1000)
    OP_8D(0xFE, 36200, 39800, 32400, 43600, 3000)
    Jump("loc_486")

    label("loc_4BC")

    Jump("loc_4E2")

    label("loc_4BF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E2")
    OP_8D(0xFE, 19800, 21600, 28200, 24800, 3000)
    Jump("loc_4BF")

    label("loc_4E2")

    Return()

    # Function_4_47F end

    def Function_5_4E3(): pass

    label("Function_5_4E3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_506")
    OP_8D(0xFE, 28150, 34670, 34240, 44760, 3000)
    Jump("Function_5_4E3")

    label("loc_506")

    Return()

    # Function_5_4E3 end

    def Function_6_507(): pass

    label("Function_6_507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_527")

    label("loc_50F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_524")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_50F")

    label("loc_524")

    Jump("loc_54A")

    label("loc_527")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54A")
    OP_8D(0xFE, 37390, 35010, 40920, 43630, 3000)
    Jump("loc_527")

    label("loc_54A")

    Return()

    # Function_6_507 end

    def Function_7_54B(): pass

    label("Function_7_54B")

    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, 28710, 33610, 41830, 44000, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_574")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_697")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65C")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7026), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_PUSH_LONG, 0x834A), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0xA366), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0xABE0), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_631")
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x0, 0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_61E():
        OP_94(0x0, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61E)
    Jump("loc_654")

    label("loc_631")


    def lambda_637():
        OP_8D(0xFE, 28710, 33610, 41830, 44000, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_637)
    Sleep(200)

    label("loc_654")

    Sleep(30)
    Jump("loc_694")

    label("loc_65C")

    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_694")
    OP_44(0xFE, 0x2)

    def lambda_67C():
        OP_8D(0xFE, 28710, 33610, 41830, 44000, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_67C)

    label("loc_694")

    Jump("loc_574")

    label("loc_697")

    Return()

    # Function_7_54B end

    def Function_8_698(): pass

    label("Function_8_698")

    OP_22(0x190, 0x0, 0x64)
    Return()

    # Function_8_698 end

    def Function_9_69E(): pass

    label("Function_9_69E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_729")
    OP_43(0xFE, 0x2, 0x0, 0xA)
    OP_22(0x191, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_729")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x38B, 1)"), scpexpr(EXPR_END)), "loc_729")
    TalkBegin(0xFE)
    OP_A2(0x6)
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

    label("loc_729")

    Return()

    # Function_9_69E end

    def Function_10_72A(): pass

    label("Function_10_72A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_745")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_10_72A")

    label("loc_745")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_72A end

    def Function_11_750(): pass

    label("Function_11_750")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_9A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_921")
    OP_A2(0x2B7)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #1
        0xFE,
        (
            "Hey, guys.\x01",
            "What's with the packs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#501FWell, it turns out we're headed\x01",
            "to Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Bose...? But I heard the airliners\x01",
            "had stopped flying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "So does this mean that you're\x01",
            "headed there on foot?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        "#010FIt seems that way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#001FWe'll be fine. I've heard that it's\x01",
            "not that long of a distance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "When it comes to jobs, I guess a\x01",
            "bracer's isn't one that's supposed\x01",
            "to be easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "Anyway, take care of yourselves.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9A2")

    label("loc_921")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #9
        0xFE,
        (
            "When it comes to jobs I guess a\x01",
            "bracer's isn't one that's supposed\x01",
            "to be easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "Anyway, take care of yourselves.\x02",
    )

    CloseMessageWindow()

    label("loc_9A2")

    Jump("loc_11F3")

    label("loc_9A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_AEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A63")
    OP_A2(0x1)

    ChrTalk(    #11
        0xFE,
        "Hi, how are you two doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "I'd sure like to get all our friends\x01",
            "from Sunday School together\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "It's been a while, so I really want\x01",
            "to see Elissa too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AEC")

    label("loc_A63")


    ChrTalk(    #14
        0xFE,
        (
            "I'd sure like to get all our friends\x01",
            "from Sunday School together\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "It's been a while, so I really want\x01",
            "to see Elissa too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AEC")

    Jump("loc_11F3")

    label("loc_AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_C67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C15")
    OP_A2(0x1)

    ChrTalk(    #16
        0xFE,
        (
            "Estelle and Joshua, thanks for\x01",
            "helping us out earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "Things have been pretty peaceful\x01",
            "around here since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Now that we're back to shipping\x01",
            "vegetables, we're overloaded with\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "I wonder if Chere and Will will be\x01",
            "able to help out with the work\x01",
            "soon...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C64")

    label("loc_C15")


    ChrTalk(    #20
        0xFE,
        (
            "I wonder if Chere and Will will be\x01",
            "able to help out with the work\x01",
            "soon...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C64")

    Jump("loc_11F3")

    label("loc_C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_DA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D30")
    OP_A2(0x1)

    ChrTalk(    #21
        0xFE,
        "I really want to thank you both!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Next time you come up here,\x01",
            "try to do it when you're free\x01",
            "from work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "Chere and Will won't stop asking\x01",
            "when you'll come visit again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA0")

    label("loc_D30")


    ChrTalk(    #24
        0xFE,
        "I really want to thank you both!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "Next time you come up here,\x01",
            "try to do it when you're free\x01",
            "from work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA0")

    Jump("loc_11F3")

    label("loc_DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1192")
    EventBegin(0x0)
    OP_A2(0x22E)
    OP_28(0x2, 0x1, 0x4)
    ClearMapFlags(0x1)
    OP_51(0x13, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x13, 0x3E8)

    ChrTalk(    #26
        0x101,
        "#001FHi, Tio!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        "#010FIt's been a while, hasn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "Estelle? And Joshua, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "Did you guys come for a visit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#000FNot exactly. We're here on bracer\x01",
            "business.\x02\x03",

            "#000FWe heard that you've been having\x01",
            "some trouble with monsters.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #31
        (
            "\x07\x05Estelle and Joshua explain that they are here to do their father's work\x01",
            "because he is away.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #32
        0xFE,
        (
            "You've finished all your training?\x01",
            "That's wonderful news! \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "Maybe you can help after all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#004FSo there really are monsters giving\x01",
            "you trouble, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Regrettably, that's been the case\x01",
            "the past several days now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Thanks to which, I'm suffering from\x01",
            "a lack of sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x102,
        (
            "#010FWhich means...the monsters only\x01",
            "come out at night?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "You're very perceptive, Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "It'd be better if you got all the\x01",
            "details from my father, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "I imagine he should be back from\x01",
            "delivering the milk and vegetables\x01",
            "any time now.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_11F3")

    label("loc_1192")


    ChrTalk(    #41
        0xFE,
        (
            "My father is out delivering\x01",
            "vegetables.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "I'm sure he'll be getting back any\x01",
            "minute now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F3")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    # Function_11_750 end

    def Function_12_11F9(): pass

    label("Function_12_11F9")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_12D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_128E")
    OP_A2(0x2)

    ChrTalk(    #43
        0xFE,
        (
            "Chere has started helping around\x01",
            "the farm, so I'm really bored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "Maybe I should try helping out on\x01",
            "the farm, too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D3")

    label("loc_128E")


    ChrTalk(    #45
        0xFE,
        (
            "Chere has started helping around\x01",
            "the farm, so I'm really bored.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D3")

    Jump("loc_17FA")

    label("loc_12D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_13CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1376")
    OP_A2(0x2)

    ChrTalk(    #46
        0xFE,
        "Joshua and Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Hey, guys, aren't you two bracers\x01",
            "who defend justice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "That's so awesome! I wonder if\x01",
            "I can be one, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13CA")

    label("loc_1376")


    ChrTalk(    #49
        0xFE,
        (
            "Aren't you two bracers who\x01",
            "defend justice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "I wonder if I can be one, too.\x02",
    )

    CloseMessageWindow()

    label("loc_13CA")

    Jump("loc_17FA")

    label("loc_13CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_14DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1490")
    OP_A2(0x2)

    ChrTalk(    #51
        0xFE,
        (
            "Aww, I wish I had an older brother\x01",
            "like you, Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Tio's so busy with work that she\x01",
            "never has time to play with me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "All Chere wants to do is play\x01",
            "house...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D8")

    label("loc_1490")


    ChrTalk(    #54
        0xFE,
        (
            "Tio's so busy with work that she\x01",
            "never has time to play with me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D8")

    Jump("loc_17FA")

    label("loc_14DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1529")
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #55
        0xFE,
        (
            "Come back and visit again,\x01",
            "Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "For sure, okay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_17FA")

    label("loc_1529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_17FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1658")
    OP_A2(0x283)
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #57
        0xFE,
        "It's Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "Did you come to play with me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        (
            "#010FI wish I had the time, but I'm afraid\x01",
            "today I'm here for work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "Work...?\x01",
            "That's no fun if we can't play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x102,
        "#011FHa ha. Maybe later if there's time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#000FThe kids here really like you,\x01",
            "Joshua.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16AF")

    label("loc_1658")

    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #63
        0xFE,
        (
            "Joshua, don't forget to play with\x01",
            "me if there's time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "For sure, okay?\x02",
    )

    CloseMessageWindow()

    label("loc_16AF")

    Jump("loc_17FA")

    label("loc_16B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 3)), scpexpr(EXPR_END)), "loc_16E5")
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #65
        0xFE,
        (
            "Come on, Joshua.\x01",
            "Let's play.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17FA")

    label("loc_16E5")

    OP_A2(0x283)
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #66
        0xFE,
        "It's Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "Did you come to play with me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x102,
        (
            "#010FI wish I had the time, but I'm afraid\x01",
            "today I'm here for work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "Work...?\x01",
            "That's no fun if we can't play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x102,
        "#011FHa ha. Maybe later if there's time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#000FThe kids here really like you,\x01",
            "Joshua.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17FA")

    TalkEnd(0x9)
    Return()

    # Function_12_11F9 end

    def Function_13_17FE(): pass

    label("Function_13_17FE")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_19C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1962")
    OP_A2(0x2B6)
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(    #72
        0xFE,
        (
            "Are you going somewhere...\x01",
            "Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x102,
        (
            "#010FYeah. It seems I'm headed to the\x01",
            "Bose region next door.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "Will you be back soon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x102,
        (
            "#010FUmm, it probably won't be any\x01",
            "time soon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "Umm, Joshua...? I'll be waiting\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "So will you come and play with\x01",
            "us again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x102,
        "#019FYeah. I promise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "Yay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_19C3")

    label("loc_1962")


    ChrTalk(    #81
        0xFE,
        (
            "Umm, Joshua...? I'll be waiting\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "So please don't forget to come\x01",
            "back and play.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19C3")

    Jump("loc_1D5D")

    label("loc_19C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1B04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ACD")
    OP_A2(0x3)
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(    #83
        0xFE,
        "Umm, Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "I'm going to start helping around\x01",
            "on the farm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x102,
        (
            "#010FReally? That's great!\x02\x03",

            "You work hard, okay?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #86
        "\x07\x05Joshua pats Chere softly on the head.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #87
        0xFE,
        (
            "I will! Teehee.\x01",
            "I promise to work hard!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B01")

    label("loc_1ACD")


    ChrTalk(    #88
        0xFE,
        (
            "I'm going to start helping around\x01",
            "on the farm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B01")

    Jump("loc_1D5D")

    label("loc_1B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1D5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_1C25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 2)), scpexpr(EXPR_END)), "loc_1B77")
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(    #89
        0xFE,
        (
            "Oh, Joshua... Umm... Mom and Dad\x01",
            "came home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "I think they're in the house.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C22")

    label("loc_1B77")

    OP_A2(0x282)

    ChrTalk(    #91
        0xFE,
        "Oh...Joshua, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        (
            "#000FHi, Chere!\x01",
            "How have you been?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(    #93
        0x102,
        "#010FAre your mom and dad home?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "Yep, they came home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "They're inside right now.\x02",
    )

    CloseMessageWindow()

    label("loc_1C22")

    Jump("loc_1D5D")

    label("loc_1C25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 2)), scpexpr(EXPR_END)), "loc_1C87")

    ChrTalk(    #96
        0xFE,
        "They're not home right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "Tio's outside if you want to talk\x01",
            "to her, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D5D")

    label("loc_1C87")

    OP_A2(0x282)

    ChrTalk(    #98
        0xFE,
        "Oh...Joshua, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#000FHi, Chere!\x01",
            "How have you been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x102,
        (
            "#010FDo you know where your mom\x01",
            "and dad are?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(    #101
        0xFE,
        "They're not home right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "Tio's outside if you want to talk\x01",
            "to her though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D5D")

    TalkEnd(0xA)
    Return()

    # Function_13_17FE end

    def Function_14_1D61(): pass

    label("Function_14_1D61")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1EFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E67")
    OP_A2(0x5)

    ChrTalk(    #103
        0xFE,
        (
            "After the airliners were built,\x01",
            "we started receiving orders\x01",
            "from various regions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "But we're having trouble just\x01",
            "keeping on top of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "I'm overjoyed as far as business\x01",
            "goes, but I need to figure a way\x01",
            "to deal with things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF9")

    label("loc_1E67")


    ChrTalk(    #106
        0xFE,
        (
            "After the airliners were built,\x01",
            "we started receiving orders\x01",
            "from various regions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "But we're having trouble just\x01",
            "keeping on top of them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EF9")

    Jump("loc_2398")

    label("loc_1EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_208C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FFE")
    OP_A2(0x5)

    ChrTalk(    #108
        0xFE,
        "Oh, hello, you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "I heard some talk about the both\x01",
            "of you while I was in town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "It looks like you've already made\x01",
            "a name for yourselves as bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "And now I get to boast to others\x01",
            "about how you protected my fields.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2089")

    label("loc_1FFE")


    ChrTalk(    #112
        0xFE,
        (
            "I heard some talk about the both\x01",
            "of you while I was in town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "And now I get to boast to others\x01",
            "about how you protected my fields.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2089")

    Jump("loc_2398")

    label("loc_208C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_2225")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2190")
    OP_A2(0x5)

    ChrTalk(    #114
        0xFE,
        "Oh, hello, you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "Ever since you drove those monsters\x01",
            "away, I've seen neither hide nor hair\x01",
            "of one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "I'm relieved that I can get back to\x01",
            "shipping vegetables like before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "It's all thanks to you.\x01",
            "I'm extremely grateful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2222")

    label("loc_2190")


    ChrTalk(    #118
        0xFE,
        (
            "Thanks to you two, I haven't seen\x01",
            "those pudgy little devils since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "I'm relieved that I can get back to\x01",
            "shipping vegetables like before.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2222")

    Jump("loc_2398")

    label("loc_2225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_2398")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_230A")
    OP_A2(0x5)

    ChrTalk(    #120
        0xFE,
        (
            "You've been a really big help.\x01",
            "Now we can get back to shipping\x01",
            "vegetables like before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "There are lots of people waiting\x01",
            "for our produce.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "We'd better get to work so\x01",
            "they can get what they need!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2398")

    label("loc_230A")


    ChrTalk(    #123
        0xFE,
        (
            "You've been a really big help.\x01",
            "Now we can get back to shipping\x01",
            "vegetables like before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "I really appreciate what you've\x01",
            "done for us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2398")

    TalkEnd(0xB)
    Return()

    # Function_14_1D61 end

    def Function_15_239C(): pass

    label("Function_15_239C")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_24EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247C")
    TurnDirection(0xFE, 0x101, 0)
    OP_A2(0x4)

    ChrTalk(    #125
        0xFE,
        (
            "Well, if it isn't Estelle and Joshua!\x01",
            "So are you here on business for\x01",
            "the guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "The work of a bracer can't be easy,\x01",
            "that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "Don't overdo things.\x01",
            "Moderation is the key.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24E7")

    label("loc_247C")


    ChrTalk(    #128
        0xFE,
        (
            "The work of a bracer can't be easy,\x01",
            "that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "Don't overdo things.\x01",
            "Moderation is the key.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24E7")

    Jump("loc_257C")

    label("loc_24EA")


    ChrTalk(    #130
        0xFE,
        (
            "Oh my, Estelle and Joshua.\x01",
            "How have the both of you been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "Come and visit us again when you've\x01",
            "got time. The kids would love to see\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_257C")

    TalkEnd(0xC)
    Return()

    # Function_15_239C end

    def Function_16_2580(): pass

    label("Function_16_2580")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrPos(0x101, 23380, 0, 61450, 0)
    SetChrPos(0x102, 24610, 0, 61450, 0)
    OP_6D(44190, 0, 16580, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3830, 0)
    OP_6C(269000, 0)
    OP_6E(261, 0)
    FadeToBright(2000, 0)

    def lambda_25F5():
        OP_6C(0, 12000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_25F5)
    OP_6D(22290, 0, 23280, 6000)

    def lambda_2616():
        OP_6D(24020, 0, 51850, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2616)
    Sleep(3000)

    def lambda_2633():
        OP_8E(0xFE, 0x5CF8, 0x3C, 0xC62A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2633)
    Sleep(500)

    def lambda_2653():
        OP_8E(0xFE, 0x60B8, 0xA0, 0xC8D2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2653)
    Sleep(3600)
    Fade(1000)
    OP_6D(24140, 30, 50930, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(1000)

    ChrTalk(    #132
        0x101,
        (
            "#501F*sigh* No matter when we come here,\x01",
            "this place is always so tranquil.\x02\x03",

            "#501FIt's hard to imagine monsters\x01",
            "running amok here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x102,
        (
            "#010FI certainly don't sense anything\x01",
            "out of the ordinary either...\x02\x03",

            "#010FAnyway, let's go ask someone\x01",
            "here to fill us in on the details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        "#000FI wonder if Tio is home today...\x02",
    )

    CloseMessageWindow()
    OP_44(0x0, 0xFF)
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    Return()

    # Function_16_2580 end

    def Function_17_2803(): pass

    label("Function_17_2803")

    OP_A6(0x0)
    OP_6B(4370, 6000)
    OP_A3(0x0)
    Return()

    # Function_17_2803 end

    def Function_18_2813(): pass

    label("Function_18_2813")

    EventBegin(0x0)
    SetMapFlags(0x400000)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8)
    SetChrPos(0xB, 23950, 20, 50260, 0)
    SetChrPos(0xC, 25400, 310, 50280, 0)
    SetChrPos(0x8, 23110, 280, 51210, 45)
    SetChrPos(0x9, 24740, 150, 51220, 0)
    SetChrPos(0xA, 25710, 360, 51250, 0)
    SetChrPos(0x101, 23600, 130, 52840, 180)
    SetChrPos(0x102, 24780, 160, 53490, 180)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_6D(23970, 130, 51650, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    OP_22(0xD, 0x0, 0x64)
    Sleep(5000)
    OP_1E()
    FadeToBright(2000, 0)
    Sleep(1000)

    ChrTalk(    #135
        0xB,
        (
            "Thank you both.\x01",
            "You did us all a great service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xB,
        (
            "Once again, I apologize for things\x01",
            "not turning out the way they should\x01",
            "have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x102,
        (
            "#010FPlease don't worry about it anymore.\x01",
            "We were able to learn a lot from this\x01",
            "experience ourselves.\x02\x03",

            "#010FIf there's anything else we can\x01",
            "help you with in the future,\x01",
            "please let the Bracer Guild know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xB,
        (
            "That'll definitely be the first place\x01",
            "we contact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x8,
        (
            "Come and visit again sometime when\x01",
            "you're free, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xC,
        (
            "We'd love to have you over for the night again\x01",
            "when things are convenient for you. I'll treat you\x01",
            "to some of my best cooking next time you come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#001FThanks for the invitation,\x01",
            "Tio and Mrs. Perzel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x102,
        (
            "#019FWe'll definitely be back to take\x01",
            "you up on that when our work\x01",
            "load settles down.\x02",
        )
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT01/R0201   ._SN", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_2813 end

    def Function_19_2C59(): pass

    label("Function_19_2C59")

    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0x5D52, 0x0, 0xF28A, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_19_2C59 end

    def Function_20_2C7F(): pass

    label("Function_20_2C7F")

    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0x5D52, 0x0, 0xF28A, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_2C7F end

    SaveToFile()

Try(main)
