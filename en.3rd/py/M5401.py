from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Bleublanc',                            # 9
        'Walter',                               # 10
        'Luciola',                              # 11
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
        "Function_4_2461",         # 04, 4
        "Function_5_3C64",         # 05, 5
        "Function_6_3D23",         # 06, 6
        "Function_7_3F39",         # 07, 7
        "Function_8_47F6",         # 08, 8
        "Function_9_48D4",         # 09, 9
        "Function_10_49A6",        # 0A, 10
        "Function_11_4ABC",        # 0B, 11
        "Function_12_4B0A",        # 0C, 12
        "Function_13_4D09",        # 0D, 13
        "Function_14_4D62",        # 0E, 14
        "Function_15_4F59",        # 0F, 15
        "Function_16_5012",        # 10, 16
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
        "Man's Voice",
        (
            "#2PAllow me to congratulate you on making it\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66E")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6D5")

    label("loc_66E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_696")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6D5")

    label("loc_696")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BE")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6D5")

    label("loc_6BE")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6D5")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_702")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_769")

    label("loc_702")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72A")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_769")

    label("loc_72A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_752")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_769")

    label("loc_752")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_769")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_796")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7FD")

    label("loc_796")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BE")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7FD")

    label("loc_7BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E6")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7FD")

    label("loc_7E6")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_7FD")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82A")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_891")

    label("loc_82A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_852")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_891")

    label("loc_852")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87A")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_891")

    label("loc_87A")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_891")

    Sleep(1000)
    OP_1D(0x6F)
    Fade(500)
    OP_6D(-900, 0, 56000, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3450, 0)
    OP_6C(0, 0)
    OP_6E(337, 0)
    SetChrPos(0x109, -1510, 0, 50360, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92F")
    SetChrPos(0xEF, -260, 0, 50300, 0)
    SetChrPos(0xF0, -1930, 0, 48960, 0)
    SetChrPos(0xF1, 210, 0, 49040, 0)
    Jump("loc_9B4")

    label("loc_92F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_973")
    SetChrPos(0xF0, -260, 0, 50300, 0)
    SetChrPos(0xEF, -1930, 0, 48960, 0)
    SetChrPos(0xF1, 210, 0, 49040, 0)
    Jump("loc_9B4")

    label("loc_973")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B4")
    SetChrPos(0xF1, -260, 0, 50300, 0)
    SetChrPos(0xEF, -1930, 0, 48960, 0)
    SetChrPos(0xF0, 210, 0, 49040, 0)

    label("loc_9B4")


    def lambda_9BA():
        OP_6D(-900, 1500, 84630, 4500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_9BA)

    def lambda_9D2():
        OP_67(0, 2500, -10000, 4500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_9D2)

    def lambda_9EA():
        OP_6B(2850, 4500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_9EA)

    def lambda_9FA():
        OP_6C(0, 4500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_9FA)

    def lambda_A0A():
        OP_6E(290, 4500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_A0A)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #1
        0x10,
        (
            "#231F#5PHaha! Quite a surprise to reunite with you\x01",
            "all in this way, let me tell you.\x02\x03",

            "Fate is a splendidly peculiar thing, is it not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x11,
        (
            "#252F#5PYou sure know how to make a guy crack a\x01",
            "smile.\x02\x03",

            "You came all this way just to give lil' old me\x01",
            "a fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x12,
        (
            "#240F#5PCircumstances as they are, it IS good to see\x01",
            "you again.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0A")
    SetChrPos(0xEF, -400, 0, 65710, 0)
    SetChrPos(0xF0, -1720, 0, 64430, 0)
    SetChrPos(0xF1, -150, 0, 64069, 0)
    Jump("loc_C8F")

    label("loc_C0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4E")
    SetChrPos(0xF0, -400, 0, 65710, 0)
    SetChrPos(0xEF, -1720, 0, 64430, 0)
    SetChrPos(0xF1, -150, 0, 64069, 0)
    Jump("loc_C8F")

    label("loc_C4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8F")
    SetChrPos(0xF1, -400, 0, 65710, 0)
    SetChrPos(0xEF, -1720, 0, 64430, 0)
    SetChrPos(0xF0, -150, 0, 64069, 0)

    label("loc_C8F")


    def lambda_C95():
        OP_8F(0xFE, 0xFFFFF8BC, 0x0, 0x1207A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C95)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1B")

    def lambda_CC3():
        OP_8F(0xFE, 0xFFFFFE7A, 0x0, 0x12084, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_CC3)
    Sleep(100)

    def lambda_CE3():
        OP_8F(0xFE, 0xFFFFF72C, 0x0, 0x1197C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_CE3)
    Sleep(100)

    def lambda_D03():
        OP_8F(0xFE, 0xFFFFFE3E, 0x0, 0x119A4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_D03)
    Jump("loc_DF0")

    label("loc_D1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D87")

    def lambda_D2F():
        OP_8F(0xFE, 0xFFFFFE7A, 0x0, 0x12084, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_D2F)
    Sleep(100)

    def lambda_D4F():
        OP_8F(0xFE, 0xFFFFF72C, 0x0, 0x1197C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_D4F)
    Sleep(100)

    def lambda_D6F():
        OP_8F(0xFE, 0xFFFFFE3E, 0x0, 0x119A4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_D6F)
    Jump("loc_DF0")

    label("loc_D87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF0")

    def lambda_D9B():
        OP_8F(0xFE, 0xFFFFFE7A, 0x0, 0x12084, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_D9B)
    Sleep(100)

    def lambda_DBB():
        OP_8F(0xFE, 0xFFFFF72C, 0x0, 0x1197C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_DBB)
    Sleep(100)

    def lambda_DDB():
        OP_8F(0xFE, 0xFFFFFE3E, 0x0, 0x119A4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_DDB)

    label("loc_DF0")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #4
        0x102,
        (
            "#1502F#11PI figured you would be the ones waiting\x01",
            "for us.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10CB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F16")

    ChrTalk(    #5
        0x10,
        (
            "#230F#5PAbove all, what joy I feel that my most worthy\x01",
            "rival and my beloved princess are among your\x01",
            "number.\x02\x03",

            "#231FThe Goddess must truly favor me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1041")

    label("loc_F16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FB4")

    ChrTalk(    #6
        0x10,
        (
            "#230F#5PAbove all, what joy I feel that my most beloved,\x01",
            "stunning princess is among your number.\x02\x03",

            "#231FThe Goddess must truly favor me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1041")

    label("loc_FB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1041")

    ChrTalk(    #7
        0x10,
        (
            "#230F#5PAbove all, what joy I feel that my most worthy\x01",
            "rival is among your number.\x02\x03",

            "#231FThe Goddess must truly favor me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1041")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1081")

    ChrTalk(    #8
        0x105,
        "#1382F#11PUmm... It's...been a while, I see.\x02",
    )

    CloseMessageWindow()

    label("loc_1081")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10CB")

    ChrTalk(    #9
        0x104,
        (
            "#1541F#11PHeh. I'm pleased to see you haven't\x01",
            "changed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1186")

    ChrTalk(    #10
        0x103,
        "#1523F#11PL-Luci...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x12,
        (
            "#247F#5P...And there was I thinking we would never\x01",
            "meet again.\x02\x03",

            "#240FI see fate had other ideas...although I can't\x01",
            "say I'm unhappy about that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1186")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1263")

    ChrTalk(    #12
        0x108,
        "#072F#11PWalter...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x11,
        (
            "#253FHeh. We keep bumpin' into each other in the\x01",
            "weirdest damn places, don't we?\x02\x03",

            "Looks like we're gonna get another chance to\x01",
            "fight after all. Works for me--I say we get it on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1263")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_141D")
    Sleep(500)

    ChrTalk(    #14
        0x110,
        (
            "#263F#11PSo I get to fight you three, do I?\x02\x03",

            "#1306FI can barely wait to get started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        "#230F#5PThe pleasure is all ours, we assure you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x12,
        (
            "#247F#5PIndeed...\x02\x03",

            "#241FFighting both the Black Fang and the\x01",
            "Angel of Slaughter at once is going to\x01",
            "pose an interesting challenge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        (
            "#252F#5PBut I ain't one to back away from a tough fight.\x02\x03",

            "In fact, I crave 'em. So let's go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x110,
        "#261F#11PTeehee. I couldn't agree more!\x02",
    )

    CloseMessageWindow()

    label("loc_141D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1634")
    Sleep(500)

    ChrTalk(    #19
        0x101,
        (
            "#1007F#11P*sigh* Do we have any cards left we can whip\x01",
            "out to avoid this?\x02\x03",

            "#1019FThree Ouroboros members at once isn't what\x01",
            "I'd call a fair fight. Or even a winnable one...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        "#231F#5PTut tut! Surely you jest, Estelle Bright.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x12,
        (
            "#247F#5PYou've grown wonderfully since our first\x01",
            "encounter, and I'm sure you know as much\x01",
            "better than anyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        (
            "#253F#5PI'm actually lookin' forward to fighting you again,\x01",
            "girlie. Don't let me down, now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1016F#11PA-Ahaha... Wow. Way to put the pressure on,\x01",
            "you guys...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1634")

    Sleep(500)

    ChrTalk(    #24
        0x109,
        (
            "#1841F#6P*sigh* There's no way we're walking away\x01",
            "from this one.\x02\x03",

            "#1840FProbably no point in saying this, but take it\x01",
            "easy on us, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        (
            "#252F#5PAs if you, of all people, need us goin' easy.\x02\x03",

            "Your game was up a long time ago, conman.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #26
        0x109,
        "#1063F#6P...\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #27
        0x10,
        (
            "#232F#5PI'd heard many a rumor regarding the church's\x01",
            "Heretic Hunter in the past...\x02\x03",

            "#231F...but I feared such rumors were almost\x01",
            "downplayed after learning he had the strength\x01",
            "to slay the Faceless alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x12,
        (
            "#247F#5PYou certainly did a flawless job of deceiving us.\x02\x03",

            "#240FI don't believe we have any interest in avenging\x01",
            "his death...\x02",
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
            "#231F#5P...but it's only right for us to repay our debts--\x01",
            "and we certainly owe you one for swindling us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x11,
        (
            "#253F#5PSo c'mon. Time for you to show your true\x01",
            "colors and stop playin' around.\x02",
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
            "#1075F#11P*sigh* Well, if that's really what you want...\x02\x03",

            "#1073FThere wasn't any point in holdin' back against\x01",
            "you freaks anyway.\x02",
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
            "#1065F#11PYou got your wish. I hereby acknowledge you\x01",
            "as heretics.\x02\x03",

            "#1072FLet the hunt begin.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C10")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BBF")

    ChrTalk(    #33
        0x101,
        "#1026F#11PK-Kevin...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10F,
        "#1802F#11P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C10")

    label("loc_1BBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BEA")

    ChrTalk(    #35
        0x101,
        "#1026F#11PK-Kevin...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C10")

    label("loc_1BEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C10")

    ChrTalk(    #36
        0x10F,
        "#1802F#11PKevin...\x02",
    )

    CloseMessageWindow()

    label("loc_1C10")


    ChrTalk(    #37
        0x10,
        (
            "#231F#2PHaha! That's IT! That's exactly what I wanted!\x02\x03",

            "You look every bit the monster I'd hoped you\x01",
            "were...just like us.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #38
        0x10,
        "Walter",
        (
            "#253F#2PDon't you even think of holding back, kiddo.\x02\x03",

            "Not unless you wanna end up splattered on\x01",
            "the ground.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x102,
        (
            "#1513F#11POh, I wouldn't dream of it at this point.\x02\x03",

            "#1514FBy the time I walked through that door,\x01",
            "my resolve was set.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    OP_22(0x1F5, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DAD")
    SetChrChipByIndex(0x102, 12)
    SetChrSubChip(0x102, 0)
    Jump("loc_1DE0")

    label("loc_1DAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DC8")
    SetChrChipByIndex(0x102, 14)
    SetChrSubChip(0x102, 0)
    Jump("loc_1DE0")

    label("loc_1DC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DE0")
    SetChrChipByIndex(0x102, 16)
    SetChrSubChip(0x102, 0)

    label("loc_1DE0")

    OP_0D()
    Sleep(500)

    ChrTalk(    #40
        0x102,
        "#1502F#11PIf I can't win here, I won't be fit to face him...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #41
        0x102,
        (
            "#1506F#11P#4S...so I'm going to come at you with all\x01",
            "I've got. There's no way in hell I'll lose!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EF1")

    ChrTalk(    #42
        0x110,
        "#1307F#11PJoshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1002F#11P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F42")

    label("loc_1EF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F1B")

    ChrTalk(    #44
        0x101,
        "#1002F#11PJoshua...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F42")

    label("loc_1F1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F42")

    ChrTalk(    #45
        0x110,
        "#1307F#11PJoshua...\x02",
    )

    CloseMessageWindow()

    label("loc_1F42")

    Sleep(150)
    Fade(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F80")
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 14)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 16)
    SetChrSubChip(0xF1, 0)
    Jump("loc_1FE5")

    label("loc_1F80")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FB4")
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 12)
    SetChrSubChip(0xEF, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 16)
    SetChrSubChip(0xF1, 0)
    Jump("loc_1FE5")

    label("loc_1FB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FE5")
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 12)
    SetChrSubChip(0xEF, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 14)
    SetChrSubChip(0xF0, 0)

    label("loc_1FE5")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20D0")
    SetChrPos(0xEF, -340, 0, 74010, 0)
    SetChrPos(0xF0, -2180, 0, 72230, 0)
    SetChrPos(0xF1, 170, 0, 72350, 0)
    Jump("loc_2155")

    label("loc_20D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2114")
    SetChrPos(0xF0, -340, 0, 74010, 0)
    SetChrPos(0xEF, -2180, 0, 72230, 0)
    SetChrPos(0xF1, 170, 0, 72350, 0)
    Jump("loc_2155")

    label("loc_2114")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2155")
    SetChrPos(0xF1, -340, 0, 74010, 0)
    SetChrPos(0xEF, -2180, 0, 72230, 0)
    SetChrPos(0xF0, 170, 0, 72350, 0)

    label("loc_2155")

    OP_20(0x7D0)

    def lambda_2160():
        OP_6B(3310, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2160)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    OP_21()
    OP_1D(0x37)
    Sleep(1000)

    ChrTalk(    #46
        0x12,
        (
            "#247F#5PHeehee...\x02\x03",

            "#241FMy, my. We've a spectacular performance\x01",
            "in store for us, don't we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x11,
        (
            "#252F#5PYou're tellin' me. I'm fired up just thinkin'\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10,
        "#230F#5PThen may the curtain rise.\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #49
        0x10,
        (
            "#234F#5P#3SLet us begin a carnival for the ages!#2S\x02\x03",

            "#3SIllusory and infinite, spectacular and without end!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_22E0():
        OP_6D(-1000, 200, 84390, 250)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_22E0)

    def lambda_22F8():
        OP_67(0, 2610, -10000, 250)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_22F8)

    def lambda_2310():
        OP_6B(3100, 250)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_2310)

    def lambda_2320():
        OP_6E(287, 250)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_2320)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x10, 6)
    SetChrSubChip(0x10, 0)
    OP_7D(0x0, 0x10, 0x32, 0x1F4)

    def lambda_2347():
        OP_96(0xFE, 0xFFFFFC4A, 0x0, 0x127B4, 0x190, 0x157C)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2347)
    Sleep(30)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x11, 7)
    SetChrSubChip(0x11, 2)
    OP_7D(0x0, 0x11, 0x32, 0x1F4)

    def lambda_2381():
        OP_96(0xFE, 0xFFFFFF56, 0x0, 0x12CBE, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2381)
    Sleep(30)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x12, 8)
    SetChrSubChip(0x12, 3)
    OP_7D(0x0, 0x12, 0x32, 0x1F4)

    def lambda_23BB():
        OP_96(0xFE, 0xFFFFF8C6, 0x0, 0x12CD2, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_23BB)

    def lambda_23D9():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_23D9)

    def lambda_23F4():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_23F4)

    def lambda_240F():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_240F)

    def lambda_242A():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_242A)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x2AD, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_279 end

    def Function_4_2461(): pass

    label("Function_4_2461")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2685")
    SetChrPos(0xEF, -300, 0, 76730, 0)
    SetChrPos(0xF0, -2190, 0, 75100, 0)
    SetChrPos(0xF1, -240, 0, 75030, 0)
    Jump("loc_270A")

    label("loc_2685")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26C9")
    SetChrPos(0xF0, -300, 0, 76730, 0)
    SetChrPos(0xEF, -2190, 0, 75100, 0)
    SetChrPos(0xF1, -240, 0, 75030, 0)
    Jump("loc_270A")

    label("loc_26C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_270A")
    SetChrPos(0xF1, -300, 0, 76730, 0)
    SetChrPos(0xEF, -2190, 0, 75100, 0)
    SetChrPos(0xF0, -240, 0, 75030, 0)

    label("loc_270A")

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
        "#254F#5P#40WBah... I underestimated you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x12,
        (
            "#247F#5P#40WOh, I had a lovely time, personally.\x02\x03",

            "#240FI almost wish it could have lasted a little\x01",
            "longer.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28B1")

    ChrTalk(    #52
        0x101,
        "#1007F#12PY-You're messing with me...right...?\x02",
    )

    CloseMessageWindow()

    label("loc_28B1")


    ChrTalk(    #53
        0x102,
        "#1514F#12PI think we're fine with stopping here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x109,
        "#1068F#6PSeriously.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2936")

    ChrTalk(    #55
        0x110,
        "#261F#12PReally? I'm with Luciola.\x02",
    )

    CloseMessageWindow()

    label("loc_2936")


    ChrTalk(    #56
        0x10,
        (
            "#232F#5P#40WRegardless, you have defeated us, and with that\x01",
            "claimed the right to challenge the fourth guardian.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x12,
        (
            "#244F#5P#40WThe first to be chosen by the Lord of Phantasma,\x01",
            "and the last that you shall face...\x02\x03",

            "#240FDefeating him will be no easy task.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x11,
        (
            "#257F#5P#40WBut hey, you managed to give the three of\x01",
            "us a real workout.\x02\x03",

            "#253FDon't go screwin' up now, or I'm gonna kill\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        "#1513F#12PWe won't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x109,
        (
            "#1066F#6PI'd rather avoid death at your fists,\x01",
            "so count on it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D27")
    Sleep(500)

    ChrTalk(    #61
        0x103,
        (
            "#1532F#12PLuci, I...\x02\x03",

            "Umm... Does you being here mean...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x12,
        (
            "#244F#5P#40WI'm afraid I can't answer that, dear.\x02\x03",

            "#240FI'm not the real Luciola, after all. Whether the\x01",
            "real one is living or dead is something I cannot\x01",
            "know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x103,
        "#1525F#12P...Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x12,
        (
            "#247F#5P#40WThe answer is surely out there, however.\x01",
            "You'll just have to find it yourself once you\x01",
            "return to your own world.\x02\x03",

            "#241FBut I would like to say this before I go:\x01",
            "your new look really suits you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x103,
        (
            "#1523F#12P...!\x02\x03",

            "#1521FHaha. Thanks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2ECD")
    Sleep(500)

    ChrTalk(    #66
        0x108,
        "#074F#4PWalter, there's something I should tell yo--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x11,
        (
            "#251F#5P#30WIf you're talkin' about Kilika, I already know.\x02\x03",

            "Something about her being scouted out for an\x01",
            "intelligence agency in Calvard, right?\x02\x03",

            "#257FGive her a message from me, Zin.\x02\x03",

            "#253FTell her she's never gonna get married if she\x01",
            "doesn't stop overdoin' the tough girl act.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x108,
        "#070F#4PHaha... All right. I'll take the punch for you.\x02",
    )

    CloseMessageWindow()

    label("loc_2ECD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3169")
    Sleep(500)

    ChrTalk(    #69
        0x110,
        "#267F#12PDo you really have to go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x10,
        (
            "#230F#5P#40WIt pains me to say yes, but we must.\x02\x03",

            "What about you? When will you be returning\x01",
            "to Ouroboros?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x110,
        "#1300F#12P...Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x12,
        (
            "#247F#5P#40WYou needn't feel rushed to find your way again.\x01",
            "Take as long as you need.\x02\x03",

            "#240FNo one can restrict the actions of we Enforcers.\x02\x03",

            "Not even the Anguis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x11,
        (
            "#252F#5P#40WIf you do become our enemy, I'll be lookin'\x01",
            "forward to a hell of a fight with you again.\x02\x03",

            "#257FAnd if you come back to us...I'm up for givin'\x01",
            "you some training if you want it.\x02\x03",

            "#251FYou'd be able to master my Zero Impact in\x01",
            "no time flat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x110,
        "#261F#12PHeehee. I'll give it some thought.\x02",
    )

    CloseMessageWindow()

    label("loc_3169")

    Sleep(500)

    ChrTalk(    #75
        0x10,
        "#230F#5P#40WAhh... It appears our time is up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x12,
        "#247F#5P#40WFor now, I bid you all farewell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x11,
        "#252F#5P#40WHeh. Later.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(140, 1500, 85730, 0)
    OP_67(0, 4090, -10000, 0)
    OP_6B(2330, 0)
    OP_6C(33000, 0)
    OP_6E(396, 0)

    def lambda_323D():
        OP_6B(2150, 5000)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_323D)
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

    def lambda_3324():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3324)

    def lambda_3336():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3336)

    def lambda_3348():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3348)
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

    def lambda_338F():
        OP_6D(-1000, 3050, 84700, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_338F)

    def lambda_33A7():
        OP_67(0, 9000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_33A7)

    def lambda_33BF():
        OP_6B(3380, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_33BF)

    def lambda_33CF():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_33CF)

    def lambda_33DF():
        OP_6E(208, 4000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_33DF)
    WaitChrThread(0xEE, 0x0)
    Fade(1000)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xEE, 0x0)
    OP_0D()
    Sleep(500)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3461")

    ChrTalk(    #78
        0x110,
        "#264F#5POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3615")

    label("loc_3461")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3486")

    ChrTalk(    #79
        0x101,
        "#1004F#5POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3615")

    label("loc_3486")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34AB")

    ChrTalk(    #80
        0x103,
        "#1523F#5POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3615")

    label("loc_34AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34CF")

    ChrTalk(    #81
        0x108,
        "#073F#5POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3615")

    label("loc_34CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34F4")

    ChrTalk(    #82
        0x104,
        "#1543F#5POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3615")

    label("loc_34F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3518")

    ChrTalk(    #83
        0x10B,
        "#213F#5POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3615")

    label("loc_3518")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_353C")

    ChrTalk(    #84
        0x107,
        "#064F#5POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3615")

    label("loc_353C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3560")

    ChrTalk(    #85
        0x10A,
        "#814F#5POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3615")

    label("loc_3560")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3585")

    ChrTalk(    #86
        0x105,
        "#1164F#5POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3615")

    label("loc_3585")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35AA")

    ChrTalk(    #87
        0x106,
        "#052F#5PHmm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3615")

    label("loc_35AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35CF")

    ChrTalk(    #88
        0x10F,
        "#1444F#5POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3615")

    label("loc_35CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35F3")

    ChrTalk(    #89
        0x10E,
        "#173F#5POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3615")

    label("loc_35F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3615")

    ChrTalk(    #90
        0x10D,
        "#273F#5PHmm...\x02",
    )

    CloseMessageWindow()

    label("loc_3615")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_364F")

    ChrTalk(    #91
        0x10C,
        "#115F#5PIt's another warp circle...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3909")

    label("loc_364F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3689")

    ChrTalk(    #92
        0x10D,
        "#272F#5PIt's another warp circle...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3909")

    label("loc_3689")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36C3")

    ChrTalk(    #93
        0x10E,
        "#178F#5PIt's another warp circle...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3909")

    label("loc_36C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36FE")

    ChrTalk(    #94
        0x10F,
        "#1443F#5PIt's another warp circle...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3909")

    label("loc_36FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3738")

    ChrTalk(    #95
        0x106,
        "#057F#5PIt's another warp circle...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3909")

    label("loc_3738")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3773")

    ChrTalk(    #96
        0x105,
        "#1163F#5PIt's another warp circle...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3909")

    label("loc_3773")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37AD")

    ChrTalk(    #97
        0x10A,
        "#812F#5PIt's another warp circle...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3909")

    label("loc_37AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37E7")

    ChrTalk(    #98
        0x107,
        "#062F#5PIt's another warp circle...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3909")

    label("loc_37E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3821")

    ChrTalk(    #99
        0x10B,
        "#212F#5PIt's another warp circle...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3909")

    label("loc_3821")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_385C")

    ChrTalk(    #100
        0x104,
        "#1542F#5PIt's another warp circle...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3909")

    label("loc_385C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3896")

    ChrTalk(    #101
        0x108,
        "#072F#5PIt's another warp circle...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3909")

    label("loc_3896")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38D1")

    ChrTalk(    #102
        0x103,
        "#1522F#5PIt's another warp circle...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3909")

    label("loc_38D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3909")

    ChrTalk(    #103
        0x101,
        "#1002F#5PIt's another warp circle...\x02",
    )

    CloseMessageWindow()

    label("loc_3909")

    Sleep(300)
    Fade(500)
    OP_6D(110, 0, 77100, 0)
    OP_67(0, 6250, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(45000, 0)
    OP_6E(275, 0)
    SetChrPos(0x109, -1780, 0, 76900, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39A5")
    SetChrPos(0x102, -400, 0, 76730, 0)
    SetChrPos(0xF0, -2190, 0, 75100, 0)
    SetChrPos(0xF1, -240, 0, 75030, 0)
    Jump("loc_3A2A")

    label("loc_39A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39E9")
    SetChrPos(0x102, -400, 0, 76730, 0)
    SetChrPos(0xEF, -2190, 0, 75100, 0)
    SetChrPos(0xF1, -240, 0, 75030, 0)
    Jump("loc_3A2A")

    label("loc_39E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A2A")
    SetChrPos(0x102, -400, 0, 76730, 0)
    SetChrPos(0xEF, -2190, 0, 75100, 0)
    SetChrPos(0xF0, -240, 0, 75030, 0)

    label("loc_3A2A")

    OP_0D()
    Sleep(800)

    ChrTalk(    #104
        0x109,
        (
            "#1065F#6PRight... On the other side of that circle awaits\x01",
            "this area's final battle.\x02\x03",

            "#1067FYou're sure you're ready for this, Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x102,
        (
            "#1505F#5P...As ready as I'll ever be.\x02\x03",

            "#1500FDon't hold back for my sake. We can step\x01",
            "inside as soon as you guys want.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3B3D():
        OP_6B(3300, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3B3D)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0xEE, 0x0)
    OP_A2(0x2B29)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B6A")
    OP_A2(0x2647)

    label("loc_3B6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B7B")
    OP_A2(0x2648)

    label("loc_3B7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B8C")
    OP_A2(0x2649)

    label("loc_3B8C")

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

    # Function_4_2461 end

    def Function_5_3C64(): pass

    label("Function_5_3C64")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C85")
    Sleep(100)
    Jump("loc_3D00")

    label("loc_3C85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C9A")
    Sleep(200)
    Jump("loc_3D00")

    label("loc_3C9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CAF")
    Sleep(300)
    Jump("loc_3D00")

    label("loc_3CAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CC4")
    Sleep(400)
    Jump("loc_3D00")

    label("loc_3CC4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CD9")
    Sleep(500)
    Jump("loc_3D00")

    label("loc_3CD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CEE")
    Sleep(600)
    Jump("loc_3D00")

    label("loc_3CEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D00")
    Sleep(700)

    label("loc_3D00")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D22")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_3D00")

    label("loc_3D22")

    Return()

    # Function_5_3C64 end

    def Function_6_3D23(): pass

    label("Function_6_3D23")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-1000, 1500, 87500, 0)
    OP_67(0, 5530, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(0, 0)
    OP_6E(308, 0)
    SetChrPos(0x109, -1000, 1500, 86910, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DBC")
    SetChrPos(0x102, 0, 1500, 85800, 0)
    SetChrPos(0xF0, -2080, 1500, 85860, 0)
    SetChrPos(0xF1, -1020, 1500, 84810, 0)
    Jump("loc_3E41")

    label("loc_3DBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E00")
    SetChrPos(0x102, 0, 1500, 85800, 0)
    SetChrPos(0xEF, -2080, 1500, 85860, 0)
    SetChrPos(0xF1, -1020, 1500, 84810, 0)
    Jump("loc_3E41")

    label("loc_3E00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E41")
    SetChrPos(0x102, 0, 1500, 85800, 0)
    SetChrPos(0xEF, -2080, 1500, 85860, 0)
    SetChrPos(0xF0, -1020, 1500, 84810, 0)

    label("loc_3E41")

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

    def lambda_3EC7():
        OP_6D(-1000, 10000, 85000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3EC7)

    def lambda_3EDF():
        OP_67(0, 3500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_3EDF)

    def lambda_3EF7():
        OP_6B(2800, 5000)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_3EF7)

    def lambda_3F07():
        OP_6E(330, 5000)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_3F07)
    Call(0, 11)
    OP_20(0xBB8)
    FadeToDark(3000, 0, -1)
    OP_0D()
    Sleep(1000)
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/M5414   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_3D23 end

    def Function_7_3F39(): pass

    label("Function_7_3F39")

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

    def lambda_4037():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4037)

    def lambda_4049():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4049)

    def lambda_405B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_405B)

    def lambda_406D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_406D)
    PlayEffect(0x0, 0xFF, 0xFF, -1170, 1500, 85960, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)
    Sleep(1000)

    def lambda_40D7():
        OP_6D(-850, 1450, 82640, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_40D7)

    def lambda_40EF():
        OP_67(0, 5940, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_40EF)

    def lambda_4107():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_4107)

    def lambda_4117():
        OP_6C(33000, 4000)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_4117)
    Sleep(500)

    def lambda_412C():
        OP_8F(0xFE, 0xFFFFFAA6, 0x0, 0x12D86, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_412C)
    Sleep(200)

    def lambda_414C():
        OP_8F(0xFE, 0xFFFFF6C8, 0x0, 0x13146, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_414C)
    Sleep(500)

    def lambda_416C():
        OP_8F(0xFE, 0x0, 0x0, 0x1324A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_416C)
    Sleep(150)

    def lambda_418C():
        OP_8F(0xFE, 0xFFFFFC72, 0x0, 0x136B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_418C)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41F5")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_425C")

    label("loc_41F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_421D")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_425C")

    label("loc_421D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4245")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_425C")

    label("loc_4245")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_425C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4289")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_42F0")

    label("loc_4289")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42B1")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_42F0")

    label("loc_42B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42D9")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_42F0")

    label("loc_42D9")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_42F0")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_431D")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4384")

    label("loc_431D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4345")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4384")

    label("loc_4345")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_436D")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4384")

    label("loc_436D")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4384")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43B1")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4418")

    label("loc_43B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43D9")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4418")

    label("loc_43D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4401")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4418")

    label("loc_4401")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4418")

    Sleep(1000)

    def lambda_4423():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4423)
    Sleep(100)

    def lambda_4436():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4436)
    Sleep(100)

    def lambda_4449():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4449)
    Sleep(100)
    OP_8C(0x3, 0, 400)
    Sleep(300)

    ChrTalk(    #106
        0x109,
        "#1079F#11PHey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x102,
        "#1504F#11PWhere did the warp circle go?\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_44AC():
        OP_6D(-1000, 2050, 91120, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_44AC)

    def lambda_44C4():
        OP_67(0, 3000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_44C4)

    def lambda_44DC():
        OP_6B(2740, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_44DC)

    def lambda_44EC():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_44EC)

    def lambda_44FC():
        OP_6E(356, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_44FC)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)
    OP_22(0x14F, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0xFF, -1000, 2000, 87960, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_22(0xD7, 0x0, 0x64)
    Fade(1000)
    OP_82(0x0, 0x2)

    def lambda_4562():
        OP_6B(2550, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_4562)
    OP_72(0x406, 0x0)
    ExitThread()
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(3000)
    Sleep(1000)

    ChrTalk(    #108
        0x102,
        "#1502F#5PWh-What?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x109,
        (
            "#1065F#5PWell, that's foreboding.\x02\x03",

            "#1067FActually, thinking about it...\x02\x03",

            "#1063FIt's possible it was this door that was here\x01",
            "first, and the warp appeared later and took\x01",
            "its place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x102,
        "#1505F#5PHmm... That would make sense.\x02",
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

    # Function_7_3F39 end

    def Function_8_47F6(): pass

    label("Function_8_47F6")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_8_47F6 end

    def Function_9_48D4(): pass

    label("Function_9_48D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48E5")
    Call(0, 6)
    Return()

    label("loc_48E5")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_9_48D4 end

    def Function_10_49A6(): pass

    label("Function_10_49A6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49CF")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_49C3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_49C3)

    label("loc_49CF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49F8")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_49EC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_49EC)

    label("loc_49F8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A21")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4A15():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4A15)

    label("loc_4A21")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A4A")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4A3E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4A3E)

    label("loc_4A4A")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A76")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4A76")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A8D")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4A8D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AA4")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4AA4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4ABB")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4ABB")

    Return()

    # Function_10_49A6 end

    def Function_11_4ABC(): pass

    label("Function_11_4ABC")


    def lambda_4AC2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4AC2)

    def lambda_4AD4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4AD4)

    def lambda_4AE6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4AE6)

    def lambda_4AF8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4AF8)
    Sleep(1000)
    Return()

    # Function_11_4ABC end

    def Function_12_4B0A(): pass

    label("Function_12_4B0A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4B28")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4B28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x3, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4B3C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4B3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4B50")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4B50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4B64")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4B64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4B78")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4B78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4B8C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4B8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4BA0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4BA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4BB4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4BB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4BC8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4BC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xB, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4BDC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4BDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4BF0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4BF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4C04")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4C04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4C18")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4C18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4C2C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4C2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4C40")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4C40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4C54")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4C54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4C68")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4C68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4C7C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4C7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4C90")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4C90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4CA4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4CA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x19, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4CB8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4CB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4CCC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4CCC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4CE0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4CE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4CF4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4CF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x24, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4D08")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4D08")

    Return()

    # Function_12_4B0A end

    def Function_13_4D09(): pass

    label("Function_13_4D09")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #111
        "\x07\x05Open the Door?\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_13_4D09 end

    def Function_14_4D62(): pass

    label("Function_14_4D62")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x12, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E38")
    OP_28(0x12, 0x4, 0x2)
    OP_82(0x82, 0x2)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_4E38")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #112
        (
            "\x07\x05#40WAll is one, and one is all...\x01",
            "All begins with one, and in\x01",
            "the end, it returns to one...\x01",
            "#500W \x01",
            "#40WOnly when you have released all of\x01",
            "the other doors shall this one open...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Call(0, 12)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4F4D")
    Call(0, 13)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F4A")
    Call(0, 15)

    label("loc_4F4A")

    Jump("loc_4F4D")

    label("loc_4F4D")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_14_4D62 end

    def Function_15_4F59(): pass

    label("Function_15_4F59")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x6, 0)
    OP_70(0x6, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x6)
    Sleep(500)

    def lambda_4FC2():
        OP_6B(4000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4FC2)
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

    # Function_15_4F59 end

    def Function_16_5012(): pass

    label("Function_16_5012")

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

    # Function_16_5012 end

    SaveToFile()

Try(main)
