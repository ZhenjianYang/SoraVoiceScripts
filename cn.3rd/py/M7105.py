from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7105   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7105.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60222",
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
        '死亡重击者',                           # 9
        '死亡重击者',                           # 10
        '死亡重击者',                           # 11
        '死亡重击者',                           # 12
        '死亡重击者',                           # 13
        '凯文',                                 # 14
        '封印石⑧',                             # 15
        '',                                     # 16
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
        'ED6_DT29/CH14120 ._CH',             # 00
        'ED6_DT29/CH14120 ._CH',             # 01
        'ED6_DT27/CH04080 ._CH',             # 02
        'ED6_DT27/CH04081 ._CH',             # 03
        'ED6_DT27/CH04085 ._CH',             # 04
        'ED6_DT27/CH03154 ._CH',             # 05
        'ED6_DT26/CH20668 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT29/CH14120P._CP',             # 00
        'ED6_DT29/CH14120P._CP',             # 01
        'ED6_DT27/CH04080P._CP',             # 02
        'ED6_DT27/CH04081P._CP',             # 03
        'ED6_DT27/CH04085P._CP',             # 04
        'ED6_DT27/CH03154P._CP',             # 05
        'ED6_DT26/CH20668P._CP',             # 06
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -8600,
        Y                   = 7000,
        Z                   = 52220,
        Range               = 8189,
        Unknown_10          = 0x2AF8,
        Unknown_14          = 0xDB60,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )


    ScpFunction(
        "Function_0_1E2",          # 00, 0
        "Function_1_1E3",          # 01, 1
        "Function_2_210",          # 02, 2
        "Function_3_221",          # 03, 3
        "Function_4_1385",         # 04, 4
        "Function_5_13DF",         # 05, 5
        "Function_6_143F",         # 06, 6
        "Function_7_149F",         # 07, 7
        "Function_8_14FF",         # 08, 8
        "Function_9_155F",         # 09, 9
        "Function_10_15BF",        # 0A, 10
    )


    def Function_0_1E2(): pass

    label("Function_0_1E2")

    Return()

    # Function_0_1E2 end

    def Function_1_1E3(): pass

    label("Function_1_1E3")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFF1D70, 0x230088)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x501, 2)), scpexpr(EXPR_END)), "loc_20F")
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x800, 0x0)
    ExitThread()
    OP_6F(0x0, 120)

    label("loc_20F")

    Return()

    # Function_1_1E3 end

    def Function_2_210(): pass

    label("Function_2_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x501, 2)), scpexpr(EXPR_END)), "loc_218")
    Return()

    label("loc_218")

    Call(0, 3)
    Call(0, 10)
    Return()

    # Function_2_210 end

    def Function_3_221(): pass

    label("Function_3_221")

    EventBegin(0x0)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    LoadEffect(0x2, "monster\\msc1000.eff")
    OP_E0(242, 0x47, 0x2)
    OP_E0(243, 0x48, 0x2)
    OP_E0(244, 0x49, 0x2)
    OP_E0(245, 0x4A, 0x2)
    Fade(1000)
    OP_6D(1650, 10000, 76160, 0)
    OP_67(0, 6850, -10000, 0)
    OP_6B(5500, 0)
    OP_6C(57000, 0)
    OP_6E(382, 0)

    def lambda_2BB():
        OP_6D(1650, 10000, 66310, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2BB)

    def lambda_2D3():
        OP_67(0, 8850, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xF3, 0, lambda_2D3)

    def lambda_2EB():
        OP_6B(6140, 6000)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2EB)

    def lambda_2FB():
        OP_6E(382, 6000)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_2FB)
    SetChrPos(0x10F, 0, 8000, 54580, 0)
    SetChrPos(0xF3, 330, 8000, 53450, 0)
    SetChrPos(0xF4, -1200, 8000, 52990, 0)
    SetChrPos(0xF5, -220, 8000, 51620, 0)
    Sleep(1000)

    def lambda_354():
        OP_8E(0xFE, 0x0, 0x1F72, 0x1022A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_354)
    Sleep(50)

    def lambda_374():
        OP_8E(0xFE, 0x4B0, 0x1F72, 0xFEB9, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF3, 1, lambda_374)
    Sleep(150)

    def lambda_394():
        OP_8E(0xFE, 0xFFFFFAEC, 0x1F72, 0xFC8A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_394)
    Sleep(50)

    def lambda_3B4():
        OP_8E(0xFE, 0xFFFFFF42, 0x1F72, 0xF898, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_3B4)
    WaitChrThread(0x10F, 0x0)
    Fade(500)
    OP_6D(1020, 8050, 66150, 0)
    OP_67(0, 5930, -10000, 0)
    OP_6B(3220, 0)
    OP_6C(45000, 0)
    OP_6E(255, 0)
    OP_0D()
    WaitChrThread(0x10F, 0x1)
    Sleep(300)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_43D():
        OP_6D(910, 11600, 106980, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_43D)

    def lambda_455():
        OP_67(0, 2670, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_455)

    def lambda_46D():
        OP_6B(4580, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_46D)

    def lambda_47D():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_47D)

    def lambda_48D():
        OP_6E(276, 4000)
        ExitThread()

    QueueWorkItem(0xF3, 1, lambda_48D)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x10F,
        "#1444F#1P啊……！\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_6D(1020, 8050, 66150, 0)
    OP_67(0, 5930, -10000, 0)
    OP_6B(3220, 0)
    OP_6C(45000, 0)
    OP_6E(255, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_547")

    ChrTalk(    #1
        0x10D,
        (
            "#277F#6P嗯……\x01",
            "这也许是出口。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63C")

    label("loc_547")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_584")

    ChrTalk(    #2
        0x10E,
        (
            "#170F#6P啊……\x01",
            "这可能是出口呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63C")

    label("loc_584")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C2")

    ChrTalk(    #3
        0x105,
        (
            "#1382F#6P难道……\x01",
            "到达出口了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63C")

    label("loc_5C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_601")

    ChrTalk(    #4
        0x102,
        (
            "#1500F看起来……\x01",
            "这儿就是出口呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63C")

    label("loc_601")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63C")

    ChrTalk(    #5
        0x107,
        (
            "#560F难、难道……\x01",
            "那就是出口！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63C")


    ChrTalk(    #6
        0x10F,
        (
            "#1447F#5P……嗯嗯。\x01",
            "好像没错。\x02\x03",

            "#1448F也许……\x01",
            "凯文他们已经……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_20(0x3E8)
    OP_6D(680, 8050, 70000, 0)
    OP_67(0, 6020, -10000, 0)
    OP_6B(3640, 0)
    OP_6C(45000, 0)
    OP_6E(258, 0)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 0, 8150, 73750, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73E")
    OP_62(0xF2, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7A5")

    label("loc_73E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_766")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7A5")

    label("loc_766")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78E")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7A5")

    label("loc_78E")

    OP_62(0xF2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_7A5")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D2")
    OP_62(0xF3, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_839")

    label("loc_7D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FA")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_839")

    label("loc_7FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_822")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_839")

    label("loc_822")

    OP_62(0xF3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_839")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_866")
    OP_62(0xF4, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8CD")

    label("loc_866")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88E")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8CD")

    label("loc_88E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B6")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8CD")

    label("loc_8B6")

    OP_62(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_8CD")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FA")
    OP_62(0xF5, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_961")

    label("loc_8FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_922")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_961")

    label("loc_922")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94A")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_961")

    label("loc_94A")

    OP_62(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_961")

    Sleep(1000)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 7)
    SetChrSubChip(0x10F, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF3, 8)
    SetChrSubChip(0xF3, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF4, 9)
    SetChrSubChip(0xF4, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF5, 10)
    SetChrSubChip(0xF5, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #7
        0x10F,
        "#1441F#6P……哎………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A2A")
    OP_A2(0x3)

    ChrTalk(    #8
        0x10B,
        (
            "#212F#6P哼……\x01",
            "看来不容我们轻易通过这里啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B61")

    label("loc_A2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A76")
    OP_A2(0x0)

    ChrTalk(    #9
        0x107,
        (
            "#062F#6P看、看起来\x01",
            "敌人不准我们轻易通过呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B61")

    label("loc_A76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC7")
    OP_A2(0x4)

    ChrTalk(    #10
        0x102,
        (
            "#1502F#6P……看来，\x01",
            "对方不容我们这么简单就通过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B61")

    label("loc_AC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B18")
    OP_A2(0x5)

    ChrTalk(    #11
        0x105,
        (
            "#1162F#6P……看来，\x01",
            "对方不容我们这么简单就通过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B61")

    label("loc_B18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B61")
    OP_A2(0x1)

    ChrTalk(    #12
        0x10E,
        (
            "#178F#6P……好像还是不能\x01",
            "这么简单就通过呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B61")

    OP_1D(0x9A)
    OP_22(0x85, 0x1, 0x64)

    def lambda_B6E():

        label("loc_B6E")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_B6E")

    QueueWorkItem2(0xF3, 0, lambda_B6E)

    def lambda_B89():
        OP_6D(1200, 8050, 71600, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_B89)

    def lambda_BA1():
        OP_67(0, 5400, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_BA1)

    def lambda_BB9():
        OP_6B(3510, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_BB9)

    def lambda_BC9():
        OP_6E(258, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_BC9)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 0, 5050, 73750, 180)
    OP_43(0x15, 0x0, 0x0, 0x4)
    WaitChrThread(0x15, 0x0)
    OP_44(0xF3, 0x0)
    OP_23(0x85)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2E")
    OP_62(0xF2, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C95")

    label("loc_C2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C56")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C95")

    label("loc_C56")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7E")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C95")

    label("loc_C7E")

    OP_62(0xF2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_C95")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC2")
    OP_62(0xF3, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D29")

    label("loc_CC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEA")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D29")

    label("loc_CEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D12")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D29")

    label("loc_D12")

    OP_62(0xF3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D29")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D56")
    OP_62(0xF4, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DBD")

    label("loc_D56")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7E")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DBD")

    label("loc_D7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA6")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DBD")

    label("loc_DA6")

    OP_62(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_DBD")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DEA")
    OP_62(0xF5, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E51")

    label("loc_DEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E12")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E51")

    label("loc_E12")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3A")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E51")

    label("loc_E3A")

    OP_62(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_E51")

    Sleep(1000)

    ChrTalk(    #13
        0x10F,
        "#1444F#6P……咦……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB9")

    ChrTalk(    #14
        0x107,
        "#065F#6P凯、凯文哥哥……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_F71")

    label("loc_EB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EF8")

    ChrTalk(    #15
        0x10E,
        "#173F#6P凯、凯文神父……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_F71")

    label("loc_EF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F34")

    ChrTalk(    #16
        0x102,
        "#1504F#6P凯文先生……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_F71")

    label("loc_F34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F71")

    ChrTalk(    #17
        0x105,
        "#1164F#6P凯、凯文先生……！？\x02",
    )

    CloseMessageWindow()

    label("loc_F71")


    ChrTalk(    #18
        0x15,
        "#1842F#5P………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x15, 4)
    SetChrSubChip(0x15, 0)

    def lambda_FBE():

        label("loc_FBE")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_FBE")

    QueueWorkItem2(0x15, 2, lambda_FBE)
    OP_0D()
    PlayEffect(0x2, 0x0, 0xFF, 0, 8050, 73750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, 0, 8050, 77000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xFF, -2200, 8050, 75500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x3, 0xFF, 2200, 8050, 75500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x4, 0xFF, -4500, 8050, 74000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x5, 0xFF, 4500, 8050, 74000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6D(0, 8800, 69800, 0)
    OP_67(0, 4019, -10000, 0)
    OP_6B(4090, 0)
    OP_6C(0, 0)
    OP_6E(254, 0)
    SetChrPos(0x10F, 0, 8050, 66090, 0)
    SetChrPos(0xF3, 1200, 8050, 65209, 0)
    SetChrPos(0xF4, -1300, 8050, 64650, 0)
    SetChrPos(0xF5, 0, 8050, 63640, 0)
    OP_22(0x85, 0x1, 0x64)

    def lambda_11E0():

        label("loc_11E0")

        OP_7C(0x32, 0x32, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_11E0")

    QueueWorkItem2(0xF3, 0, lambda_11E0)

    def lambda_11FB():
        OP_6D(0, 8800, 70100, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_11FB)

    def lambda_1213():
        OP_67(0, 2310, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1213)

    def lambda_122B():
        OP_6B(4090, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_122B)

    def lambda_123B():
        OP_6E(230, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_123B)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x10, 0, 5050, 77000, 180)
    SetChrPos(0x11, -2200, 5050, 75500, 180)
    SetChrPos(0x12, 2200, 5050, 75500, 180)
    SetChrPos(0x13, -4500, 5050, 74000, 180)
    SetChrPos(0x14, 4500, 5050, 74000, 180)
    OP_43(0x10, 0x0, 0x0, 0x5)
    OP_43(0x11, 0x0, 0x0, 0x6)
    OP_43(0x12, 0x0, 0x0, 0x7)
    OP_43(0x13, 0x0, 0x0, 0x8)
    OP_43(0x14, 0x0, 0x0, 0x9)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x14, 0x0)
    Fade(1000)
    LoadEffect(0x1, "map\\mp250_00.eff")
    OP_82(0x0, 0x2)
    WaitChrThread(0x10F, 0x0)
    OP_44(0xF3, 0x0)
    OP_23(0x85)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x15, 2)
    SetChrSubChip(0x15, 0)
    OP_44(0x15, 0x2)
    OP_0D()
    Sleep(800)

    ChrTalk(    #19
        0x10F,
        "#1449F#6P#3S……凯文……！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    Battle(0x13C, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_221 end

    def Function_4_1385(): pass

    label("Function_4_1385")

    SetChrFlags(0xFE, 0x20)
    PlayEffect(0x1, 0x4, 0xFF, 0, 8150, 73750, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_4_1385 end

    def Function_5_13DF(): pass

    label("Function_5_13DF")

    PlayEffect(0x1, 0xFF, 0xFF, 0, 8050, 77000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_141A():

        label("loc_141A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_141A")

    QueueWorkItem2(0xFE, 1, lambda_141A)
    OP_91(0xFE, 0x0, 0xDAC, 0x0, 0x320, 0x0)
    OP_82(0x1, 0x2)
    Return()

    # Function_5_13DF end

    def Function_6_143F(): pass

    label("Function_6_143F")

    PlayEffect(0x1, 0xFF, 0xFF, -2200, 8150, 75500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_147A():

        label("loc_147A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_147A")

    QueueWorkItem2(0xFE, 1, lambda_147A)
    OP_91(0xFE, 0x0, 0xDAC, 0x0, 0x320, 0x0)
    OP_82(0x2, 0x2)
    Return()

    # Function_6_143F end

    def Function_7_149F(): pass

    label("Function_7_149F")

    PlayEffect(0x1, 0xFF, 0xFF, 2200, 8150, 75500, 1, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_14DA():

        label("loc_14DA")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_14DA")

    QueueWorkItem2(0xFE, 1, lambda_14DA)
    OP_91(0xFE, 0x0, 0xDAC, 0x0, 0x320, 0x0)
    OP_82(0x3, 0x2)
    Return()

    # Function_7_149F end

    def Function_8_14FF(): pass

    label("Function_8_14FF")

    PlayEffect(0x1, 0xFF, 0xFF, -4500, 8050, 74000, 1, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_153A():

        label("loc_153A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_153A")

    QueueWorkItem2(0xFE, 1, lambda_153A)
    OP_91(0xFE, 0x0, 0xDAC, 0x0, 0x320, 0x0)
    OP_82(0x4, 0x2)
    Return()

    # Function_8_14FF end

    def Function_9_155F(): pass

    label("Function_9_155F")

    PlayEffect(0x1, 0xFF, 0xFF, 4500, 8050, 74000, 1, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_159A():

        label("loc_159A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_159A")

    QueueWorkItem2(0xFE, 1, lambda_159A)
    OP_91(0xFE, 0x0, 0xDAC, 0x0, 0x320, 0x0)
    OP_82(0x5, 0x2)
    Return()

    # Function_9_155F end

    def Function_10_15BF(): pass

    label("Function_10_15BF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    OP_E0(242, 0x47, 0x2)
    OP_E0(243, 0x48, 0x2)
    OP_E0(244, 0x49, 0x2)
    OP_E0(245, 0x4A, 0x2)
    SetChrPos(0x10F, -240, 8050, 67870, 0)
    SetChrPos(0xF3, 1330, 8050, 66380, 0)
    SetChrPos(0xF4, -1330, 8050, 66880, 0)
    SetChrPos(0xF5, 40, 8050, 65430, 0)
    SetChrChipByIndex(0x10F, 7)
    SetChrSubChip(0x10F, 0)
    SetChrChipByIndex(0xF3, 8)
    SetChrSubChip(0xF3, 0)
    SetChrChipByIndex(0xF4, 9)
    SetChrSubChip(0xF4, 0)
    SetChrChipByIndex(0xF5, 10)
    SetChrSubChip(0xF5, 0)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    OP_A3(0x3)
    OP_A3(0x4)
    OP_A3(0x5)
    OP_6D(1220, 8050, 65800, 0)
    OP_67(0, 5530, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(135000, 0)
    OP_6E(285, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    ClearChrFlags(0x16, 0x80)
    OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x16, -260, 9300, 69960, 0)
    PlayEffect(0x1, 0x7, 0x16, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x6, 0x16, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B0")
    OP_62(0xF2, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1817")

    label("loc_17B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D8")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1817")

    label("loc_17D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1800")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1817")

    label("loc_1800")

    OP_62(0xF2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1817")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1844")
    OP_62(0xF3, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18AB")

    label("loc_1844")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_186C")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18AB")

    label("loc_186C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1894")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18AB")

    label("loc_1894")

    OP_62(0xF3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_18AB")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D8")
    OP_62(0xF4, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_193F")

    label("loc_18D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1900")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_193F")

    label("loc_1900")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1928")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_193F")

    label("loc_1928")

    OP_62(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_193F")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_196C")
    OP_62(0xF5, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_19D3")

    label("loc_196C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1994")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_19D3")

    label("loc_1994")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19BC")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_19D3")

    label("loc_19BC")

    OP_62(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_19D3")

    Sleep(1000)

    ChrTalk(    #20
        0x10F,
        "#1444F#5P啊……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 65535)
    SetChrSubChip(0x0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 65535)
    SetChrSubChip(0x1, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 65535)
    SetChrSubChip(0x2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)

    def lambda_1A50():
        OP_6D(1130, 8050, 67300, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1A50)
    OP_8E(0x10F, 0xFFFFFEE8, 0x1F72, 0x10CFC, 0x3E8, 0x0)
    WaitChrThread(0x10F, 0x1)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x10F, 6)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x16, 0x64, 0x238C, 0x10E5A, 0x1F4, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    SetChrFlags(0x16, 0x80)
    OP_0D()
    Sleep(150)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x00得到了\x1F\x59\x03\x07\x00。\x02",
    )

    Jump("loc_1AF5")

    label("loc_1AF5")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x359, 1)
    Fade(250)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(300)
    OP_22(0x6C, 0x0, 0x64)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_B0(0x0, 0x19)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x78)
    Sleep(500)
    Fade(500)
    OP_6D(910, 11600, 106980, 0)
    OP_67(0, 2670, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(276, 0)

    def lambda_1B8E():
        OP_6B(4600, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1B8E)
    OP_73(0x0)
    OP_22(0x9A, 0x0, 0x64)
    OP_23(0x6C)
    WaitChrThread(0x10F, 0x0)
    SetChrPos(0x10F, -360, 8050, 68500, 0)
    SetChrPos(0xF3, 470, 8050, 66800, 0)
    SetChrPos(0xF4, -1590, 8050, 66500, 0)
    SetChrPos(0xF5, -660, 8050, 65500, 0)
    Sleep(1000)
    Fade(500)
    OP_6D(790, 8050, 68460, 0)
    OP_67(0, 5810, -10000, 0)
    OP_6B(3650, 0)
    OP_6C(45000, 0)
    OP_6E(224, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CBE")
    OP_A2(0x2)

    ChrTalk(    #22
        0x10D,
        (
            "#272F#12P看来……\x01",
            "所谓的试炼已经结束了。\x02\x03",

            "#270F但是……\x01",
            "居然有能变得与\x01",
            "神父如此相像的魔物啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF1")

    label("loc_1CBE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D45")
    OP_A2(0x1)

    ChrTalk(    #23
        0x10E,
        (
            "#176F#12P看来……\x01",
            "试炼到此就结束了吧。\x02\x03",

            "#178F不过，\x01",
            "真没想到居然有能变得\x01",
            "与神父如此相像的魔物。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF1")

    label("loc_1D45")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DD6")
    OP_A2(0x4)

    ChrTalk(    #24
        0x102,
        (
            "#1505F#12P看来……\x01",
            "那个试炼已经完成了呢。\x02\x03",

            "#1503F不过话说回来，\x01",
            "竟然有能变得与凯文先生\x01",
            "如此相像的魔物啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF1")

    label("loc_1DD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E65")
    OP_A2(0x3)

    ChrTalk(    #25
        0x10B,
        (
            "#413F#12P看、看起来，\x01",
            "那个试炼已经结束了吧。\x02\x03",

            "#212F不过话说回来，\x01",
            "竟然有能变成与神父\x01",
            "这么相像的魔物啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF1")

    label("loc_1E65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EF1")
    OP_A2(0x5)

    ChrTalk(    #26
        0x105,
        (
            "#1167F#12P看起来……\x01",
            "试炼到此就结束了吧。\x02\x03",

            "#1163F不过，没想到\x01",
            "居然有能变得和凯文先生\x01",
            "一模一样的魔物……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EF1")

    OP_8C(0x10F, 180, 400)
    Sleep(300)

    ChrTalk(    #27
        0x10F,
        (
            "#1446F#5P………嗯……………\x02\x03",

            "#1445F……啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x10F, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(300)
    Fade(500)
    OP_22(0x20C, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 5)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F91")
    OP_62(0xF3, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1FF8")

    label("loc_1F91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FB9")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1FF8")

    label("loc_1FB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FE1")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1FF8")

    label("loc_1FE1")

    OP_62(0xF3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1FF8")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2025")
    OP_62(0xF4, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_208C")

    label("loc_2025")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_204D")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_208C")

    label("loc_204D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2075")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_208C")

    label("loc_2075")

    OP_62(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_208C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20B9")
    OP_62(0xF5, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2120")

    label("loc_20B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20E1")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2120")

    label("loc_20E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2109")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2120")

    label("loc_2109")

    OP_62(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2120")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_217E")
    OP_A2(0x0)

    ChrTalk(    #28
        0x107,
        (
            "#065F#12P莉、莉丝姐姐！？\x02\x03",

            "你、你、你不要紧吧！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2327")

    label("loc_217E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21EF")
    OP_A2(0x5)

    ChrTalk(    #29
        0x105,
        (
            "#1164F#12P莉丝小姐……！？\x02\x03",

            "#1163F你、你不要紧吧？\x01",
            "是不是哪儿受伤了……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2327")

    label("loc_21EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2254")
    OP_A2(0x3)

    ChrTalk(    #30
        0x10B,
        (
            "#213F#12P等、等一下！\x02\x03",

            "#214F怎么了！？\x01",
            "是不是哪儿受伤了……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2327")

    label("loc_2254")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22BF")
    OP_A2(0x4)

    ChrTalk(    #31
        0x102,
        (
            "#1504F#12P莉丝小姐……！？\x02\x03",

            "#1502F你没事吧？\x01",
            "是不是哪儿受伤了……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2327")

    label("loc_22BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2327")
    OP_A2(0x1)

    ChrTalk(    #32
        0x10E,
        (
            "#173F#12P莉丝小姐……！？\x02\x03",

            "#178F你不要紧吧？\x01",
            "是不是哪儿受伤了……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2327")


    ChrTalk(    #33
        0x10F,
        (
            "#1806F#5P没、没事，只是……\x02\x03",

            "知道那个不是本人之后……\x01",
            "一放心下来就有些恍惚而已……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_62(0x10F, 0xE6, 1200, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    OP_62(0x10F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #34
        0x10F,
        (
            "#1800F#5P总、总之……\x01",
            "那个令人毛骨悚然的炮台，\x01",
            "很可能又是敌人布下的圈套。\x02\x03",

            "#1443F也不知道凯文他们怎么样了。\x01",
            "总之，我们赶快从这门出去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24E4")

    ChrTalk(    #35
        0x105,
        (
            "#1382F#12P没、没错……\x02\x03",

            "#1165F（呵呵，\x01",
            "  看来她挺担心凯文先生的事情呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2630")

    label("loc_24E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2551")

    ChrTalk(    #36
        0x10B,
        (
            "#213F#12P嗯、嗯……\x02\x03",

            "#210F（嘿嘿，\x01",
            "  看来她挺挂念那个冒牌神父嘛。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2630")

    label("loc_2551")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25C0")

    ChrTalk(    #37
        0x102,
        (
            "#1500F#12P嗯，是啊。\x02\x03",

            "#1513F（……她好像很担心\x01",
            "  凯文先生的事情呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2630")

    label("loc_25C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2630")

    ChrTalk(    #38
        0x10E,
        (
            "#170F#12P是啊……没错。\x02\x03",

            "#179F（呵呵，\x01",
            "  看来她挺担心凯文神父的事情嘛。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2630")

    OP_A2(0x280A)
    OP_28(0x31, 0x1, 0x8)
    OP_28(0x31, 0x1, 0x10)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_10_15BF end

    SaveToFile()

Try(main)
