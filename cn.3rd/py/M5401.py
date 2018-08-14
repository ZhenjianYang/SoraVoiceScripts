from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5401   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5401.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60234",
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
        '怪盗布卢布兰',                         # 9
        '瘦狼瓦鲁特',                           # 10
        '幻惑之铃露茜奥拉',                     # 11
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH03530 ._CH',             # 00
        'ED6_DT27/CH03500 ._CH',             # 01
        'ED6_DT27/CH03520 ._CH',             # 02
        'ED6_DT27/CH04530 ._CH',             # 03
        'ED6_DT27/CH04500 ._CH',             # 04
        'ED6_DT27/CH04520 ._CH',             # 05
        'ED6_DT26/CH20273 ._CH',             # 06
        'ED6_DT26/CH20242 ._CH',             # 07
        'ED6_DT27/CH04521 ._CH',             # 08
        'ED6_DT26/CH20280 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT27/CH03530P._CP',             # 00
        'ED6_DT27/CH03500P._CP',             # 01
        'ED6_DT27/CH03520P._CP',             # 02
        'ED6_DT27/CH04530P._CP',             # 03
        'ED6_DT27/CH04500P._CP',             # 04
        'ED6_DT27/CH04520P._CP',             # 05
        'ED6_DT26/CH20273P._CP',             # 06
        'ED6_DT26/CH20242P._CP',             # 07
        'ED6_DT27/CH04521P._CP',             # 08
        'ED6_DT26/CH20280P._CP',             # 09
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -1110,
        TriggerZ            = 1500,
        TriggerY            = 87020,
        TriggerRange        = 1000,
        ActorX              = -1500,
        ActorZ              = 4500,
        ActorY              = 87500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_17E",          # 00, 0
        "Function_1_1F2",          # 01, 1
        "Function_2_270",          # 02, 2
        "Function_3_279",          # 03, 3
        "Function_4_2076",         # 04, 4
        "Function_5_36E0",         # 05, 5
        "Function_6_379F",         # 06, 6
        "Function_7_39B5",         # 07, 7
        "Function_8_4258",         # 08, 8
        "Function_9_4336",         # 09, 9
        "Function_10_4408",        # 0A, 10
        "Function_11_451E",        # 0B, 11
        "Function_12_456C",        # 0C, 12
        "Function_13_476B",        # 0D, 13
        "Function_14_47DF",        # 0E, 14
        "Function_15_49B5",        # 0F, 15
        "Function_16_4A6E",        # 10, 16
    )


    def Function_0_17E(): pass

    label("Function_0_17E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19D")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_196"),
        (SWITCH_DEFAULT, "loc_19D"),
    )


    label("loc_196")

    Event(0, 8)
    Jump("loc_19D")

    label("loc_19D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_1C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DE")
    Event(0, 7)

    label("loc_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1F1")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 16)

    label("loc_1F1")

    Return()

    # Function_0_17E end

    def Function_1_1F2(): pass

    label("Function_1_1F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 7)), scpexpr(EXPR_END)), "loc_21B")
    OP_10(0x1, 0x0)
    OP_72(0x406, 0x0)
    ExitThread()
    OP_82(0x81, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x12, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_215")
    OP_82(0x82, 0x0)
    Jump("loc_218")

    label("loc_215")

    OP_82(0x83, 0x0)

    label("loc_218")

    Jump("loc_26F")

    label("loc_21B")

    OP_71(0x406, 0x0)
    ExitThread()
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_64(0x0, 0x1)
    OP_1B(0x1, 0x0, 0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 1)), scpexpr(EXPR_END)), "loc_26F")
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_26F")

    Return()

    # Function_1_1F2 end

    def Function_2_270(): pass

    label("Function_2_270")

    Call(0, 3)
    Call(0, 4)
    Return()

    # Function_2_270 end

    def Function_3_279(): pass

    label("Function_3_279")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(238, 0x4A, 0x2)
    OP_E0(238, 0x4B, 0x3)
    OP_E0(239, 0x4C, 0x2)
    OP_E0(239, 0x4D, 0x3)
    OP_E0(240, 0x4E, 0x2)
    OP_E0(240, 0x4F, 0x3)
    OP_E0(241, 0x50, 0x2)
    OP_E0(241, 0x51, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -880, 970, 81900, 180)
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 690, 1500, 83150, 180)
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -2590, 1480, 82880, 180)
    SetChrPos(0x109, -1760, 0, 40080, 0)
    OP_1F(0x50, 0x12C)
    Sleep(300)
    OP_1F(0x5A, 0x12C)
    Sleep(300)
    OP_1F(0x64, 0x12C)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_376")
    SetChrPos(0xEF, -350, 0, 39700, 0)
    SetChrPos(0xF0, -1560, 0, 38360, 0)
    SetChrPos(0xF1, 60, 0, 37520, 0)
    Jump("loc_3FB")

    label("loc_376")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BA")
    SetChrPos(0xF0, -350, 0, 39700, 0)
    SetChrPos(0xEF, -1560, 0, 38360, 0)
    SetChrPos(0xF1, 60, 0, 37520, 0)
    Jump("loc_3FB")

    label("loc_3BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FB")
    SetChrPos(0xF1, -350, 0, 39700, 0)
    SetChrPos(0xEF, -1560, 0, 38360, 0)
    SetChrPos(0xF0, 60, 0, 37520, 0)

    label("loc_3FB")

    OP_6D(2940, -4750, 52390, 0)
    OP_67(0, 10050, -10000, 0)
    OP_6B(4090, 0)
    OP_6C(44000, 0)
    OP_6E(447, 0)

    def lambda_43E():
        OP_8F(0xFE, 0xFFFFF93E, 0x0, 0xBDEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_43E)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BA")

    def lambda_467():
        OP_8F(0xFE, 0xFFFFFF06, 0x0, 0xBE82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_467)
    Sleep(100)

    def lambda_487():
        OP_8F(0xFE, 0xFFFFF984, 0x0, 0xB842, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_487)

    def lambda_4A2():
        OP_8F(0xFE, 0x14, 0x0, 0xB8E2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_4A2)
    Jump("loc_585")

    label("loc_4BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_521")

    def lambda_4CE():
        OP_8F(0xFE, 0xFFFFFF06, 0x0, 0xBE82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_4CE)
    Sleep(100)

    def lambda_4EE():
        OP_8F(0xFE, 0xFFFFF984, 0x0, 0xB842, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_4EE)

    def lambda_509():
        OP_8F(0xFE, 0x14, 0x0, 0xB8E2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_509)
    Jump("loc_585")

    label("loc_521")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_585")

    def lambda_535():
        OP_8F(0xFE, 0xFFFFFF06, 0x0, 0xBE82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_535)
    Sleep(100)

    def lambda_555():
        OP_8F(0xFE, 0xFFFFF984, 0x0, 0xB842, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_555)

    def lambda_570():
        OP_8F(0xFE, 0x14, 0x0, 0xB8E2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_570)

    label("loc_585")


    def lambda_58B():
        OP_6D(2940, -4750, 57390, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_58B)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1500)
    Fade(500)
    OP_44(0xEE, 0x3)
    OP_6D(-180, 0, 47050, 0)
    OP_67(0, 7090, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(141000, 0)
    OP_6E(256, 0)
    WaitChrThread(0xEE, 0x0)
    OP_0D()
    Sleep(500)
    OP_20(0x7D0)

    NpcTalk(    #0
        0x10,
        "男子的声音",
        (
            "#2P呵呵……\x01",
            "终于来到这里了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65E")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6C5")

    label("loc_65E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_686")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6C5")

    label("loc_686")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AE")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6C5")

    label("loc_6AE")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6C5")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F2")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_759")

    label("loc_6F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71A")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_759")

    label("loc_71A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_742")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_759")

    label("loc_742")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_759")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_786")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7ED")

    label("loc_786")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AE")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7ED")

    label("loc_7AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D6")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7ED")

    label("loc_7D6")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_7ED")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81A")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_881")

    label("loc_81A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_842")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_881")

    label("loc_842")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86A")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_881")

    label("loc_86A")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_881")

    Sleep(1000)
    OP_1D(0x6F)
    Fade(500)
    OP_6D(-900, 0, 56000, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3450, 0)
    OP_6C(0, 0)
    OP_6E(337, 0)
    SetChrPos(0x109, -1510, 0, 50360, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91F")
    SetChrPos(0xEF, -260, 0, 50300, 0)
    SetChrPos(0xF0, -1930, 0, 48960, 0)
    SetChrPos(0xF1, 210, 0, 49040, 0)
    Jump("loc_9A4")

    label("loc_91F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_963")
    SetChrPos(0xF0, -260, 0, 50300, 0)
    SetChrPos(0xEF, -1930, 0, 48960, 0)
    SetChrPos(0xF1, 210, 0, 49040, 0)
    Jump("loc_9A4")

    label("loc_963")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A4")
    SetChrPos(0xF1, -260, 0, 50300, 0)
    SetChrPos(0xEF, -1930, 0, 48960, 0)
    SetChrPos(0xF0, 210, 0, 49040, 0)

    label("loc_9A4")


    def lambda_9AA():
        OP_6D(-900, 1500, 84630, 4500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_9AA)

    def lambda_9C2():
        OP_67(0, 2500, -10000, 4500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_9C2)

    def lambda_9DA():
        OP_6B(2850, 4500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_9DA)

    def lambda_9EA():
        OP_6C(0, 4500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_9EA)

    def lambda_9FA():
        OP_6E(290, 4500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_9FA)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #1
        0x10,
        (
            "#231F#5P哈哈，真是有缘啊。\x02\x03",

            "没想到竟能以这种形式\x01",
            "与诸位重逢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x11,
        (
            "#252F#5P哼哼……我真开心。\x02\x03",

            "没想到你们居然\x01",
            "能大摇大摆来到这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x12,
        (
            "#240F#5P呵呵……\x01",
            "该说好久不见吗。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(1860, 470, 80620, 0)
    OP_67(0, 4120, -10000, 0)
    OP_6B(4290, 0)
    OP_6C(45000, 0)
    OP_6E(292, 0)
    OP_71(0x404, 0x0)
    ExitThread()
    OP_79(0x9, 0x2)
    OP_7B()
    SetChrPos(0x109, -1740, 0, 66100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B87")
    SetChrPos(0xEF, -400, 0, 65710, 0)
    SetChrPos(0xF0, -1720, 0, 64430, 0)
    SetChrPos(0xF1, -150, 0, 64069, 0)
    Jump("loc_C0C")

    label("loc_B87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCB")
    SetChrPos(0xF0, -400, 0, 65710, 0)
    SetChrPos(0xEF, -1720, 0, 64430, 0)
    SetChrPos(0xF1, -150, 0, 64069, 0)
    Jump("loc_C0C")

    label("loc_BCB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0C")
    SetChrPos(0xF1, -400, 0, 65710, 0)
    SetChrPos(0xEF, -1720, 0, 64430, 0)
    SetChrPos(0xF0, -150, 0, 64069, 0)

    label("loc_C0C")


    def lambda_C12():
        OP_8F(0xFE, 0xFFFFF8BC, 0x0, 0x1207A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C12)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C98")

    def lambda_C40():
        OP_8F(0xFE, 0xFFFFFE7A, 0x0, 0x12084, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_C40)
    Sleep(100)

    def lambda_C60():
        OP_8F(0xFE, 0xFFFFF72C, 0x0, 0x1197C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_C60)
    Sleep(100)

    def lambda_C80():
        OP_8F(0xFE, 0xFFFFFE3E, 0x0, 0x119A4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_C80)
    Jump("loc_D6D")

    label("loc_C98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D04")

    def lambda_CAC():
        OP_8F(0xFE, 0xFFFFFE7A, 0x0, 0x12084, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_CAC)
    Sleep(100)

    def lambda_CCC():
        OP_8F(0xFE, 0xFFFFF72C, 0x0, 0x1197C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_CCC)
    Sleep(100)

    def lambda_CEC():
        OP_8F(0xFE, 0xFFFFFE3E, 0x0, 0x119A4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_CEC)
    Jump("loc_D6D")

    label("loc_D04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6D")

    def lambda_D18():
        OP_8F(0xFE, 0xFFFFFE7A, 0x0, 0x12084, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_D18)
    Sleep(100)

    def lambda_D38():
        OP_8F(0xFE, 0xFFFFF72C, 0x0, 0x1197C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_D38)
    Sleep(100)

    def lambda_D58():
        OP_8F(0xFE, 0xFFFFFE3E, 0x0, 0x119A4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_D58)

    label("loc_D6D")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #4
        0x102,
        (
            "#1502F#11P果然……\x01",
            "是你们啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FAC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E4D")

    ChrTalk(    #5
        0x10,
        (
            "#230F#5P没想到能与我的公主和好对手\x01",
            "再次相见啊。\x02\x03",

            "#231F呵呵……\x01",
            "这也是女神的安排吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F30")

    label("loc_E4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EC1")

    ChrTalk(    #6
        0x10,
        (
            "#230F#5P没想到能与我美丽的公主\x01",
            "再次相见啊。\x02\x03",

            "#231F呵呵……\x01",
            "这也是女神的安排吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F30")

    label("loc_EC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F30")

    ChrTalk(    #7
        0x10,
        (
            "#230F#5P没想到能与我的好对手\x01",
            "再次相见啊。\x02\x03",

            "#231F呵呵……\x01",
            "这也是女神的安排吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F6E")

    ChrTalk(    #8
        0x105,
        (
            "#1382F#11P哎……\x01",
            "那个，好久不见呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FAC")

    ChrTalk(    #9
        0x104,
        (
            "#1541F#11P呼……\x01",
            "看来还是老样子呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1057")

    ChrTalk(    #10
        0x103,
        "#1523F#11P露、露茜奥拉姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x12,
        (
            "#247F#5P呵呵……\x01",
            "本来以为\x01",
            "再也不会见面了。\x02\x03",

            "#240F命运偶尔\x01",
            "也会做这种巧妙的安排呢。\x02",
        )
    )

    Jump("loc_1056")

    label("loc_1056")

    CloseMessageWindow()

    label("loc_1057")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10DC")

    ChrTalk(    #12
        0x108,
        "#072F#11P瓦鲁特……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x11,
        (
            "#253F哼哼，\x01",
            "又在奇怪的地方碰头了嘛。\x02\x03",

            "看来还能再次\x01",
            "尽情比试比试呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1247")
    Sleep(500)

    ChrTalk(    #14
        0x110,
        (
            "#263F#11P嘻嘻……\x01",
            "和你们三人决胜负吗。\x02\x03",

            "#1306F玲觉得\x01",
            "好兴奋哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "#230F#5P呵呵……\x01",
            "这应该是我们的台词啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x12,
        (
            "#247F#5P『漆黑之牙』加上\x01",
            "『歼灭天使』作对手……\x02\x03",

            "#241F这可有点棘手呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        (
            "#252F#5P哈哈……\x01",
            "不过，这样更好。\x02\x03",

            "看来可以尽情享受血的滋味了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x110,
        "#261F#11P嘻嘻……同感。\x02",
    )

    CloseMessageWindow()

    label("loc_1247")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B0")
    Sleep(500)

    ChrTalk(    #19
        0x101,
        (
            "#1007F#11P唉，\x01",
            "竟然要和这三个人一起对战……\x02\x03",

            "#1019F实在是觉得\x01",
            "有点犯规的样子啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        (
            "#231F#5P呵呵，说什么呢。\x01",
            "艾丝蒂尔·布莱特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x12,
        (
            "#247F#5P你经过那件事之后，\x01",
            "应该也达到了更高的层次。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        (
            "#253F#5P好久没比试了……\x01",
            "让我好好享受一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1016F#11P啊、啊哈哈……\x01",
            "好像受到不情愿的期待了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13B0")

    Sleep(500)

    ChrTalk(    #24
        0x109,
        (
            "#1841F#6P呼……\x01",
            "看来已经逃不掉了呢。\x02\x03",

            "#1840F虽然说了也没用，\x01",
            "不过还是请手下留情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        (
            "#252F#5P哼哼……\x01",
            "玩笑就到此为止吧。\x02\x03",

            "我们早就抓到证据了。\x01",
            "你这油嘴滑舌的家伙。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #26
        0x109,
        "#1063F#6P……………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #27
        0x10,
        (
            "#232F#5P『异端制裁者』……\x01",
            "虽然之前听过传闻。\x02\x03",

            "#231F不过真没想到，\x01",
            "居然有本事毁灭那个『白面』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x12,
        (
            "#247F#5P呵呵……\x01",
            "骗过我们的手段真出色。\x02\x03",

            "#240F说实话，\x01",
            "我丝毫没有给教授报仇的意思……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(1600, 1000, 84500, 0)
    OP_67(0, 4030, -10000, 0)
    OP_6B(3210, 0)
    OP_6C(45000, 0)
    OP_6E(263, 0)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)
    Sleep(50)
    OP_22(0x23B, 0x0, 0x64)
    SetChrChipByIndex(0x11, 4)
    SetChrSubChip(0x11, 0)
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x12, 5)
    SetChrSubChip(0x12, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #29
        0x10,
        (
            "#231F#5P不过被骗了\x01",
            "就要连同敬意一起偿还，\x01",
            "这是我的风格。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x11,
        (
            "#253F#5P哼哼哼……\x01",
            "就让我看看你的本性吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_6D(100, 0, 72000, 0)
    OP_67(0, 6140, -10000, 0)
    OP_6B(1980, 0)
    OP_6C(136000, 0)
    OP_6E(378, 0)
    OP_0D()
    Sleep(800)

    ChrTalk(    #31
        0x109,
        (
            "#1075F#11P呼……哎呀哎呀。\x02\x03",

            "#1073F不过也罢，\x01",
            "对你们似乎没有客气的必要。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 10)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #32
        0x109,
        (
            "#1065F#11P──我正式认定\x01",
            "你们为『异端』。\x02\x03",

            "#1072F如你们所愿……\x01",
            "让我制裁到底吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_18D2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_186D")

    ChrTalk(    #33
        0x101,
        "#1026F#11P凯、凯文先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10F,
        "#1802F#11P………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_18D2")

    label("loc_186D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18A5")

    ChrTalk(    #35
        0x101,
        "#1026F#11P凯、凯文先生……\x02",
    )

    CloseMessageWindow()
    Jump("loc_18D2")

    label("loc_18A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18D2")

    ChrTalk(    #36
        0x10F,
        "#1802F#11P凯文……\x02",
    )

    CloseMessageWindow()

    label("loc_18D2")


    ChrTalk(    #37
        0x10,
        (
            "#231F#2P哈哈，这才对！\x02\x03",

            "看来你和我们预期的一样，\x01",
            "是个不近人情的怪物。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #38
        0x10,
        "瘦狼瓦鲁特",
        (
            "#253F#2P漆黑小子……\x01",
            "你也要动真格的哦？\x02\x03",

            "如果不尽全力的话，\x01",
            "我可是会把你给撕成碎片。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x102,
        (
            "#1513F#11P……你的担心是多余的。\x02\x03",

            "#1514F从进入这里开始，\x01",
            "我就已下定决心了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    OP_22(0x1F5, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A27")
    SetChrChipByIndex(0x102, 12)
    SetChrSubChip(0x102, 0)
    Jump("loc_1A5A")

    label("loc_1A27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A42")
    SetChrChipByIndex(0x102, 14)
    SetChrSubChip(0x102, 0)
    Jump("loc_1A5A")

    label("loc_1A42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A5A")
    SetChrChipByIndex(0x102, 16)
    SetChrSubChip(0x102, 0)

    label("loc_1A5A")

    OP_0D()
    Sleep(500)

    ChrTalk(    #40
        0x102,
        (
            "#1502F#11P为了走到\x01",
            "在你们后面的『他』面前……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #41
        0x102,
        "#1506F#11P#4S我会全力应战的！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B47")

    ChrTalk(    #42
        0x110,
        "#1307F#11P约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1002F#11P…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BA8")

    label("loc_1B47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B79")

    ChrTalk(    #44
        0x101,
        "#1002F#11P约修亚……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BA8")

    label("loc_1B79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BA8")

    ChrTalk(    #45
        0x110,
        "#1307F#11P约修亚……\x02",
    )

    CloseMessageWindow()

    label("loc_1BA8")

    Sleep(150)
    Fade(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BE6")
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 14)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 16)
    SetChrSubChip(0xF1, 0)
    Jump("loc_1C4B")

    label("loc_1BE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C1A")
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 12)
    SetChrSubChip(0xEF, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 16)
    SetChrSubChip(0xF1, 0)
    Jump("loc_1C4B")

    label("loc_1C1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C4B")
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 12)
    SetChrSubChip(0xEF, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 14)
    SetChrSubChip(0xF0, 0)

    label("loc_1C4B")

    OP_0D()
    Sleep(500)
    Fade(1000)
    OP_6D(-950, 350, 84190, 0)
    OP_67(0, 2280, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(0, 0)
    OP_6E(311, 0)
    OP_72(0x404, 0x0)
    ExitThread()
    OP_7A(0x9, 0x2)
    OP_7B()
    SetChrPos(0x10, -880, 970, 81900, 180)
    SetChrPos(0x11, 690, 1500, 83300, 180)
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x800)
    SetChrPos(0x12, -2590, 1480, 82880, 180)
    SetChrPos(0x109, -1590, 0, 73840, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D36")
    SetChrPos(0xEF, -340, 0, 74010, 0)
    SetChrPos(0xF0, -2180, 0, 72230, 0)
    SetChrPos(0xF1, 170, 0, 72350, 0)
    Jump("loc_1DBB")

    label("loc_1D36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D7A")
    SetChrPos(0xF0, -340, 0, 74010, 0)
    SetChrPos(0xEF, -2180, 0, 72230, 0)
    SetChrPos(0xF1, 170, 0, 72350, 0)
    Jump("loc_1DBB")

    label("loc_1D7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DBB")
    SetChrPos(0xF1, -340, 0, 74010, 0)
    SetChrPos(0xEF, -2180, 0, 72230, 0)
    SetChrPos(0xF0, 170, 0, 72350, 0)

    label("loc_1DBB")

    OP_20(0x7D0)

    def lambda_1DC6():
        OP_6B(3310, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1DC6)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    OP_21()
    OP_1D(0x37)
    Sleep(1000)

    ChrTalk(    #46
        0x12,
        (
            "#247F#5P呵呵……\x02\x03",

            "#241F看来最棒的舞台\x01",
            "已经准备好了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x11,
        (
            "#252F#5P是啊……\x01",
            "我都兴奋得发抖了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10,
        "#230F#5P那么开始吧……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #49
        0x10,
        (
            "#234F#5P#3S梦幻的无限！#2S\x02\x03",

            "#3S永劫不复、\x01",
            "至高无上的狂欢节！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1EF5():
        OP_6D(-1000, 200, 84390, 250)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1EF5)

    def lambda_1F0D():
        OP_67(0, 2610, -10000, 250)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1F0D)

    def lambda_1F25():
        OP_6B(3100, 250)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1F25)

    def lambda_1F35():
        OP_6E(287, 250)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_1F35)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x10, 6)
    SetChrSubChip(0x10, 0)
    OP_7D(0x0, 0x10, 0x32, 0x1F4)

    def lambda_1F5C():
        OP_96(0xFE, 0xFFFFFC4A, 0x0, 0x127B4, 0x190, 0x157C)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1F5C)
    Sleep(30)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x11, 7)
    SetChrSubChip(0x11, 2)
    OP_7D(0x0, 0x11, 0x32, 0x1F4)

    def lambda_1F96():
        OP_96(0xFE, 0xFFFFFF56, 0x0, 0x12CBE, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1F96)
    Sleep(30)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x12, 8)
    SetChrSubChip(0x12, 3)
    OP_7D(0x0, 0x12, 0x32, 0x1F4)

    def lambda_1FD0():
        OP_96(0xFE, 0xFFFFF8C6, 0x0, 0x12CD2, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1FD0)

    def lambda_1FEE():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1FEE)

    def lambda_2009():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2009)

    def lambda_2024():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2024)

    def lambda_203F():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_203F)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x2AD, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_279 end

    def Function_4_2076(): pass

    label("Function_4_2076")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    Sleep(1000)
    OP_44(0xEE, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x10, 0x0)
    OP_44(0x12, 0x0)
    OP_7D(0x1, 0x11, 0x0, 0x0)
    OP_7D(0x1, 0x10, 0x0, 0x0)
    OP_7D(0x1, 0x12, 0x0, 0x0)
    LoadEffect(0x0, "map\\mp259_02.eff")
    LoadEffect(0x1, "map\\mp256_00.eff")
    OP_E0(238, 0x4A, 0x2)
    OP_E0(238, 0x4B, 0x3)
    OP_E0(239, 0x4C, 0x2)
    OP_E0(239, 0x4D, 0x3)
    OP_E0(240, 0x4E, 0x2)
    OP_E0(240, 0x4F, 0x3)
    OP_E0(241, 0x50, 0x2)
    OP_E0(241, 0x51, 0x3)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -1600, 1500, 83000, 180)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 760, 1500, 84340, 180)
    SetChrChipByIndex(0x11, 9)
    SetChrSubChip(0x11, 0)
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -2700, 1500, 84000, 180)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    OP_43(0x10, 0x3, 0x0, 0x5)
    OP_43(0x11, 0x3, 0x0, 0x5)
    OP_43(0x12, 0x3, 0x0, 0x5)
    OP_22(0x146, 0x1, 0x3C)
    PlayEffect(0x0, 0x0, 0x10, 100, 900, 100, 0, 0, 0, 2100, 3200, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x0, 0x2, 0x11, 200, 900, 100, 0, 0, 0, 2200, 3300, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x0, 0x4, 0x12, 150, 900, 100, 0, 0, 0, 2100, 3200, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x109, -1780, 0, 76900, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_229A")
    SetChrPos(0xEF, -300, 0, 76730, 0)
    SetChrPos(0xF0, -2190, 0, 75100, 0)
    SetChrPos(0xF1, -240, 0, 75030, 0)
    Jump("loc_231F")

    label("loc_229A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22DE")
    SetChrPos(0xF0, -300, 0, 76730, 0)
    SetChrPos(0xEF, -2190, 0, 75100, 0)
    SetChrPos(0xF1, -240, 0, 75030, 0)
    Jump("loc_231F")

    label("loc_22DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_231F")
    SetChrPos(0xF1, -300, 0, 76730, 0)
    SetChrPos(0xEF, -2190, 0, 75100, 0)
    SetChrPos(0xF0, -240, 0, 75030, 0)

    label("loc_231F")

    SetChrChipByIndex(0xEE, 10)
    SetChrChipByIndex(0xEF, 12)
    SetChrChipByIndex(0xF0, 14)
    SetChrChipByIndex(0xF1, 16)
    SetChrSubChip(0xEE, 0)
    SetChrSubChip(0xEF, 0)
    SetChrSubChip(0xF0, 0)
    SetChrSubChip(0xF1, 0)
    OP_71(0x404, 0x0)
    ExitThread()
    OP_79(0x9, 0x2)
    OP_7B()
    OP_6D(190, 960, 81840, 0)
    OP_67(0, 3120, -10000, 0)
    OP_6B(4250, 0)
    OP_6C(34000, 0)
    OP_6E(292, 0)
    OP_1D(0xAD)
    FadeToBright(1500, 0)
    OP_6B(4050, 1500)
    OP_0D()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #50
        0x11,
        (
            "#254F#5P#40W啧……\x01",
            "太小看人了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x12,
        (
            "#247F#5P#40W呵呵……\x01",
            "不过是场不错的比试。\x02\x03",

            "#240F如果能再继续一会儿\x01",
            "就好了，是吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24A9")

    ChrTalk(    #52
        0x101,
        "#1007F#12P开、开玩笑吧……\x02",
    )

    CloseMessageWindow()

    label("loc_24A9")


    ChrTalk(    #53
        0x102,
        (
            "#1514F#12P……那还是\x01",
            "免了吧。\x02",
        )
    )

    Jump("loc_24DE")

    label("loc_24DE")

    CloseMessageWindow()

    ChrTalk(    #54
        0x109,
        "#1068F#6P是啊……的确如此。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2548")

    ChrTalk(    #55
        0x110,
        (
            "#261F#12P哎呀，\x01",
            "玲倒是还想再玩一会儿。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2548")


    ChrTalk(    #56
        0x10,
        (
            "#232F#5P#40W好了，\x01",
            "既然已经打退了我们，\x01",
            "诸位获得了挑战第四『守护者』的资格。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x12,
        (
            "#244F#5P#40W『影之王』所挑选的\x01",
            "第一个也是最后一个『守护者』。\x02\x03",

            "#240F恐怕将是阻挡在你们面前\x01",
            "最大的障壁吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x11,
        (
            "#257F#5P#40W话说回来\x01",
            "你们可是打败了我们三人的。\x02\x03",

            "#253F要是表现得太丢脸……我可杀了你们哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        "#1513F#12P啊啊……知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x109,
        (
            "#1066F#6P嗯，\x01",
            "我们会好好努力的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_287A")
    Sleep(500)

    ChrTalk(    #61
        0x103,
        (
            "#1532F#12P……露茜奥拉姐姐……\x02\x03",

            "那个……\x01",
            "……现在姐姐还……\x02",
        )
    )

    Jump("loc_274D")

    label("loc_274D")

    CloseMessageWindow()

    ChrTalk(    #62
        0x12,
        (
            "#244F#5P#40W呵呵，\x01",
            "真正的我是生是死……\x02\x03",

            "#240F身为假货,\x01",
            "我可无法给出任何答案哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x103,
        "#1525F#12P……是吗………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x12,
        (
            "#247F#5P#40W这答案等你回去之后\x01",
            "自己去寻找吧。\x02\x03",

            "#241F还有……那发型和服装，\x01",
            "很适合你哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x103,
        (
            "#1523F#12P啊……\x02\x03",

            "#1521F呵呵，谢谢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_287A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_298D")
    Sleep(500)

    ChrTalk(    #66
        0x108,
        (
            "#074F#4P瓦鲁特……\x01",
            "关于雾香的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x11,
        (
            "#251F#5P#30W啊啊，我听说了。\x02\x03",

            "是被卡尔瓦德的情报机构\x01",
            "挖角了吧。\x02\x03",

            "#257F金，去跟那家伙说。\x02\x03",

            "#253F太过逞强的话\x01",
            "会变成老姑娘的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x108,
        (
            "#070F#4P哈哈……\x01",
            "知道了，我会转达的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_298D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BAF")
    Sleep(500)

    ChrTalk(    #69
        0x110,
        (
            "#267F#12P你们三个……\x01",
            "要走了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x10,
        (
            "#230F#5P#40W呵呵，真是依依不舍啊。\x02\x03",

            "你呢，\x01",
            "打算什么时候回『结社』呢？\x02",
        )
    )

    Jump("loc_2A2E")

    label("loc_2A2E")

    CloseMessageWindow()

    ChrTalk(    #71
        0x110,
        "#1300F#12P………这个……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x12,
        (
            "#247F#5P#40W呵呵……\x01",
            "想通之前就尽情迷惘吧。\x02\x03",

            "#240F我们是『执行者』。\x02\x03",

            "『使徒』无法限制\x01",
            "我们的行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x11,
        (
            "#252F#5P#40W如果成为敌人，\x01",
            "就再让我好好开心一下吧。\x02\x03",

            "#257F要是回来了……\x01",
            "嗯，到时就陪你练习吧。\x02\x03",

            "#251F如果是你，\x01",
            "很快就能学会那种『寸劲』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x110,
        (
            "#261F#12P嘻嘻……\x01",
            "让我考虑考虑吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BAF")

    Sleep(500)

    ChrTalk(    #75
        0x10,
        (
            "#230F#5P#40W好了……\x01",
            "差不多到时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x12,
        (
            "#247F#5P#40W那么各位……\x01",
            "今宵的舞台就到此结束。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x11,
        (
            "#252F#5P#40W哼哼……\x01",
            "那么，再见了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(140, 1500, 85730, 0)
    OP_67(0, 4090, -10000, 0)
    OP_6B(2330, 0)
    OP_6C(33000, 0)
    OP_6E(396, 0)

    def lambda_2C9F():
        OP_6B(2150, 5000)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_2C9F)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x10, 200, -1000, 300, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x3, 0x11, 200, -1000, 300, 0, 0, 0, 2600, 2600, 2600, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x5, 0x12, 200, -1000, 300, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_23(0x146)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_44(0x10, 0x3)
    OP_44(0x11, 0x3)
    OP_44(0x12, 0x3)

    def lambda_2D86():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2D86)

    def lambda_2D98():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2D98)

    def lambda_2DAA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2DAA)
    Sleep(800)
    Fade(1000)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_82(0x5, 0x0)
    OP_0D()
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Sleep(1000)
    OP_44(0xF1, 0x3)

    def lambda_2DF1():
        OP_6D(-1000, 3050, 84700, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2DF1)

    def lambda_2E09():
        OP_67(0, 9000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2E09)

    def lambda_2E21():
        OP_6B(3380, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2E21)

    def lambda_2E31():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_2E31)

    def lambda_2E41():
        OP_6E(208, 4000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2E41)
    WaitChrThread(0xEE, 0x0)
    Fade(1000)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xEE, 0x0)
    OP_0D()
    Sleep(500)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2ECB")

    ChrTalk(    #78
        0x110,
        "#264F#5P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30DF")

    label("loc_2ECB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EF8")

    ChrTalk(    #79
        0x101,
        "#1004F#5P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30DF")

    label("loc_2EF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F25")

    ChrTalk(    #80
        0x103,
        "#1523F#5P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30DF")

    label("loc_2F25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F51")

    ChrTalk(    #81
        0x108,
        "#073F#5P哦……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30DF")

    label("loc_2F51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F80")

    ChrTalk(    #82
        0x104,
        "#1543F#5P哦哦……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30DF")

    label("loc_2F80")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FAC")

    ChrTalk(    #83
        0x10B,
        "#213F#5P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30DF")

    label("loc_2FAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FD8")

    ChrTalk(    #84
        0x107,
        "#064F#5P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30DF")

    label("loc_2FD8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3004")

    ChrTalk(    #85
        0x10A,
        "#814F#5P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30DF")

    label("loc_3004")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3031")

    ChrTalk(    #86
        0x105,
        "#1164F#5P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30DF")

    label("loc_3031")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_305D")

    ChrTalk(    #87
        0x106,
        "#052F#5P唔……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30DF")

    label("loc_305D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_308A")

    ChrTalk(    #88
        0x10F,
        "#1444F#5P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30DF")

    label("loc_308A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30B6")

    ChrTalk(    #89
        0x10E,
        "#173F#5P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30DF")

    label("loc_30B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30DF")

    ChrTalk(    #90
        0x10D,
        "#273F#5P唔……\x02",
    )

    CloseMessageWindow()

    label("loc_30DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3119")

    ChrTalk(    #91
        0x10C,
        "#115F#5P传送用的魔法阵吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_33D9")

    label("loc_3119")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3153")

    ChrTalk(    #92
        0x10D,
        "#272F#5P传送用的魔法阵吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_33D9")

    label("loc_3153")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_318D")

    ChrTalk(    #93
        0x10E,
        "#178F#5P传送用的魔法阵吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_33D9")

    label("loc_318D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31CC")

    ChrTalk(    #94
        0x10F,
        "#1443F#5P传送用的魔法阵……对吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_33D9")

    label("loc_31CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3206")

    ChrTalk(    #95
        0x106,
        "#057F#5P传送用的魔法阵吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_33D9")

    label("loc_3206")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3243")

    ChrTalk(    #96
        0x105,
        "#1163F#5P传送用的魔法阵，对吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_33D9")

    label("loc_3243")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_327F")

    ChrTalk(    #97
        0x10A,
        "#812F#5P传送用的魔法阵，对吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_33D9")

    label("loc_327F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32B7")

    ChrTalk(    #98
        0x107,
        "#062F#5P传送用的魔法阵……\x02",
    )

    CloseMessageWindow()
    Jump("loc_33D9")

    label("loc_32B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32F3")

    ChrTalk(    #99
        0x10B,
        "#212F#5P传送用的魔法阵，是吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_33D9")

    label("loc_32F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_332E")

    ChrTalk(    #100
        0x104,
        "#1542F#5P传送用的魔法阵吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_33D9")

    label("loc_332E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3368")

    ChrTalk(    #101
        0x108,
        "#072F#5P传送用的魔法阵吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_33D9")

    label("loc_3368")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33A3")

    ChrTalk(    #102
        0x103,
        "#1522F#5P传送用的魔法阵啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_33D9")

    label("loc_33A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33D9")

    ChrTalk(    #103
        0x101,
        "#1002F#5P传送用的魔法阵……\x02",
    )

    CloseMessageWindow()

    label("loc_33D9")

    Sleep(300)
    Fade(500)
    OP_6D(110, 0, 77100, 0)
    OP_67(0, 6250, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(45000, 0)
    OP_6E(275, 0)
    SetChrPos(0x109, -1780, 0, 76900, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3475")
    SetChrPos(0x102, -400, 0, 76730, 0)
    SetChrPos(0xF0, -2190, 0, 75100, 0)
    SetChrPos(0xF1, -240, 0, 75030, 0)
    Jump("loc_34FA")

    label("loc_3475")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B9")
    SetChrPos(0x102, -400, 0, 76730, 0)
    SetChrPos(0xEF, -2190, 0, 75100, 0)
    SetChrPos(0xF1, -240, 0, 75030, 0)
    Jump("loc_34FA")

    label("loc_34B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34FA")
    SetChrPos(0x102, -400, 0, 76730, 0)
    SetChrPos(0xEF, -2190, 0, 75100, 0)
    SetChrPos(0xF0, -240, 0, 75030, 0)

    label("loc_34FA")

    OP_0D()
    Sleep(800)

    ChrTalk(    #104
        0x109,
        (
            "#1065F#6P好了……\x01",
            "终于轮到这领域最后的战斗了。\x02\x03",

            "#1067F约修亚……\x01",
            "可以继续前进吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x102,
        (
            "#1505F#5P……没问题。\x02\x03",

            "#1500F准备万全之后\x01",
            "就进入魔法阵吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_35B9():
        OP_6B(3300, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_35B9)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0xEE, 0x0)
    OP_A2(0x2B29)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35E6")
    OP_A2(0x2647)

    label("loc_35E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35F7")
    OP_A2(0x2648)

    label("loc_35F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3608")
    OP_A2(0x2649)

    label("loc_3608")

    OP_28(0x3A, 0x1, 0x200)
    OP_28(0x3A, 0x1, 0x400)
    OP_6D(-1110, 0, 75880, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -1110, 0, 75880, 0)
    SetChrPos(0x1, -1110, 0, 75880, 0)
    SetChrPos(0x2, -1110, 0, 75880, 0)
    SetChrPos(0x3, -1110, 0, 75880, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    OP_72(0x404, 0x0)
    ExitThread()
    OP_7A(0x9, 0x2)
    OP_7B()
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_4_2076 end

    def Function_5_36E0(): pass

    label("Function_5_36E0")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3701")
    Sleep(100)
    Jump("loc_377C")

    label("loc_3701")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3716")
    Sleep(200)
    Jump("loc_377C")

    label("loc_3716")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_372B")
    Sleep(300)
    Jump("loc_377C")

    label("loc_372B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3740")
    Sleep(400)
    Jump("loc_377C")

    label("loc_3740")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3755")
    Sleep(500)
    Jump("loc_377C")

    label("loc_3755")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_376A")
    Sleep(600)
    Jump("loc_377C")

    label("loc_376A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_377C")
    Sleep(700)

    label("loc_377C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_379E")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_377C")

    label("loc_379E")

    Return()

    # Function_5_36E0 end

    def Function_6_379F(): pass

    label("Function_6_379F")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-1000, 1500, 87500, 0)
    OP_67(0, 5530, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(0, 0)
    OP_6E(308, 0)
    SetChrPos(0x109, -1000, 1500, 86910, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3838")
    SetChrPos(0x102, 0, 1500, 85800, 0)
    SetChrPos(0xF0, -2080, 1500, 85860, 0)
    SetChrPos(0xF1, -1020, 1500, 84810, 0)
    Jump("loc_38BD")

    label("loc_3838")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_387C")
    SetChrPos(0x102, 0, 1500, 85800, 0)
    SetChrPos(0xEF, -2080, 1500, 85860, 0)
    SetChrPos(0xF1, -1020, 1500, 84810, 0)
    Jump("loc_38BD")

    label("loc_387C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38BD")
    SetChrPos(0x102, 0, 1500, 85800, 0)
    SetChrPos(0xEF, -2080, 1500, 85860, 0)
    SetChrPos(0xF0, -1020, 1500, 84810, 0)

    label("loc_38BD")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(500)
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -1170, 1500, 85960, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3943():
        OP_6D(-1000, 10000, 85000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3943)

    def lambda_395B():
        OP_67(0, 3500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_395B)

    def lambda_3973():
        OP_6B(2800, 5000)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_3973)

    def lambda_3983():
        OP_6E(330, 5000)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_3983)
    Call(0, 11)
    OP_20(0xBB8)
    FadeToDark(3000, 0, -1)
    OP_0D()
    Sleep(1000)
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/M5414   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_379F end

    def Function_7_39B5(): pass

    label("Function_7_39B5")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x404, 0x0)
    ExitThread()
    OP_79(0x9, 0x2)
    OP_7B()
    LoadEffect(0x0, "map\\mp204_02.eff")
    LoadEffect(0x1, "map\\mp277_00.eff")
    SetChrPos(0x0, -1150, 1500, 85230, 180)
    SetChrPos(0x1, -2020, 1500, 86100, 180)
    SetChrPos(0x2, -10, 1500, 86170, 180)
    SetChrPos(0x3, -990, 1500, 86990, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-210, 1500, 86640, 0)
    OP_67(0, 5940, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(45000, 0)
    OP_6E(351, 0)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_3AB3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3AB3)

    def lambda_3AC5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3AC5)

    def lambda_3AD7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3AD7)

    def lambda_3AE9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3AE9)
    PlayEffect(0x0, 0xFF, 0xFF, -1170, 1500, 85960, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)
    Sleep(1000)

    def lambda_3B53():
        OP_6D(-850, 1450, 82640, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3B53)

    def lambda_3B6B():
        OP_67(0, 5940, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_3B6B)

    def lambda_3B83():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_3B83)

    def lambda_3B93():
        OP_6C(33000, 4000)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_3B93)
    Sleep(500)

    def lambda_3BA8():
        OP_8F(0xFE, 0xFFFFFAA6, 0x0, 0x12D86, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3BA8)
    Sleep(200)

    def lambda_3BC8():
        OP_8F(0xFE, 0xFFFFF6C8, 0x0, 0x13146, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3BC8)
    Sleep(500)

    def lambda_3BE8():
        OP_8F(0xFE, 0x0, 0x0, 0x1324A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3BE8)
    Sleep(150)

    def lambda_3C08():
        OP_8F(0xFE, 0xFFFFFC72, 0x0, 0x136B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3C08)
    WaitChrThread(0x0, 0x0)
    Sleep(300)
    OP_22(0x99, 0x0, 0x64)
    Fade(1000)
    OP_82(0x80, 0x0)
    OP_0D()
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C71")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3CD8")

    label("loc_3C71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C99")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3CD8")

    label("loc_3C99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CC1")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3CD8")

    label("loc_3CC1")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3CD8")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D05")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3D6C")

    label("loc_3D05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D2D")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3D6C")

    label("loc_3D2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D55")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3D6C")

    label("loc_3D55")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3D6C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D99")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3E00")

    label("loc_3D99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DC1")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3E00")

    label("loc_3DC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DE9")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3E00")

    label("loc_3DE9")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3E00")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E2D")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3E94")

    label("loc_3E2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E55")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3E94")

    label("loc_3E55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E7D")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3E94")

    label("loc_3E7D")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3E94")

    Sleep(1000)

    def lambda_3E9F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3E9F)
    Sleep(100)

    def lambda_3EB2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3EB2)
    Sleep(100)

    def lambda_3EC5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3EC5)
    Sleep(100)
    OP_8C(0x3, 0, 400)
    Sleep(300)

    ChrTalk(    #106
        0x109,
        "#1079F#11P怎、怎么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x102,
        "#1504F#11P传送的魔法阵……！？\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_3F33():
        OP_6D(-1000, 2050, 91120, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3F33)

    def lambda_3F4B():
        OP_67(0, 3000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_3F4B)

    def lambda_3F63():
        OP_6B(2740, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_3F63)

    def lambda_3F73():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_3F73)

    def lambda_3F83():
        OP_6E(356, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3F83)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)
    OP_22(0x14F, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0xFF, -1000, 2000, 87960, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_22(0xD7, 0x0, 0x64)
    Fade(1000)
    OP_82(0x0, 0x2)

    def lambda_3FE9():
        OP_6B(2550, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3FE9)
    OP_72(0x406, 0x0)
    ExitThread()
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(3000)
    Sleep(1000)

    ChrTalk(    #108
        0x102,
        "#1502F#5P这、这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x109,
        (
            "#1065F#5P……真是在意味深长的\x01",
            "时机出现了啊。\x02\x03",

            "#1067F不，搞不好……\x02\x03",

            "#1063F也许这个门\x01",
            "才是原本就在这里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x102,
        (
            "#1505F#5P原来如此……\x01",
            "有这个可能呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_23(0x14F)
    OP_44(0xEE, 0x0)
    OP_65(0x0, 0x1)
    OP_10(0x1, 0x0)
    OP_A2(0x2B2F)
    OP_72(0x404, 0x0)
    ExitThread()
    OP_7A(0x9, 0x2)
    OP_7B()
    OP_6D(-1140, 0, 78210, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -1140, 0, 78210, 0)
    SetChrPos(0x1, -1140, 0, 78210, 0)
    SetChrPos(0x2, -1140, 0, 78210, 0)
    SetChrPos(0x3, -1140, 0, 78210, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_7_39B5 end

    def Function_8_4258(): pass

    label("Function_8_4258")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -1150, 1500, 85230, 180)
    SetChrPos(0x1, -2020, 1500, 86100, 180)
    SetChrPos(0x2, -10, 1500, 86170, 180)
    SetChrPos(0x3, -990, 1500, 86990, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -1170, 1500, 85960, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 10)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_8_4258 end

    def Function_9_4336(): pass

    label("Function_9_4336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4347")
    Call(0, 6)
    Return()

    label("loc_4347")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -1150, 1500, 85230, 0)
    SetChrPos(0x2, -2020, 1500, 86100, 0)
    SetChrPos(0x1, -10, 1500, 86170, 0)
    SetChrPos(0x0, -990, 1500, 86990, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -1170, 1500, 85960, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    ClearMapFlags(0x2000000)
    Call(0, 11)
    NewScene("ED6_DT21/M5414   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_4336 end

    def Function_10_4408(): pass

    label("Function_10_4408")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4431")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4425():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4425)

    label("loc_4431")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_445A")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_444E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_444E)

    label("loc_445A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4483")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4477():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4477)

    label("loc_4483")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44AC")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_44A0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_44A0)

    label("loc_44AC")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44D8")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_44D8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44EF")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_44EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4506")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4506")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_451D")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_451D")

    Return()

    # Function_10_4408 end

    def Function_11_451E(): pass

    label("Function_11_451E")


    def lambda_4524():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4524)

    def lambda_4536():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4536)

    def lambda_4548():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4548)

    def lambda_455A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_455A)
    Sleep(1000)
    Return()

    # Function_11_451E end

    def Function_12_456C(): pass

    label("Function_12_456C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_458A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_458A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x3, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_459E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_459E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_45B2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_45B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_45C6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_45C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_45DA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_45DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_45EE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_45EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4602")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4602")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4616")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4616")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_462A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_462A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xB, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_463E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_463E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4652")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4652")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4666")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4666")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_467A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_467A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_468E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_468E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_46A2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_46A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_46B6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_46B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_46CA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_46CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_46DE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_46DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_46F2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_46F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4706")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4706")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x19, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_471A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_471A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_472E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_472E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4742")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4742")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4756")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4756")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x24, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_476A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_476A")

    Return()

    # Function_12_456C end

    def Function_13_476B(): pass

    label("Function_13_476B")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #111
        "\x07\x05打开『门』吗？\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_47C8")

    label("loc_47C8")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_13_476B end

    def Function_14_47DF(): pass

    label("Function_14_47DF")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, -390, 1500, 85500, 0)
    SetChrPos(0x1, -1970, 1500, 85420, 0)
    SetChrPos(0x2, -280, 1500, 83310, 0)
    SetChrPos(0x3, -2220, 1500, 83380, 0)
    OP_6D(-1070, 1500, 85620, 0)
    OP_67(0, 6340, -10000, 0)
    OP_6B(4660, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x12, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48B5")
    OP_28(0x12, 0x4, 0x2)
    OP_82(0x82, 0x2)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_48B5")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #112
        (
            "\x07\x05#40W　　全即为一，一亦为全……\x01",
            "　　   全由一所生，\x01",
            "      亦将复归于一……\x01",
            "#500W\x01",
            "#40W  当汝将『门』尽数解放之时，\x01",
            " 　  则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Call(0, 12)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_49A9")
    Call(0, 13)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49A6")
    Call(0, 15)

    label("loc_49A6")

    Jump("loc_49A9")

    label("loc_49A9")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_14_47DF end

    def Function_15_49B5(): pass

    label("Function_15_49B5")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x6, 0)
    OP_70(0x6, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x6)
    Sleep(500)

    def lambda_4A1E():
        OP_6B(4000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4A1E)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_23(0x85)
    OP_E3(0x0, 0x1D, 0, 0x0)
    NewScene("ED6_DT21/P9001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_49B5 end

    def Function_16_4A6E(): pass

    label("Function_16_4A6E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, -390, 1500, 85500, 0)
    SetChrPos(0x1, -1970, 1500, 85420, 0)
    SetChrPos(0x2, -280, 1500, 83310, 0)
    SetChrPos(0x3, -2220, 1500, 83380, 0)
    OP_6D(-1070, 1500, 85620, 0)
    OP_67(0, 6340, -10000, 0)
    OP_6B(4660, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_16_4A6E end

    SaveToFile()

Try(main)
