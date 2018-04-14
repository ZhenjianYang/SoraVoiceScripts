from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3101_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60029",
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
        '',                                     # 8
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_C0",           # 01, 1
        "Function_2_8A6",          # 02, 2
        "Function_3_10C2",         # 03, 3
        "Function_4_1118",         # 04, 4
        "Function_5_116E",         # 05, 5
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BF")
    OP_99(0xFE, 0x0, 0xC, 0x7D0)
    Jump("Function_0_AA")

    label("loc_BF")

    Return()

    # Function_0_AA end

    def Function_1_C0(): pass

    label("Function_1_C0")

    OP_B5(0x0)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_6D(21160, 0, -32460, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(4250, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x9, 33300, 0, -32150, 270)
    SetChrPos(0xA, 34470, 0, -30990, 270)
    SetChrPos(0xB, 33870, 0, -34110, 270)
    SetChrPos(0xC, 35470, 0, -33030, 270)
    SetChrPos(0xD, 33840, 10, -30000, 270)
    SetChrPos(0xE, 35840, 10, -32150, 270)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xD, 7)
    SetChrChipByIndex(0xA, 25)
    SetChrChipByIndex(0x9, 28)
    SetChrChipByIndex(0xC, 25)
    SetChrChipByIndex(0xB, 7)
    SetChrChipByIndex(0xE, 7)
    SetChrFlags(0xF7, 0x40)
    SetChrFlags(0xF8, 0x40)
    SetChrFlags(0xF9, 0x40)
    SetChrPos(0x101, 35300, 0, -32150, 270)
    SetChrPos(0xF7, 39860, 0, -30640, 270)
    SetChrPos(0xF8, 42600, 0, -32910, 270)
    SetChrPos(0xF9, 40460, 0, -33870, 270)
    LoadEffect(0x0, "map\\\\snddst1.eff")
    SetChrChipByIndex(0x101, 18)
    SetChrChipByIndex(0x107, 21)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_259")
    OP_D2(0x70218, 0x70224, 0x1E)
    OP_D2(0x70219, 0x70225, 0x1F)
    OP_D2(0x7021A, 0x70226, 0x20)
    Jump("loc_277")

    label("loc_259")

    OP_D2(0x701D0, 0x701DC, 0x1E)
    OP_D2(0x701D1, 0x701DD, 0x1F)
    OP_D2(0x701D2, 0x701DE, 0x20)

    label("loc_277")

    SetChrChipByIndex(0xF7, 30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A1")
    OP_D2(0x701E8, 0x701F4, 0x21)
    OP_D2(0x701E9, 0x701F5, 0x22)
    Jump("loc_2B5")

    label("loc_2A1")

    OP_D2(0x70200, 0x7020C, 0x21)
    OP_D2(0x70201, 0x7020D, 0x22)

    label("loc_2B5")

    SetChrChipByIndex(0xF9, 33)
    FadeToBright(1000, 0)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xC, 0x0, 0x0, 0x2)
    OP_43(0xD, 0x0, 0x0, 0x2)
    OP_43(0xE, 0x0, 0x0, 0x2)

    def lambda_2F3():
        OP_8E(0xB, 0xF1E, 0x0, 0xFFFF7AC2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2F3)

    def lambda_30E():
        OP_8E(0xD, 0xF00, 0xA, 0xFFFF8AD0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_30E)

    def lambda_329():
        OP_8E(0x9, 0xCE4, 0x0, 0xFFFF826A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_329)

    def lambda_344():
        OP_8E(0xC, 0x155E, 0x0, 0xFFFF7EFA, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_344)

    def lambda_35F():
        OP_8E(0xA, 0x1176, 0x0, 0xFFFF86F2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_35F)

    def lambda_37A():
        OP_8E(0xE, 0x168A, 0x0, 0xFFFF826A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_37A)

    def lambda_395():
        OP_6B(3250, 2000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_395)
    Sleep(2500)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)

    def lambda_3BE():
        OP_8E(0x101, 0x4F4C, 0x0, 0xFFFF826A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BE)

    def lambda_3D9():
        OP_8E(0xF7, 0x41DC, 0x0, 0xFFFF86F2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3D9)

    def lambda_3F4():
        OP_8E(0xF8, 0x44C0, 0x0, 0xFFFF7F72, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_3F4)

    def lambda_40F():
        OP_8E(0xF9, 0x404C, 0x0, 0xFFFF7BB2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_40F)

    def lambda_42A():
        OP_6C(120000, 3000)
        ExitThread()

    QueueWorkItem(0xF7, 3, lambda_42A)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    ClearMapFlags(0x2000000)

    ChrTalk(    #0 op#5
        0x101,
        "#1005F#2P#3S呀──！\x05\x02",
    )

    SetChrChipByIndex(0x101, 20)
    OP_22(0x1F4, 0x0, 0x64)

    def lambda_469():
        OP_96(0x101, 0x3FAC, 0x5A, 0xFFFF826A, 0x7D0, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_469)
    SetChrFlags(0x101, 0x800)

    def lambda_48C():
        OP_6D(15300, 0, -32460, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_48C)
    OP_43(0xF7, 0x2, 0x1, 0x3)
    OP_99(0x101, 0x0, 0xA, 0x7D0)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(30)
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(80)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrChipByIndex(0xD, 6)
    SetChrChipByIndex(0xA, 24)
    SetChrChipByIndex(0x9, 27)
    SetChrChipByIndex(0xC, 24)
    SetChrChipByIndex(0xB, 6)
    SetChrChipByIndex(0xE, 6)

    def lambda_596():
        OP_95(0x9, 0x0, 0x0, 0x0, 0x5DC, 0x2710)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_596)

    def lambda_5B4():
        OP_95(0xA, 0x0, 0x0, 0x0, 0x5DC, 0x2710)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5B4)

    def lambda_5D2():
        OP_95(0xB, 0x0, 0x0, 0x0, 0x5DC, 0x2710)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5D2)

    def lambda_5F0():
        OP_95(0xC, 0x0, 0x0, 0x0, 0x5DC, 0x2710)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5F0)

    def lambda_60E():
        OP_95(0xE, 0x0, 0x0, 0x0, 0x5DC, 0x2710)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_60E)
    OP_95(0xD, 0x0, 0x0, 0x0, 0x5DC, 0x2710)
    OP_63(0x9)
    OP_63(0xA)
    OP_63(0xB)
    OP_63(0xC)
    OP_63(0xD)
    OP_63(0xE)

    def lambda_655():
        TurnDirection(0x9, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_655)

    def lambda_663():
        TurnDirection(0xA, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_663)

    def lambda_671():
        TurnDirection(0xB, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_671)

    def lambda_67F():
        TurnDirection(0xC, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_67F)

    def lambda_68D():
        TurnDirection(0xE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_68D)
    TurnDirection(0xD, 0x101, 400)
    Sleep(1000)

    def lambda_6A7():
        OP_8F(0x9, 0x2D8C, 0x0, 0xFFFF826A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6A7)

    def lambda_6C2():
        OP_8F(0xA, 0x307A, 0x0, 0xFFFF8AD0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6C2)

    def lambda_6DD():
        OP_8F(0xB, 0x3368, 0x0, 0xFFFF72D4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6DD)

    def lambda_6F8():
        OP_8F(0xC, 0x2F44, 0x0, 0xFFFF7A2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6F8)

    def lambda_713():
        OP_8F(0xE, 0x3264, 0x0, 0xFFFF810C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_713)

    def lambda_72E():
        OP_67(0, 6000, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_72E)
    OP_8F(0xD, 0x3674, 0xA, 0xFFFF90F2, 0x7D0, 0x0)
    OP_99(0x101, 0xA, 0xC, 0x7D0)
    ClearChrFlags(0x101, 0x800)

    ChrTalk(    #1
        0x101,
        "#1002F──看来终于觉悟了呢。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    ClearChrFlags(0xF7, 0x40)
    ClearChrFlags(0xF8, 0x40)
    ClearChrFlags(0xF9, 0x40)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7CB")

    ChrTalk(    #2
        0x106,
        "#057F稍微教训你们一下吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7EA")

    label("loc_7CB")


    ChrTalk(    #3
        0x103,
        "#525F稍微惩罚你们一下吧。\x02",
    )

    CloseMessageWindow()

    label("loc_7EA")


    def lambda_7F0():
        OP_92(0x9, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7F0)

    def lambda_805():
        OP_92(0xA, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_805)

    def lambda_81A():
        OP_92(0xB, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_81A)

    def lambda_82F():
        OP_92(0xC, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_82F)

    def lambda_844():
        OP_92(0xD, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_844)

    def lambda_859():
        OP_92(0xE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_859)
    Sleep(300)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    Battle(0x1EB, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_89E"),
        (SWITCH_DEFAULT, "loc_8A1"),
    )


    label("loc_89E")

    OP_B4(0x0)
    Return()

    label("loc_8A1")

    Call(1, 2)
    Return()

    # Function_1_C0 end

    def Function_2_8A6(): pass

    label("Function_2_8A6")

    EventBegin(0x0)
    LoadEffect(0x0, "map\\\\snddst1.eff")
    OP_6D(15300, 0, -32460, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(120000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 16300, 0, -32150, 270)
    SetChrPos(0xF7, 16860, 0, -30640, 270)
    SetChrPos(0xF8, 17600, 0, -32910, 270)
    SetChrPos(0xF9, 16460, 0, -33870, 270)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, 11660, 0, -32150, 315)
    SetChrPos(0xA, 12410, 0, -30000, 180)
    SetChrPos(0xB, 13160, 0, -36140, 270)
    SetChrPos(0xC, 12100, 0, -34260, 90)
    SetChrPos(0xD, 13940, 10, -28430, 135)
    SetChrPos(0xE, 13460, 0, -32350, 0)
    SetChrChipByIndex(0xD, 23)
    SetChrChipByIndex(0xA, 26)
    SetChrChipByIndex(0x9, 29)
    SetChrChipByIndex(0xC, 26)
    SetChrChipByIndex(0xB, 23)
    SetChrChipByIndex(0xE, 23)
    SetChrSubChip(0x9, 0)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0xD, 0)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0x101, 18)
    SetChrChipByIndex(0x107, 21)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A2E")
    OP_D2(0x70218, 0x70224, 0x1E)
    OP_D2(0x70219, 0x70225, 0x1F)
    OP_D2(0x7021A, 0x70226, 0x20)
    Jump("loc_A4C")

    label("loc_A2E")

    OP_D2(0x701D0, 0x701DC, 0x1E)
    OP_D2(0x701D1, 0x701DD, 0x1F)
    OP_D2(0x701D2, 0x701DE, 0x20)

    label("loc_A4C")

    SetChrChipByIndex(0xF7, 30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A76")
    OP_D2(0x701E8, 0x701F4, 0x21)
    OP_D2(0x701E9, 0x701F5, 0x22)
    Jump("loc_A8A")

    label("loc_A76")

    OP_D2(0x70200, 0x7020C, 0x21)
    OP_D2(0x70201, 0x7020D, 0x22)

    label("loc_A8A")

    SetChrChipByIndex(0xF9, 33)
    OP_0D()

    ChrTalk(    #4
        0x101,
        "#1002F这样一来总算……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ADC")

    ChrTalk(    #5
        0x105,
        "#047F嗯，已经分出胜负了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B07")

    label("loc_ADC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B07")

    ChrTalk(    #6
        0x104,
        "#030F嗯，已经收拾好了。\x02",
    )

    CloseMessageWindow()

    label("loc_B07")


    ChrTalk(    #7
        0x107,
        "#065F想、想不到还会合体……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_B6A")

    ChrTalk(    #8
        0x106,
        (
            "#053F算了，有此教训以后\x01",
            "应该不会再敢来村里了吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9C")

    label("loc_B6A")


    ChrTalk(    #9
        0x103,
        (
            "#026F有此教训以后\x01",
            "应该不会再敢来村里了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9C")

    OP_96(0xF7, 0x3D04, 0x0, 0xFFFF8AD0, 0x3E8, 0x2710)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_BE1")
    SetChrChipByIndex(0x106, 32)
    SetChrFlags(0x106, 0x800)
    OP_43(0xF7, 0x2, 0x1, 0x4)
    OP_99(0x106, 0x0, 0x7, 0x7D0)
    WaitChrThread(0x106, 0x0)
    SetChrSubChip(0x106, 0)
    Jump("loc_C05")

    label("loc_BE1")

    SetChrChipByIndex(0x103, 32)
    SetChrFlags(0x103, 0x800)
    OP_43(0xF7, 0x2, 0x1, 0x5)
    OP_99(0x103, 0x0, 0x9, 0x7D0)
    WaitChrThread(0x103, 0x0)
    SetChrSubChip(0x103, 9)

    label("loc_C05")

    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(120)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(60)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x9, 0x101, 0)
    TurnDirection(0xA, 0x101, 0)
    TurnDirection(0xB, 0x101, 0)
    TurnDirection(0xC, 0x101, 0)
    TurnDirection(0xD, 0x101, 0)
    TurnDirection(0xE, 0x101, 0)
    SetChrChipByIndex(0xD, 6)
    SetChrChipByIndex(0xA, 24)
    SetChrChipByIndex(0x9, 27)
    SetChrChipByIndex(0xC, 24)
    SetChrChipByIndex(0xB, 6)
    SetChrChipByIndex(0xE, 6)

    def lambda_CE7():
        OP_95(0x9, 0x0, 0x0, 0x0, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_CE7)

    def lambda_D05():
        OP_95(0xA, 0x0, 0x0, 0x0, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_D05)

    def lambda_D23():
        OP_95(0xB, 0x0, 0x0, 0x0, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D23)

    def lambda_D41():
        OP_95(0xC, 0x0, 0x0, 0x0, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D41)

    def lambda_D5F():
        OP_95(0xE, 0x0, 0x0, 0x0, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_D5F)
    OP_95(0xD, 0x0, 0x0, 0x0, 0x3E8, 0x2710)
    OP_63(0x9)
    OP_63(0xA)
    OP_63(0xB)
    OP_63(0xC)
    OP_63(0xD)
    OP_63(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_DF0")

    ChrTalk(    #10
        0x106,
        (
            "#057F#1P下次再来的话\x01",
            "就要你们的小命。\x02\x03",

            "#054F明白的话，就快滚吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E3C")

    label("loc_DF0")


    ChrTalk(    #11
        0x103,
        (
            "#027F#1P下次再来的话\x01",
            "我会更加疼爱你们的。\x02\x03",

            "#024F明白的话，就赶快走吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_E6A")
    SetChrChipByIndex(0x106, 32)
    SetChrFlags(0x106, 0x800)
    OP_43(0xF7, 0x2, 0x1, 0x4)
    OP_99(0x106, 0x0, 0x7, 0x7D0)
    WaitChrThread(0x106, 0x0)
    ClearChrFlags(0x106, 0x800)
    Jump("loc_E93")

    label("loc_E6A")

    SetChrChipByIndex(0x103, 32)
    SetChrFlags(0x103, 0x800)
    OP_43(0xF7, 0x2, 0x1, 0x5)
    OP_99(0x103, 0x0, 0x9, 0x7D0)
    WaitChrThread(0x103, 0x0)
    SetChrSubChip(0x103, 9)
    ClearChrFlags(0x103, 0x800)

    label("loc_E93")


    def lambda_E99():
        OP_95(0x9, 0x0, 0x0, 0x0, 0x258, 0x2710)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E99)

    def lambda_EB7():
        OP_95(0xA, 0x0, 0x0, 0x0, 0x258, 0x2710)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_EB7)

    def lambda_ED5():
        OP_95(0xB, 0x0, 0x0, 0x0, 0x258, 0x2710)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_ED5)

    def lambda_EF3():
        OP_95(0xC, 0x0, 0x0, 0x0, 0x258, 0x2710)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_EF3)

    def lambda_F11():
        OP_95(0xE, 0x0, 0x0, 0x0, 0x258, 0x2710)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_F11)
    OP_95(0xD, 0x0, 0x0, 0x0, 0x3E8, 0x2710)
    OP_62(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xC, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xD, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xC, 0x0, 0x0, 0x2)
    OP_43(0xD, 0x0, 0x0, 0x2)
    OP_43(0xE, 0x0, 0x0, 0x2)
    SetChrChipByIndex(0xD, 7)
    SetChrChipByIndex(0xA, 25)
    SetChrChipByIndex(0x9, 28)
    SetChrChipByIndex(0xC, 25)
    SetChrChipByIndex(0xB, 7)
    SetChrChipByIndex(0xE, 7)

    def lambda_FFA():
        OP_8E(0x9, 0x10E0, 0x0, 0xFFFF8E2C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_FFA)
    Sleep(100)

    def lambda_101A():
        OP_8E(0xA, 0x1680, 0x0, 0xFFFF9926, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_101A)

    def lambda_1035():
        OP_8E(0xB, 0x1950, 0x0, 0xFFFF63DE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1035)
    Sleep(100)

    def lambda_1055():
        OP_8E(0xC, 0x1464, 0x0, 0xFFFF7306, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1055)

    def lambda_1070():
        OP_8E(0xD, 0x20BC, 0x0, 0xFFFFA8C6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1070)

    def lambda_108B():
        OP_8E(0xE, 0x1504, 0x0, 0xFFFF8D6E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_108B)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T3221   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_8A6 end

    def Function_3_10C2(): pass

    label("Function_3_10C2")

    Sleep(700)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0x55, 0x0, 0x5A)
    PlayEffect(0x0, 0xFF, 0xFF, 15300, 90, -32150, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    Return()

    # Function_3_10C2 end

    def Function_4_1118(): pass

    label("Function_4_1118")

    Sleep(500)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0x55, 0x0, 0x5A)
    PlayEffect(0x0, 0xFF, 0xFF, 14230, 30, -30150, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    Return()

    # Function_4_1118 end

    def Function_5_116E(): pass

    label("Function_5_116E")

    Sleep(200)
    OP_22(0x1F6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 13740, 20, -30120, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_5_116E end

    SaveToFile()

Try(main)
