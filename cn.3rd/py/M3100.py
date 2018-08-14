from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M3100   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M3100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60232",
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


    DeclActor(
        TriggerX            = 3630,
        TriggerZ            = -20,
        TriggerY            = -49100,
        TriggerRange        = 1000,
        ActorX              = 3630,
        ActorZ              = 2000,
        ActorY              = -49100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6000,
        TriggerZ            = 0,
        TriggerY            = -45540,
        TriggerRange        = 1500,
        ActorX              = 6000,
        ActorZ              = 1500,
        ActorY              = -45540,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F2",           # 00, 0
        "Function_1_127",          # 01, 1
        "Function_2_151",          # 02, 2
        "Function_3_E92",          # 03, 3
        "Function_4_112A",         # 04, 4
        "Function_5_12C1",         # 05, 5
        "Function_6_141C",         # 06, 6
        "Function_7_1532",         # 07, 7
        "Function_8_1580",         # 08, 8
    )


    def Function_0_F2(): pass

    label("Function_0_F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_107")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_107")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_11F"),
        (SWITCH_DEFAULT, "loc_126"),
    )


    label("loc_11F")

    Event(0, 4)
    Jump("loc_126")

    label("loc_126")

    Return()

    # Function_0_F2 end

    def Function_1_127(): pass

    label("Function_1_127")

    OP_22(0x1CC, 0x0, 0x64)
    OP_1B(0x3, 0x0, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_142")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 0)), scpexpr(EXPR_END)), "loc_150")
    OP_6F(0x0, 450)

    label("loc_150")

    Return()

    # Function_1_127 end

    def Function_2_151(): pass

    label("Function_2_151")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 880, 0, -54890, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B6")
    SetChrPos(0xEF, 100, -110, -53600, 0)
    SetChrPos(0xF0, -1120, -40, -54830, 0)
    SetChrPos(0xF1, -140, 0, -55760, 0)
    Jump("loc_23B")

    label("loc_1B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FA")
    SetChrPos(0xF0, 100, -110, -53600, 0)
    SetChrPos(0xEF, -1120, -40, -54830, 0)
    SetChrPos(0xF1, -140, 0, -55760, 0)
    Jump("loc_23B")

    label("loc_1FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23B")
    SetChrPos(0xF1, 100, -110, -53600, 0)
    SetChrPos(0xEF, -1120, -40, -54830, 0)
    SetChrPos(0xF0, -140, 0, -55760, 0)

    label("loc_23B")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(500, -70, -54070, 0)
    OP_67(0, 8480, -10000, 0)
    OP_6B(2050, 0)
    OP_6C(45000, 0)
    OP_6E(329, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3AA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3AA)

    def lambda_3BC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3BC)

    def lambda_3CE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3CE)

    def lambda_3E0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3E0)
    Sleep(1500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_435")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_49C")

    label("loc_435")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45D")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_49C")

    label("loc_45D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_485")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_49C")

    label("loc_485")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_49C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C9")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_530")

    label("loc_4C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F1")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_530")

    label("loc_4F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_519")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_530")

    label("loc_519")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_530")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55D")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5C4")

    label("loc_55D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_585")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5C4")

    label("loc_585")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AD")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5C4")

    label("loc_5AD")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5C4")

    Sleep(1500)

    ChrTalk(    #0
        0x10C,
        (
            "#119F#6P原来如此啊……\x02\x03",

            "#118F『铁壁要塞』……\x01",
            "真是恰如其名。\x02",
        )
    )

    CloseMessageWindow()
    OP_1D(0xE8)
    Sleep(300)
    Fade(1000)
    OP_6D(1360, -100, -50470, 0)
    OP_67(0, 10030, -10000, 0)
    OP_6B(3390, 0)
    OP_6C(45000, 0)
    OP_6E(378, 0)

    def lambda_668():
        OP_6D(0, 3000, -1700, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_668)

    def lambda_680():
        OP_67(0, 8200, -10000, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_680)

    def lambda_698():
        OP_6B(3390, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_698)

    def lambda_6A8():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_6A8)

    def lambda_6B8():
        OP_6E(387, 7000)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_6B8)
    OP_C8(0x200, 0x46, "C_PLAC35._CH", 0x1, 0xBB8)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_768")

    def lambda_6F0():
        OP_8F(0xFE, 0xFFFFFD8A, 0xFFFFFF7E, 0xFFFF5150, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_6F0)
    Sleep(50)

    def lambda_710():
        OP_8F(0xFE, 0x276, 0xFFFFFF56, 0xFFFF50A6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_710)
    Sleep(150)

    def lambda_730():
        OP_8F(0xFE, 0x2A8, 0xFFFFFF06, 0xFFFF4B92, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_730)
    Sleep(50)

    def lambda_750():
        OP_8F(0xFE, 0xFFFFFCEA, 0xFFFFFF6A, 0xFFFF4B2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_750)
    Jump("loc_87D")

    label("loc_768")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F4")

    def lambda_77C():
        OP_8F(0xFE, 0xFFFFFD8A, 0xFFFFFF7E, 0xFFFF5150, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_77C)
    Sleep(50)

    def lambda_79C():
        OP_8F(0xFE, 0x276, 0xFFFFFF56, 0xFFFF50A6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_79C)
    Sleep(150)

    def lambda_7BC():
        OP_8F(0xFE, 0x2A8, 0xFFFFFF06, 0xFFFF4B92, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_7BC)
    Sleep(50)

    def lambda_7DC():
        OP_8F(0xFE, 0xFFFFFCEA, 0xFFFFFF6A, 0xFFFF4B2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_7DC)
    Jump("loc_87D")

    label("loc_7F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87D")

    def lambda_808():
        OP_8F(0xFE, 0xFFFFFD8A, 0xFFFFFF7E, 0xFFFF5150, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_808)
    Sleep(50)

    def lambda_828():
        OP_8F(0xFE, 0x276, 0xFFFFFF56, 0xFFFF50A6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_828)
    Sleep(150)

    def lambda_848():
        OP_8F(0xFE, 0x2A8, 0xFFFFFF06, 0xFFFF4B92, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_848)
    Sleep(50)

    def lambda_868():
        OP_8F(0xFE, 0xFFFFFCEA, 0xFFFFFF6A, 0xFFFF4B2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_868)

    label("loc_87D")

    WaitChrThread(0xEF, 0x1)

    def lambda_888():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_888)
    OP_22(0x6C, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1C2)
    WaitChrThread(0xEE, 0x1)

    def lambda_8B0():
        OP_6D(0, 3300, -500, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_8B0)

    def lambda_8C8():
        OP_67(0, 3600, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_8C8)

    def lambda_8E0():
        OP_6B(3900, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_8E0)

    def lambda_8F0():
        OP_6E(410, 8000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_8F0)
    Sleep(1000)
    OP_22(0x6C, 0x0, 0x64)
    WaitChrThread(0xEE, 0x1)
    OP_73(0x0)
    OP_44(0xEE, 0x3)
    OP_44(0xEF, 0x1)
    Sleep(300)
    Fade(1000)
    OP_6D(1110, -150, -44470, 0)
    OP_67(0, 7470, -10000, 0)
    OP_6B(2490, 0)
    OP_6C(45000, 0)
    OP_6E(266, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A3B")

    ChrTalk(    #1
        0x10F,
        (
            "#1802F#12P凯文……\x01",
            "那个宏伟的建筑是？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1065F#5P雷斯顿要塞……\x01",
            "我记得应该是王国军的大本营。\x02\x03",

            "#1063F而且看起来，\x01",
            "满是欢迎我们的气氛嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10F,
        "#1443F#4P……好像是呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB0")

    label("loc_A3B")


    ChrTalk(    #4
        0x109,
        (
            "#1065F#5P雷斯顿要塞……\x01",
            "我记得这里是王国军的大本营吧。\x02\x03",

            "#1063F而且看起来，\x01",
            "满是欢迎我们的气氛嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB0")


    ChrTalk(    #5
        0x10C,
        (
            "#119F#5P呵呵，这可伤脑筋了。\x02\x03",

            "是谁等在里面\x01",
            "大概也不难猜出来……\x02\x03",

            "#110F……似乎有必要\x01",
            "带着必死的决心前去挑战啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B6B")

    ChrTalk(    #6
        0x101,
        "#1020F#12P的、的确……\x02",
    )

    CloseMessageWindow()

    label("loc_B6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9E")

    ChrTalk(    #7
        0x105,
        "#1162F#12P……是啊………\x02",
    )

    CloseMessageWindow()

    label("loc_B9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD1")

    ChrTalk(    #8
        0x103,
        "#1525F#12P我也有同感……\x02",
    )

    CloseMessageWindow()

    label("loc_BD1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFF")

    ChrTalk(    #9
        0x108,
        "#074F#12P……没错。\x02",
    )

    CloseMessageWindow()

    label("loc_BFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C3F")

    ChrTalk(    #10
        0x10A,
        (
            "#1317F#12P这、这实在是\x01",
            "有些犯规啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C7B")

    ChrTalk(    #11
        0x102,
        (
            "#1502F#12P似乎会有\x01",
            "一场苦战呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC2")

    ChrTalk(    #12
        0x10E,
        (
            "#178F#12P没想到会以这种方式\x01",
            "拜访这个地方……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CFC")

    ChrTalk(    #13
        0x104,
        (
            "#1545F#12P呼……\x01",
            "还挺有趣的嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D69")

    ChrTalk(    #14
        0x10D,
        (
            "#278F#12P以难攻不破著称的\x01",
            "利贝尔军大本营……\x02\x03",

            "#277F守备力量到底有多强大呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DB6")

    ChrTalk(    #15
        0x10B,
        (
            "#413F#12P嗯～可是这里给我\x01",
            "只留下不好的回忆而已……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DF5")

    ChrTalk(    #16
        0x106,
        (
            "#051F#12P哼，\x01",
            "没想到又要潜入这里了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E3A")

    ChrTalk(    #17
        0x107,
        (
            "#065F#12P又、又要和士兵哥哥们\x01",
            "打仗了吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E78")

    ChrTalk(    #18
        0x110,
        (
            "#1306F#12P呵呵……\x01",
            "真是让人兴奋呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E78")

    OP_A2(0x2B18)
    OP_28(0x39, 0x1, 0x8)
    Sleep(300)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x0)
    Return()

    # Function_2_151 end

    def Function_3_E92(): pass

    label("Function_3_E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F61")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(6400)
    Sleep(500)
    Jump("loc_F64")

    label("loc_F61")

    TalkBegin(0xFF)

    label("loc_F64")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #19
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_F8E")

    label("loc_F8E")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F9")

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

    Jump("loc_FF3")

    label("loc_FF3")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1010"),
        (1, "loc_108B"),
        (2, "loc_10BA"),
        (SWITCH_DEFAULT, "loc_10E9"),
    )


    label("loc_1010")

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
    OP_1D(0xE8)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10F6")

    label("loc_108B")

    OP_A9(0x26)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #20
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_10B7")

    label("loc_10B7")

    Jump("loc_10F6")

    label("loc_10BA")

    OP_A9(0x9)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #21
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_10E6")

    label("loc_10E6")

    Jump("loc_10F6")

    label("loc_10E9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10F6")

    label("loc_10F6")

    Jump("loc_FA1")

    label("loc_10F9")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1126")
    OP_A2(0x259C)
    EventEnd(0x1)
    Jump("loc_1129")

    label("loc_1126")

    TalkEnd(0xFF)

    label("loc_1129")

    Return()

    # Function_3_E92 end

    def Function_4_112A(): pass

    label("Function_4_112A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_113B")
    Call(0, 2)
    Return()

    label("loc_113B")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 100, -110, -53600, 0)
    SetChrPos(0x1, 880, 0, -54890, 0)
    SetChrPos(0x2, -1120, -40, -54830, 0)
    SetChrPos(0x3, -140, 0, -55760, 0)
    OP_69(0x0, 0x0)
    OP_6C(45000, 0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 6)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_4_112A end

    def Function_5_12C1(): pass

    label("Function_5_12C1")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 100, -110, -53600, 180)
    SetChrPos(0x2, 880, 0, -54890, 180)
    SetChrPos(0x1, -1120, -40, -54830, 180)
    SetChrPos(0x0, -140, 0, -55760, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 7)
    NewScene("ED6_DT21/M4112   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_5_12C1 end

    def Function_6_141C(): pass

    label("Function_6_141C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1445")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1439():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1439)

    label("loc_1445")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_146E")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1462():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1462)

    label("loc_146E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1497")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_148B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_148B)

    label("loc_1497")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14C0")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_14B4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_14B4)

    label("loc_14C0")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14EC")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_14EC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1503")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1503")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_151A")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_151A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1531")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1531")

    Return()

    # Function_6_141C end

    def Function_7_1532(): pass

    label("Function_7_1532")


    def lambda_1538():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1538)

    def lambda_154A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_154A)

    def lambda_155C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_155C)

    def lambda_156E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_156E)
    Sleep(1000)
    Return()

    # Function_7_1532 end

    def Function_8_1580(): pass

    label("Function_8_1580")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #22
        (
            "\x07\x05　　　　警告！　　　　\x01",
            " 禁止在军事区域摄影\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_1580 end

    SaveToFile()

Try(main)
