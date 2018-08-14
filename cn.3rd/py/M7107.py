from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7107   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7107.x',
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
        '黑骑士',                               # 9
        '',                                     # 10
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
        'ED6_DT27/CH03440 ._CH',             # 00
        'ED6_DT27/CH04455 ._CH',             # 01
        'ED6_DT27/CH04080 ._CH',             # 02
        'ED6_DT27/CH04082 ._CH',             # 03
        'ED6_DT26/CH20724 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT27/CH03440P._CP',             # 00
        'ED6_DT27/CH04455P._CP',             # 01
        'ED6_DT27/CH04080P._CP',             # 02
        'ED6_DT27/CH04082P._CP',             # 03
        'ED6_DT26/CH20724P._CP',             # 04
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -4450,
        Y                   = -1000,
        Z                   = 15020,
        Range               = 4070,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x4858,
        Unknown_18          = 0x0,
        Unknown_1C          = 15,
    )


    DeclActor(
        TriggerX            = 7800,
        TriggerZ            = 0,
        TriggerY            = -80,
        TriggerRange        = 1000,
        ActorX              = 7800,
        ActorZ              = 2000,
        ActorY              = -80,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 1500,
        TriggerY            = 33300,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 2500,
        ActorY              = 33300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_15A",          # 00, 0
        "Function_1_1A4",          # 01, 1
        "Function_2_234",          # 02, 2
        "Function_3_35A",          # 03, 3
        "Function_4_3B4",          # 04, 4
        "Function_5_75F",          # 05, 5
        "Function_6_78B",          # 06, 6
        "Function_7_7BC",          # 07, 7
        "Function_8_7ED",          # 08, 8
        "Function_9_81E",          # 09, 9
        "Function_10_C44",         # 0A, 10
        "Function_11_C70",         # 0B, 11
        "Function_12_CA1",         # 0C, 12
        "Function_13_CD2",         # 0D, 13
        "Function_14_D03",         # 0E, 14
        "Function_15_39C6",        # 0F, 15
        "Function_16_3FB1",        # 10, 16
        "Function_17_40FC",        # 11, 17
        "Function_18_42B5",        # 12, 18
        "Function_19_4393",        # 13, 19
        "Function_20_4474",        # 14, 20
        "Function_21_458A",        # 15, 21
    )


    def Function_0_15A(): pass

    label("Function_0_15A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_179")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_172"),
        (SWITCH_DEFAULT, "loc_179"),
    )


    label("loc_172")

    Event(0, 18)
    Jump("loc_179")

    label("loc_179")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A3")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A3")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_1A3")

    Return()

    # Function_0_15A end

    def Function_1_1A4(): pass

    label("Function_1_1A4")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE0C00, 0x23008A)
    OP_1B(0x2, 0x0, 0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E5")
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x85, 0x0)

    label("loc_1E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F4")
    Jump("loc_21A")

    label("loc_1F4")

    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_6F(0x0, 120)
    OP_6F(0x1, 120)
    OP_72(0x800, 0x0)
    ExitThread()
    OP_72(0x801, 0x0)
    ExitThread()

    label("loc_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22C")
    OP_6F(0x3, 0)
    Jump("loc_233")

    label("loc_22C")

    OP_6F(0x3, 60)

    label("loc_233")

    Return()

    # Function_1_1A4 end

    def Function_2_234(): pass

    label("Function_2_234")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_319")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x33F, 1)"), scpexpr(EXPR_END)), "loc_2A8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x3F\x03\x07\x00。\x02",
    )

    Jump("loc_28D")

    label("loc_28D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x28AF)
    Jump("loc_316")

    label("loc_2A8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x3F\x03\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x3F\x03\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_2F7")

    label("loc_2F7")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_316")

    Jump("loc_34C")

    label("loc_319")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_34C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_234 end

    def Function_3_35A(): pass

    label("Function_3_35A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 3)), scpexpr(EXPR_END)), "loc_38D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x501, 2)), scpexpr(EXPR_END)), "loc_37B")
    Call(0, 9)
    Jump("loc_38A")

    label("loc_37B")

    OP_DC(0x0, 0x1)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7101   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_38A")

    Jump("loc_3B1")

    label("loc_38D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 4)), scpexpr(EXPR_END)), "loc_3B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 7)), scpexpr(EXPR_END)), "loc_3A2")
    Call(0, 4)
    Jump("loc_3B1")

    label("loc_3A2")

    OP_DC(0x0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7102   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3B1")

    EventEnd(0x0)
    Return()

    # Function_3_35A end

    def Function_4_3B4(): pass

    label("Function_4_3B4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DF(0x0, 0x1, 0x1)
    Sleep(300)
    SetChrPos(0xEE, 14890, 4000, -29830, 0)
    SetChrPos(0xEF, 15300, 4000, -30380, 0)
    SetChrPos(0xF0, 14260, 4000, -30350, 0)
    SetChrPos(0xF1, 14970, 4000, -31300, 0)
    OP_9F(0xEE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x4, 0x80)
    ClearChrFlags(0x5, 0x80)
    ClearChrFlags(0x6, 0x80)
    ClearChrFlags(0x7, 0x80)
    ClearChrFlags(0x4, 0x8)
    ClearChrFlags(0x5, 0x8)
    ClearChrFlags(0x6, 0x8)
    ClearChrFlags(0x7, 0x8)
    SetChrPos(0xF2, 1960, 0, -2570, 135)
    SetChrPos(0xF3, 0, 0, -1870, 135)
    SetChrPos(0xF4, 2410, 0, -740, 135)
    SetChrPos(0xF5, 850, 0, 0, 135)
    OP_6D(13690, 9000, -26230, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3670, 0)
    OP_6C(224000, 0)
    OP_6E(262, 0)

    def lambda_514():
        OP_6D(13690, 4500, -26230, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_514)

    def lambda_52C():
        OP_67(0, 6200, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_52C)
    FadeToBright(2000, 0)
    OP_22(0x6C, 0x0, 0x64)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x78)
    OP_73(0x0)
    OP_22(0x9A, 0x0, 0x64)
    OP_23(0x6C)
    OP_43(0xEE, 0x0, 0x0, 0x5)
    OP_43(0xEF, 0x0, 0x0, 0x6)
    OP_43(0xF0, 0x0, 0x0, 0x7)
    OP_43(0xF1, 0x0, 0x0, 0x8)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)

    ChrTalk(    #3
        0x10F,
        "#1442F#1P凯文……！\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_5E1():
        OP_6D(-270, 0, -1370, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5E1)

    def lambda_5F9():
        OP_67(0, 6970, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5F9)

    def lambda_611():
        OP_6B(3670, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_611)

    def lambda_621():
        OP_6C(270000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_621)

    def lambda_631():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_631)
    WaitChrThread(0x109, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(14160, 4000, -25750, 0)
    OP_67(0, 6460, -10000, 0)
    OP_6B(3440, 0)
    OP_6C(224000, 0)
    OP_6E(253, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #4
        0x109,
        "#1840F#5P哈哈……看来你们平安无事啊。\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_6CA():
        OP_8E(0xFE, 0x3930, 0x0, 0xFFFFCAA4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6CA)
    Sleep(150)

    def lambda_6EA():
        OP_8E(0xFE, 0x3CFA, 0x0, 0xFFFFC928, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_6EA)
    Sleep(200)

    def lambda_70A():
        OP_8E(0xFE, 0x35E8, 0x0, 0xFFFFC93C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_70A)
    Sleep(250)

    def lambda_72A():
        OP_8E(0xFE, 0x38FE, 0x0, 0xFFFFC680, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_72A)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    Call(0, 14)
    Return()

    # Function_4_3B4 end

    def Function_5_75F(): pass

    label("Function_5_75F")


    def lambda_765():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_765)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x39F8, 0xFA0, 0xFFFFA128, 0x7D0, 0x0)
    Return()

    # Function_5_75F end

    def Function_6_78B(): pass

    label("Function_6_78B")

    Sleep(300)

    def lambda_796():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_796)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x3D36, 0xFA0, 0xFFFF9D7C, 0x7D0, 0x0)
    Return()

    # Function_6_78B end

    def Function_7_7BC(): pass

    label("Function_7_7BC")

    Sleep(600)

    def lambda_7C7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C7)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x367E, 0xFA0, 0xFFFF9BD8, 0x7D0, 0x0)
    Return()

    # Function_7_7BC end

    def Function_8_7ED(): pass

    label("Function_8_7ED")

    Sleep(1000)

    def lambda_7F8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7F8)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x394E, 0xFA0, 0xFFFF9750, 0x7D0, 0x0)
    Return()

    # Function_8_7ED end

    def Function_9_81E(): pass

    label("Function_9_81E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DC(0x0, 0x0)
    OP_DF(0x0, 0x1, 0x1)
    Sleep(300)
    OP_E0(242, 0x45, 0x1)
    OP_E0(243, 0x46, 0x1)
    OP_E0(244, 0x47, 0x1)
    OP_E0(245, 0x48, 0x1)
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x4, 0x80)
    ClearChrFlags(0x5, 0x80)
    ClearChrFlags(0x6, 0x80)
    ClearChrFlags(0x7, 0x80)
    ClearChrFlags(0x4, 0x8)
    ClearChrFlags(0x5, 0x8)
    ClearChrFlags(0x6, 0x8)
    ClearChrFlags(0x7, 0x8)
    SetChrPos(0xF2, -14750, 4000, -29670, 0)
    SetChrPos(0xF3, -14120, 4000, -30480, 0)
    SetChrPos(0xF4, -15430, 4000, -30480, 0)
    SetChrPos(0xF5, -14720, 4000, -31090, 0)
    OP_9F(0x4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x6, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x7, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x3, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x0, -2060, 0, -1910, 225)
    SetChrPos(0x1, -2270, 0, -560, 225)
    SetChrPos(0x2, 250, 0, -2310, 225)
    SetChrPos(0x3, 220, 0, -500, 225)
    OP_6D(-13410, 9000, -26560, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3670, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)

    def lambda_9E9():
        OP_6D(-13410, 4500, -26560, 5000)
        ExitThread()

    QueueWorkItem(0xF2, 2, lambda_9E9)

    def lambda_A01():
        OP_67(0, 6200, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xF2, 3, lambda_A01)
    FadeToBright(2000, 0)
    OP_22(0x6C, 0x0, 0x64)
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_B0(0x1, 0x1E)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x78)
    OP_73(0x1)
    OP_22(0x9A, 0x0, 0x64)
    OP_23(0x6C)
    OP_43(0xF2, 0x0, 0x0, 0xA)
    OP_43(0xF3, 0x0, 0x0, 0xB)
    OP_43(0xF4, 0x0, 0x0, 0xC)
    OP_43(0xF5, 0x0, 0x0, 0xD)
    WaitChrThread(0xF2, 0x0)
    WaitChrThread(0xF3, 0x0)
    WaitChrThread(0xF4, 0x0)
    WaitChrThread(0xF5, 0x0)

    ChrTalk(    #5
        0x109,
        "#1078F#2P莉丝……！\x02",
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_AB6():
        OP_6D(110, 0, -1560, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AB6)

    def lambda_ACE():
        OP_67(0, 6080, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ACE)

    def lambda_AE6():
        OP_6B(3800, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AE6)

    def lambda_AF6():
        OP_6C(89000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_AF6)

    def lambda_B06():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_B06)
    WaitChrThread(0x109, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(-13620, 4000, -26570, 0)
    OP_67(0, 5360, -10000, 0)
    OP_6B(3440, 0)
    OP_6C(135000, 0)
    OP_6E(256, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #6
        0x10F,
        "#1442F#11P……太好了，你们也平安无事。\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xF2, 5)

    def lambda_BA0():
        OP_8E(0xFE, 0xFFFFC662, 0x0, 0xFFFFC7B6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF2, 0, lambda_BA0)
    Sleep(150)
    SetChrChipByIndex(0xF3, 6)

    def lambda_BC5():
        OP_8E(0xFE, 0xFFFFCA5E, 0x0, 0xFFFFC400, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF3, 0, lambda_BC5)
    Sleep(200)
    SetChrChipByIndex(0xF4, 7)

    def lambda_BEA():
        OP_8E(0xFE, 0xFFFFC2FC, 0x0, 0xFFFFC48C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_BEA)
    Sleep(250)
    SetChrChipByIndex(0xF5, 8)

    def lambda_C0F():
        OP_8E(0xFE, 0xFFFFC69E, 0x0, 0xFFFFC22A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_C0F)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0xF2, 0x0)
    OP_44(0xF3, 0x0)
    OP_44(0xF4, 0x0)
    OP_44(0xF5, 0x0)
    Call(0, 14)
    Return()

    # Function_9_81E end

    def Function_10_C44(): pass

    label("Function_10_C44")


    def lambda_C4A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C4A)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFC680, 0xFA0, 0xFFFFA088, 0x7D0, 0x0)
    Return()

    # Function_10_C44 end

    def Function_11_C70(): pass

    label("Function_11_C70")

    Sleep(300)

    def lambda_C7B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C7B)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFCB58, 0xFA0, 0xFFFF9CAA, 0x7D0, 0x0)
    Return()

    # Function_11_C70 end

    def Function_12_CA1(): pass

    label("Function_12_CA1")

    Sleep(600)

    def lambda_CAC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CAC)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFC2FC, 0xFA0, 0xFFFF9D22, 0x7D0, 0x0)
    Return()

    # Function_12_CA1 end

    def Function_13_CD2(): pass

    label("Function_13_CD2")

    Sleep(1000)

    def lambda_CDD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CDD)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFC752, 0xFA0, 0xFFFF98C2, 0x7D0, 0x0)
    Return()

    # Function_13_CD2 end

    def Function_14_D03(): pass

    label("Function_14_D03")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp254_00.eff")
    LoadEffect(0x1, "map\\mp254_01.eff")
    LoadEffect(0x2, "monster\\msc1000.eff")
    OP_DC(0x0, 0x0)
    OP_DF(0x0, 0x1, 0x1)
    Sleep(300)
    SetChrPos(0xEE, 870, 0, 660, 270)
    SetChrPos(0xEF, 2330, 0, 740, 270)
    SetChrPos(0xF0, 600, 0, -1530, 315)
    SetChrPos(0xF1, 2210, 0, -1110, 270)
    OP_51(0xF2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF2, 0x8)
    ClearChrFlags(0xF3, 0x8)
    ClearChrFlags(0xF4, 0x8)
    ClearChrFlags(0xF5, 0x8)
    SetChrPos(0xF2, -910, 0, 410, 90)
    SetChrPos(0xF3, -2540, 0, 610, 90)
    SetChrPos(0xF4, -1400, 0, -1890, 45)
    SetChrPos(0xF5, -2780, 0, -1310, 90)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 10000, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(1080, 0, 1010, 0)
    OP_67(0, 6370, -10000, 0)
    OP_6B(2970, 0)
    OP_6C(45000, 0)
    OP_6E(291, 0)
    Sleep(1500)

    def lambda_E88():
        OP_6B(2770, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_E88)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #7
        0x109,
        (
            "#1068F#5P呼……\x01",
            "看来你才是真人了。\x02\x03",

            "#1840F真是的……\x01",
            "总是要别人担心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10F,
        (
            "#1447F#6P……这句话应该由我说才对。\x02\x03",

            "#1445F话说回来，\x01",
            "那个果然就是『格利摩尔』对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x109,
        "#1063F#5P嗯……应该就是这回事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10E,
        "#173F格利摩尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10D,
        "#270F那个会拟态成其他东西的魔物？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x109,
        (
            "#1065F#5P嗯，没错。\x01",
            "那的确是圣典记载里的魔物。\x02\x03",

            "#1063F与其说是魔物……\x01",
            "倒不如说是灵魂\x01",
            "坠入『炼狱』后的悲惨下场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10B,
        "#216F灵魂的悲惨下场……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        "#1503F……听起来就很不吉利啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10F,
        (
            "#1446F#6P……根据七耀教会的教义，\x01",
            "罪孽深重的灵魂会被打入『炼狱』。\x02\x03",

            "#1445F然后，不断被地狱之火所肆虐，\x01",
            "不知不觉地失去自我……\x02\x03",

            "#1443F最后，这类混沌的灵魂聚集在一起，\x01",
            "就形成了所谓的『格利摩尔』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x107,
        "#065F哇、哇啊～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x105,
        (
            "#1163F也就是说……\x01",
            "那个拟态的怪物就是\x01",
            "那个格利摩尔吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10F,
        (
            "#1446F#6P没错……\x02\x03",

            "刚才同时出现的镜子和炮台，\x01",
            "都是源自『炼狱』的咒具。\x02\x03",

            "#1443F看起来……\x01",
            "虽然不知道敌人使用了何种禁忌手法，\x01",
            "但可以肯定的是，他们已经打开了地狱之门。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #19
        0x10,
        "男子的声音",
        "\x07\x05#4P……呵呵，如你所言。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_130E")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1375")

    label("loc_130E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1336")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1375")

    label("loc_1336")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135E")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1375")

    label("loc_135E")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1375")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139D")
    OP_62(0xF2, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1404")

    label("loc_139D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C5")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1404")

    label("loc_13C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13ED")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1404")

    label("loc_13ED")

    OP_62(0xF2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1404")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1431")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1498")

    label("loc_1431")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1459")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1498")

    label("loc_1459")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1481")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1498")

    label("loc_1481")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1498")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14C0")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1527")

    label("loc_14C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E8")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1527")

    label("loc_14E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1510")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1527")

    label("loc_1510")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1527")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1554")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_15BB")

    label("loc_1554")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_157C")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_15BB")

    label("loc_157C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A4")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_15BB")

    label("loc_15A4")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_15BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15E3")
    OP_62(0xF5, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_164A")

    label("loc_15E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_160B")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_164A")

    label("loc_160B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1633")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_164A")

    label("loc_1633")

    OP_62(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_164A")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1677")
    OP_62(0xF4, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16DE")

    label("loc_1677")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_169F")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16DE")

    label("loc_169F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C7")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16DE")

    label("loc_16C7")

    OP_62(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_16DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1706")
    OP_62(0xF3, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_176D")

    label("loc_1706")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_172E")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_176D")

    label("loc_172E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1756")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_176D")

    label("loc_1756")

    OP_62(0xF3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_176D")

    Sleep(1000)

    def lambda_1778():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1778)
    Sleep(50)

    def lambda_178B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF2, 1, lambda_178B)

    def lambda_1799():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1799)
    Sleep(50)

    def lambda_17AC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_17AC)

    def lambda_17BA():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_17BA)
    Sleep(50)

    def lambda_17CD():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_17CD)

    def lambda_17DB():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_17DB)
    Sleep(50)

    def lambda_17EE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF3, 1, lambda_17EE)
    Sleep(300)

    ChrTalk(    #20
        0x10F,
        "#1441F#6P哎……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x109,
        "#1069F#12P……这个声音！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_1D(0xB0)

    def lambda_184B():
        OP_6D(530, 0, 10740, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_184B)

    def lambda_1863():
        OP_67(0, 5770, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1863)

    def lambda_187B():
        OP_6B(2970, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_187B)

    def lambda_188B():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_188B)

    def lambda_189B():
        OP_6E(291, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_189B)
    WaitChrThread(0x109, 0x0)
    Sleep(300)
    OP_22(0xBA, 0x1, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 0, 0, 10000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    PlayEffect(0x1, 0x1, 0xFF, -350, 0, 10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1929():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1929)
    OP_22(0x59, 0x0, 0x64)
    OP_8C(0xEE, 0, 0)
    OP_8C(0xEF, 0, 0)
    OP_8C(0xF0, 0, 0)
    OP_8C(0xF1, 0, 0)
    OP_8C(0xF2, 0, 0)
    OP_8C(0xF3, 0, 0)
    OP_8C(0xF4, 0, 0)
    OP_8C(0xF5, 0, 0)
    Fade(500)
    OP_6D(-480, 0, 4120, 0)
    OP_67(0, 4530, -10000, 0)
    OP_6B(2370, 0)
    OP_6C(157000, 0)
    OP_6E(473, 0)
    OP_6D(-200, 0, 4510, 0)
    OP_67(0, 3890, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(152000, 0)
    OP_6E(473, 0)
    OP_6D(-200, 0, 4510, 0)
    OP_67(0, 4530, -10000, 0)
    OP_6B(2370, 0)
    OP_6C(152000, 0)
    OP_6E(473, 0)
    OP_6D(350, 0, 3060, 0)
    OP_67(0, 4530, -10000, 0)
    OP_6B(2370, 0)
    OP_6C(152000, 0)
    OP_6E(473, 0)
    OP_0D()
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_23(0xBA)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AA2")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1B09")

    label("loc_1AA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ACA")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1B09")

    label("loc_1ACA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AF2")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1B09")

    label("loc_1AF2")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1B09")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B31")
    OP_62(0xF2, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1B98")

    label("loc_1B31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B59")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1B98")

    label("loc_1B59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B81")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1B98")

    label("loc_1B81")

    OP_62(0xF2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1B98")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BC5")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1C2C")

    label("loc_1BC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BED")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1C2C")

    label("loc_1BED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C15")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1C2C")

    label("loc_1C15")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1C2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C54")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1CBB")

    label("loc_1C54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C7C")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1CBB")

    label("loc_1C7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CA4")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1CBB")

    label("loc_1CA4")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1CBB")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE8")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1D4F")

    label("loc_1CE8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D10")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1D4F")

    label("loc_1D10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D38")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1D4F")

    label("loc_1D38")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1D4F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D77")
    OP_62(0xF5, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1DDE")

    label("loc_1D77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D9F")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1DDE")

    label("loc_1D9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DC7")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1DDE")

    label("loc_1DC7")

    OP_62(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1DDE")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E0B")
    OP_62(0xF4, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1E72")

    label("loc_1E0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E33")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1E72")

    label("loc_1E33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E5B")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1E72")

    label("loc_1E5B")

    OP_62(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1E72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E9A")
    OP_62(0xF3, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1F01")

    label("loc_1E9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EC2")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1F01")

    label("loc_1EC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EEA")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1F01")

    label("loc_1EEA")

    OP_62(0xF3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1F01")

    Sleep(1000)

    ChrTalk(    #22
        0x102,
        "#1504F#5P………！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10E,
        "#172F#5P又来了……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        (
            "#1075F#5P还敢明目张胆现身……？\x02\x03",

            "#1060F莫非……\x01",
            "你又奉『影之王』之令来监视我们？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "\x07\x05#1591F#6P呵呵……\x01",
            "那不过是目的之一罢了。\x02\x03",

            "你们有幸得到『隐者』的指导，\x01",
            "顺利抵达这里，真是不错啊。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        "#1063F#5P『隐者』……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x105,
        (
            "#1163F#5P莫非你指的是……\x01",
            "那个女性灵魂？\x02\x03",

            "那个一直在引导我们、\x01",
            "帮助我们的那位……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        (
            "\x07\x05#1590F#6P没错。一个虚幻的庭院主人，\x01",
            "一个被遗弃的『影之国』亡灵。\x02\x03",

            "#1591F呵呵，由于吾王略施小计，\x01",
            "那个灵魂丧失了大半的力量……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x109,
        (
            "#1075F#5P哼，虽不知道你在说什么……\x02\x03",

            "#1060F既然她是你们的敌人……\x01",
            "也就可以说是我们的朋友对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        (
            "\x07\x05#1591F#6P呵呵……\x01",
            "你认为她果真是你们的朋友吗？\x02\x03",

            "姑且不说这个话题——\x01",
            "这次，我是为『影之王』传话来的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #31
        0x10,
        (
            "\x07\x05#1590F#6P『——次回为兽之道。』 \x02\x03",

            "『领受新供品，\x01",
            "  即让汝等发现印记。』\x02\x03",

            "『如此，炼狱之焰愈猛烈，\x01",
            "  吾王国竣工则指日可待——』\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #32
        0x10F,
        "#1444F#5P哎……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x109,
        "#1079F#5P……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10E,
        "#178F#5P……什么意思……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10,
        (
            "\x07\x05#1591F#6P呵呵……\x01",
            "能否领悟个中玄机，就看你们自己了。\x02\x03",

            "好了，我已经传话完毕。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x109, 4)
    SetChrSubChip(0x109, 1)
    OP_0D()
    Sleep(500)
    OP_9E(0x109, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(500)

    ChrTalk(    #36
        0x109,
        "#1846F#5P#50W……哼……哈哈……\x02",
    )

    CloseMessageWindow()
    Sleep(800)

    ChrTalk(    #37
        0x109,
        "#1061F#5P#4S哈哈哈哈哈哈哈哈！！！\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x12C)
    CloseMessageWindow()
    OP_8C(0x10F, 90, 400)
    Sleep(300)

    ChrTalk(    #38
        0x10F,
        "#1802F#12P凯、凯文……？\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #39
        0x109,
        (
            "#1840F#5P呵呵……失礼了。抱歉、抱歉。\x02\x03",

            "不就是那么点故弄玄虚的伎俩吗……\x01",
            "我差点又陷入圈套里了。\x02\x03",

            "#1075F我说，那无非是……\x01",
            "想把我们引入圈套而说的胡话对吧。\x02\x03",

            "#1073F即使如此，\x01",
            "装模作样也做得太过头了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10,
        "\x07\x05#1590F#6P……………………………………\x07\x00\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_6D(1200, 0, 5900, 0)
    OP_67(0, 4450, -10000, 0)
    OP_6B(3480, 0)
    OP_6C(33000, 0)
    OP_6E(334, 0)
    OP_0D()
    Sleep(300)
    Fade(500)

    def lambda_264A():
        OP_6D(1430, 0, 6040, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_264A)

    def lambda_2662():
        OP_6B(3350, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2662)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 2)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    SetChrChipByIndex(0x109, 3)
    SetChrSubChip(0x109, 0)

    def lambda_2691():
        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2691)
    Sleep(300)
    OP_22(0xD8, 0x0, 0x64)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    ChrTalk(    #41
        0x109,
        (
            "#1072F#6P……话说完了的话，\x01",
            "就马上给我消失吧。\x02\x03",

            "要想找人陪你玩无聊的游戏，\x01",
            "抱歉，我们可没那闲工夫。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x555, 0x2)"), scpexpr(EXPR_END)), "loc_27FF")

    ChrTalk(    #42
        0x10,
        (
            "\x07\x05#1591F#5P呵呵……\x02\x03",

            "看上去，\x01",
            "你对王的恩赐相当满意啊。\x02\x03",

            "一定非常怀念吧？\x07\x00\x02",
        )
    )

    Jump("loc_279F")

    label("loc_279F")

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #43
        0x109,
        "#1074F#6P什么……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10F,
        "#1802F#6P凯文……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_29C7")

    label("loc_27FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x555, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28FD")

    ChrTalk(    #45
        0x10,
        (
            "\x07\x05#1590F#5P唔……\x02\x03",

            "看上去，\x01",
            "你对王的恩赐很不满意啊。\x02\x03",

            "#1591F哎呀哎呀……\x01",
            "就这么一点恩赐都让你如此痛苦？\x07\x00\x02",
        )
    )

    Jump("loc_289D")

    label("loc_289D")

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #46
        0x109,
        "#1074F#6P什么……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10F,
        "#1802F#6P凯文……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_29C7")

    label("loc_28FD")


    ChrTalk(    #48
        0x10,
        (
            "\x07\x05#1590F#5P唔……\x01",
            "难得吾王煞费苦心予以你赏赐，\x01",
            "你竟敢视若无睹。\x02\x03",

            "#1591F哎呀哎呀……\x01",
            "这就是无意识的畏惧所造成的吗。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x109,
        "#1074F#6P什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10F,
        "#1802F#6P凯文……？\x02",
    )

    CloseMessageWindow()

    label("loc_29C7")

    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)
    PlayEffect(0x2, 0x1, 0xFF, 0, 0, 10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_8C(0x10F, 0, 400)
    Sleep(500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 0, 0, 10000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_22(0xBA, 0x1, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A8C")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2AF3")

    label("loc_2A8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AB4")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2AF3")

    label("loc_2AB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ADC")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2AF3")

    label("loc_2ADC")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2AF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B1B")
    OP_62(0xF2, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2B82")

    label("loc_2B1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B43")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2B82")

    label("loc_2B43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B6B")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2B82")

    label("loc_2B6B")

    OP_62(0xF2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2B82")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BAF")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2C16")

    label("loc_2BAF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BD7")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2C16")

    label("loc_2BD7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BFF")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2C16")

    label("loc_2BFF")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2C16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C3E")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2CA5")

    label("loc_2C3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C66")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2CA5")

    label("loc_2C66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C8E")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2CA5")

    label("loc_2C8E")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2CA5")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CD2")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2D39")

    label("loc_2CD2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CFA")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2D39")

    label("loc_2CFA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D22")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2D39")

    label("loc_2D22")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2D39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D61")
    OP_62(0xF5, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2DC8")

    label("loc_2D61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D89")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2DC8")

    label("loc_2D89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DB1")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2DC8")

    label("loc_2DB1")

    OP_62(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2DC8")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DF5")
    OP_62(0xF4, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2E5C")

    label("loc_2DF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E1D")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2E5C")

    label("loc_2E1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E45")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2E5C")

    label("loc_2E45")

    OP_62(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2E5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E84")
    OP_62(0xF3, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2EEB")

    label("loc_2E84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EAC")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2EEB")

    label("loc_2EAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ED4")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2EEB")

    label("loc_2ED4")

    OP_62(0xF3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2EEB")

    Sleep(1000)

    ChrTalk(    #51
        0x102,
        "#1502F#6P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10B,
        "#214F#6P想、想逃吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        (
            "\x07\x05#1591F#5P哈哈，\x01",
            "反正我们迟早会再碰面的。\x02\x03",

            "请牢记，我名为『黑骑士』——\x01",
            "『影之国』第一守护者。\x02\x03",

            "呵呵……后会有期。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2FFC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2FFC)
    OP_22(0x59, 0x0, 0x64)
    Sleep(500)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_23(0xBA)
    OP_20(0x7D0)
    Sleep(2000)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEE, 65535)
    SetChrSubChip(0xEE, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_305D")
    OP_62(0xEE, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_30B5")

    label("loc_305D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3080")
    OP_62(0xEE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_30B5")

    label("loc_3080")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30A3")
    OP_62(0xEE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_30B5")

    label("loc_30A3")

    OP_62(0xEE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_30B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30D8")
    OP_62(0xF5, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3130")

    label("loc_30D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30FB")
    OP_62(0xF5, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3130")

    label("loc_30FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_311E")
    OP_62(0xF5, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3130")

    label("loc_311E")

    OP_62(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_3130")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3158")
    OP_62(0xF4, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_31B0")

    label("loc_3158")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_317B")
    OP_62(0xF4, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_31B0")

    label("loc_317B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_319E")
    OP_62(0xF4, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_31B0")

    label("loc_319E")

    OP_62(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_31B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31D3")
    OP_62(0xF1, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_322B")

    label("loc_31D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31F6")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_322B")

    label("loc_31F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3219")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_322B")

    label("loc_3219")

    OP_62(0xF1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_322B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3253")
    OP_62(0xF0, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_32AB")

    label("loc_3253")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3276")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_32AB")

    label("loc_3276")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3299")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_32AB")

    label("loc_3299")

    OP_62(0xF0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_32AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32CE")
    OP_62(0xF3, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3326")

    label("loc_32CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32F1")
    OP_62(0xF3, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3326")

    label("loc_32F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3314")
    OP_62(0xF3, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3326")

    label("loc_3314")

    OP_62(0xF3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_3326")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_334E")
    OP_62(0xEF, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_33A6")

    label("loc_334E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3371")
    OP_62(0xEF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_33A6")

    label("loc_3371")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3394")
    OP_62(0xEF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_33A6")

    label("loc_3394")

    OP_62(0xEF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_33A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33C9")
    OP_62(0xF2, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3421")

    label("loc_33C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33EC")
    OP_62(0xF2, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3421")

    label("loc_33EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_340F")
    OP_62(0xF2, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3421")

    label("loc_340F")

    OP_62(0xF2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_3421")

    Fade(1000)
    OP_6D(1800, 0, 0, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(134000, 0)
    OP_6E(245, 0)
    SetChrPos(0xEE, 730, 0, -740, 0)
    SetChrPos(0xEF, 2320, 0, 10, 0)
    SetChrPos(0xF0, 2910, 0, -1790, 0)
    SetChrPos(0xF1, 1750, 0, -2940, 0)
    SetChrPos(0xF2, -1110, 0, -790, 0)
    SetChrPos(0xF3, -2970, 0, -20, 0)
    SetChrPos(0xF4, -3250, 0, -1640, 0)
    SetChrPos(0xF5, -1530, 0, -2530, 0)

    def lambda_34F1():
        OP_6D(1800, 0, -3000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_34F1)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    OP_63(0xEE)
    OP_63(0xEF)
    OP_63(0xF0)
    OP_63(0xF1)
    OP_63(0xF2)
    OP_63(0xF3)
    OP_63(0xF4)
    OP_63(0xF5)
    Sleep(500)

    ChrTalk(    #54
        0x102,
        "#1503F#5P……那个人就是『黑骑士』……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x109,
        (
            "#1075F#5P哼，喜欢临走时说些即兴的台词，\x01",
            "这个癖好倒是跟他的主人一个样。\x02\x03",

            "#1840F他那点故弄玄虚的伎俩，\x01",
            "一看就知道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10F,
        "#1802F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10E,
        (
            "#176F#5P『——次回为兽之道。』 \x02\x03",

            "『领受新供品，\x01",
            "  即让汝等发现印记。』\x02\x03",

            "#178F『如此，炼狱之焰愈猛烈，\x01",
            "  吾王国竣工则指日可待——』\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10D,
        (
            "#272F#5P……的确是\x01",
            "怎么解释都可以的语句啊。\x02\x03",

            "#270F要是随便听信的话……\x01",
            "恐怕会落入敌人的陷阱里啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x109,
        "#1075F#5P嗯，就是这样。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #60
        0x109,
        (
            "#1078F#5P……也罢。\x01",
            "……难得又得到两个封印石，\x01",
            "我们暂时先回『据点』吧。\x02\x03",

            "把这两个封印石在石碑前解放之后，\x01",
            "应该就能马上获得线索了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_37ED():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_37ED)
    Sleep(50)

    def lambda_3800():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_3800)
    Sleep(50)

    def lambda_3813():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_3813)
    Sleep(50)

    def lambda_3826():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_3826)
    Sleep(50)

    def lambda_3839():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_3839)
    Sleep(50)

    def lambda_384C():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF3, 1, lambda_384C)
    Sleep(50)
    OP_8C(0xF2, 90, 400)
    Sleep(200)

    ChrTalk(    #61
        0x107,
        "#560F#5P是、是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x105,
        (
            "#1382F#5P……这次从封印里解放出来的\x01",
            "又会是什么人呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0xBB8)

    def lambda_38D0():
        OP_6B(4000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_38D0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x2)
    Sleep(2000)
    OP_A2(0x280B)
    OP_A2(0x258D)
    OP_AA(2560)
    OP_AA(65281)
    OP_AD(0x2400EF, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x2582)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x158), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存】\x01",              # 0
            "【继续下面剧情】\x01",      # 1
        )
    )

    Jump("loc_3966")

    label("loc_3966")

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_397A")
    ShowSaveMenu()

    label("loc_397A")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_20(0x7D0)
    OP_21()
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_A3(0x2582)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2504)
    OP_A2(0x2506)
    NewScene("ED6_DT21/U7000   ._SN", 104, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_14_D03 end

    def Function_15_39C6(): pass

    label("Function_15_39C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 1)), scpexpr(EXPR_END)), "loc_39CE")
    Return()

    label("loc_39CE")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-120, 1530, 28620, 0)
    OP_67(0, 12070, -10000, 0)
    OP_6B(3930, 0)
    OP_6C(47000, 0)
    OP_6E(287, 0)
    SetChrPos(0x109, -990, 0, 14080, 0)
    SetChrPos(0x102, 670, 0, 13980, 0)
    SetChrPos(0xF0, -990, 0, 14080, 0)
    SetChrPos(0xF1, 670, 0, 13980, 0)
    Sleep(1000)

    def lambda_3A61():
        OP_6D(110, 1530, 26410, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3A61)

    def lambda_3A79():
        OP_67(0, 7090, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3A79)

    def lambda_3A91():
        OP_6B(3350, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3A91)

    def lambda_3AA1():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3AA1)

    def lambda_3AB1():
        OP_6E(245, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3AB1)

    def lambda_3AC1():
        OP_8E(0xFE, 0xFFFFFC68, 0x5FA, 0x5F28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3AC1)
    Sleep(200)

    def lambda_3AE1():
        OP_8E(0xFE, 0x1D6, 0x5FA, 0x5E92, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3AE1)
    Sleep(500)

    def lambda_3B01():
        OP_8E(0xFE, 0xFFFFFBDC, 0x5FA, 0x592E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_3B01)
    Sleep(300)

    def lambda_3B21():
        OP_8E(0xFE, 0xDC, 0x5FA, 0x5884, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_3B21)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)
    OP_0D()
    Sleep(300)

    ChrTalk(    #63
        0x102,
        (
            "#1502F#12P这是……\x01",
            "通往第四星层的入口吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x109,
        (
            "#1065F#6P是啊……\x01",
            "这是连接星层之间的转位魔法阵。\x02\x03",

            "#1063F这里面应该也和之前一样，\x01",
            "可以通往一些全新的场所。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C80")

    ChrTalk(    #65
        0x104,
        (
            "#1545F唔，也就是说，\x01",
            "一定会有一些奇怪的魔物在游荡吗。\x02\x03",

            "#1540F总觉得让人有点紧张啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DE4")

    label("loc_3C80")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CCA")

    ChrTalk(    #66
        0x107,
        (
            "#065F有、有可能又会\x01",
            "出现一些奇怪的怪物对吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DE4")

    label("loc_3CCA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D16")

    ChrTalk(    #67
        0x10B,
        (
            "#413F啊……会不会还有\x01",
            "什么奇怪的魔物在游荡呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DE4")

    label("loc_3D16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D5F")

    ChrTalk(    #68
        0x105,
        (
            "#1162F……很可能又会\x01",
            "出现一些奇怪的魔物呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DE4")

    label("loc_3D5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DA3")

    ChrTalk(    #69
        0x10E,
        (
            "#178F很可能又会\x01",
            "出现一些奇怪的魔物呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DE4")

    label("loc_3DA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DE4")

    ChrTalk(    #70
        0x10D,
        (
            "#270F很可能又会\x01",
            "出现一些奇怪的魔物呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E32")

    ChrTalk(    #71
        0x108,
        (
            "#072F嗯，想进去的话，\x01",
            "一定要做好随时迎战的准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FA6")

    label("loc_3E32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E7C")

    ChrTalk(    #72
        0x10D,
        (
            "#270F想进去的话，\x01",
            "一定要做好随时迎战的准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FA6")

    label("loc_3E7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EC6")

    ChrTalk(    #73
        0x10E,
        (
            "#178F想进去的话，\x01",
            "一定要做好随时迎战的准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FA6")

    label("loc_3EC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F13")

    ChrTalk(    #74
        0x105,
        (
            "#1162F想进去的话……\x01",
            "一定要做好随时迎战的准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FA6")

    label("loc_3F13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F61")

    ChrTalk(    #75
        0x10B,
        (
            "#212F唔，想进去的话，\x01",
            "一定要做好随时迎战的准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FA6")

    label("loc_3F61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FA6")

    ChrTalk(    #76
        0x107,
        (
            "#062F要、要进去的话，\x01",
            "一定要提起精神才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FA6")

    OP_A2(0x2901)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_15_39C6 end

    def Function_16_3FB1(): pass

    label("Function_16_3FB1")

    EventBegin(0x0)
    Fade(500)
    OP_6D(530, 1530, 28420, 0)
    OP_67(0, 7380, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(253, 0)
    SetChrPos(0x109, -140, 1530, 28780, 0)
    SetChrPos(0x102, 680, 1530, 27980, 0)
    SetChrPos(0xF0, -1030, 1530, 27780, 0)
    SetChrPos(0xF1, -110, 1530, 27110, 0)
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
    PlayEffect(0x0, 0xFF, 0xFF, -90, 1530, 27950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_40BF():
        OP_6D(12870, 1430, 40450, 8000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_40BF)
    Call(0, 21)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    NewScene("ED6_DT21/U5100   ._SN", 104, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_16_3FB1 end

    def Function_17_40FC(): pass

    label("Function_17_40FC")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #77
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_4129")

    label("loc_4129")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_413C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4294")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_418E")

    label("loc_418E")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_41AB"),
        (1, "loc_4226"),
        (2, "loc_4255"),
        (SWITCH_DEFAULT, "loc_4284"),
    )


    label("loc_41AB")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xDE)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4291")

    label("loc_4226")

    OP_A9(0x1A)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #78
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_4252")

    label("loc_4252")

    Jump("loc_4291")

    label("loc_4255")

    OP_A9(0x5)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #79
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_4281")

    label("loc_4281")

    Jump("loc_4291")

    label("loc_4284")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4291")

    label("loc_4291")

    Jump("loc_413C")

    label("loc_4294")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xFF)
    Return()

    # Function_17_40FC end

    def Function_18_42B5(): pass

    label("Function_18_42B5")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -110, 1530, 27110, 180)
    SetChrPos(0x1, -1030, 1530, 27780, 180)
    SetChrPos(0x2, 680, 1530, 27980, 180)
    SetChrPos(0x3, -140, 1530, 28780, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -90, 1530, 27950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_18_42B5 end

    def Function_19_4393(): pass

    label("Function_19_4393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43A4")
    Call(0, 16)
    Return()

    label("loc_43A4")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -110, 1530, 27110, 0)
    SetChrPos(0x2, -1030, 1530, 27780, 0)
    SetChrPos(0x1, 680, 1530, 27980, 0)
    SetChrPos(0x0, -140, 1530, 28780, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -90, 1530, 27950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_446A")
    NewScene("ED6_DT21/U5100   ._SN", 104, 0, 0)
    IdleLoop()
    Jump("loc_4473")

    label("loc_446A")

    NewScene("ED6_DT21/U5102   ._SN", 103, 0, 0)
    IdleLoop()

    label("loc_4473")

    Return()

    # Function_19_4393 end

    def Function_20_4474(): pass

    label("Function_20_4474")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_449D")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4491():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4491)

    label("loc_449D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44C6")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_44BA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_44BA)

    label("loc_44C6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44EF")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_44E3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_44E3)

    label("loc_44EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4518")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_450C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_450C)

    label("loc_4518")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4544")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4544")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_455B")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_455B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4572")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4572")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4589")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4589")

    Return()

    # Function_20_4474 end

    def Function_21_458A(): pass

    label("Function_21_458A")


    def lambda_4590():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4590)

    def lambda_45A2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_45A2)

    def lambda_45B4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_45B4)

    def lambda_45C6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_45C6)
    Sleep(1000)
    Return()

    # Function_21_458A end

    SaveToFile()

Try(main)
