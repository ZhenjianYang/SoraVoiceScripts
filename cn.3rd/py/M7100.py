from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7100   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7100.x',
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
        '女性的灵魂',                           # 9
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
        'ED6_DT26/CH20622 ._CH',             # 00
        'ED6_DT07/CH02890 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT26/CH20622P._CP',             # 00
        'ED6_DT07/CH02890P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 7700,
        TriggerZ            = 0,
        TriggerY            = -250,
        TriggerRange        = 1000,
        ActorX              = 7700,
        ActorZ              = 2000,
        ActorY              = -250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_FE",           # 00, 0
        "Function_1_11E",          # 01, 1
        "Function_2_19F",          # 02, 2
        "Function_3_285A",         # 03, 3
        "Function_4_288E",         # 04, 4
        "Function_5_28C2",         # 05, 5
        "Function_6_28F6",         # 06, 6
        "Function_7_292A",         # 07, 7
        "Function_8_29EB",         # 08, 8
        "Function_9_34C7",         # 09, 9
        "Function_10_353F",        # 0A, 10
        "Function_11_35BC",        # 0B, 11
        "Function_12_3639",        # 0C, 12
        "Function_13_36B6",        # 0D, 13
        "Function_14_3758",        # 0E, 14
        "Function_15_37FF",        # 0F, 15
        "Function_16_38A6",        # 10, 16
        "Function_17_394D",        # 11, 17
        "Function_18_3DF8",        # 12, 18
        "Function_19_3EE7",        # 13, 19
        "Function_20_3FA3",        # 14, 20
        "Function_21_40B9",        # 15, 21
    )


    def Function_0_FE(): pass

    label("Function_0_FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_116"),
        (SWITCH_DEFAULT, "loc_11D"),
    )


    label("loc_116")

    Event(0, 18)
    Jump("loc_11D")

    label("loc_11D")

    Return()

    # Function_0_FE end

    def Function_1_11E(): pass

    label("Function_1_11E")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE0C00, 0x230083)
    OP_1B(0x2, 0x0, 0x13)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_156")
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x0)
    Jump("loc_17C")

    label("loc_156")

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

    label("loc_17C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D")
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x85, 0x0)

    label("loc_18D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19E")

    Return()

    # Function_1_11E end

    def Function_2_19F(): pass

    label("Function_2_19F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp204_02.eff")
    LoadEffect(0x1, "map\\mp252_01.eff")
    SetChrPos(0x109, 10, -1500, -27370, 0)
    SetChrPos(0x10F, 700, -1500, -28360, 0)
    SetChrPos(0xF0, -970, -1500, -28200, 0)
    SetChrPos(0xF1, -250, -1500, -29110, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(490, -2200, -27700, 0)
    OP_67(0, 9550, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(45000, 0)
    OP_6E(309, 0)

    def lambda_284():
        OP_6D(650, -1500, -27440, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_284)

    def lambda_29C():
        OP_67(0, 6510, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_29C)

    def lambda_2B4():
        OP_6B(2660, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2B4)

    def lambda_2C4():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2C4)

    def lambda_2D4():
        OP_6E(298, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_2D4)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    PlayEffect(0x0, 0xFF, 0xFF, -160, -1500, -28300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(300)

    def lambda_337():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_337)

    def lambda_349():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_349)

    def lambda_35B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_35B)

    def lambda_36D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_36D)
    WaitChrThread(0x109, 0x1)
    Sleep(500)
    OP_43(0x109, 0x0, 0x0, 0x3)
    Sleep(200)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    Sleep(300)
    OP_43(0xF0, 0x0, 0x0, 0x5)
    Sleep(300)
    OP_43(0xF1, 0x0, 0x0, 0x6)

    def lambda_3B4():
        OP_6D(940, -1500, -22250, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3B4)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #0
        0x10F,
        "#1444F#5P这里是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x109,
        (
            "#1067F#5P看来和『翡翠回廊』一样，\x01",
            "有点像异空间里的回廊……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10F, 0, 400)
    Sleep(300)

    ChrTalk(    #2
        0x10F,
        "#1443F#6P凯文，那是……\x02",
    )

    CloseMessageWindow()

    def lambda_49D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_49D)
    Sleep(100)

    def lambda_4B0():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_4B0)
    Sleep(100)
    OP_8C(0xF0, 0, 400)
    OP_1D(0xDE)
    Fade(1000)
    OP_6D(0, 0, -9000, 0)
    OP_67(0, 8790, -10000, 0)
    OP_6B(3780, 0)
    OP_6C(0, 0)
    OP_6E(429, 0)

    def lambda_50E():
        OP_6D(0, 13800, 0, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_50E)

    def lambda_526():
        OP_67(0, 8200, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_526)

    def lambda_53E():
        OP_6B(4800, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_53E)

    def lambda_54E():
        OP_6E(429, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_54E)
    OP_C8(0x200, 0x46, "C_PLAC41._CH", 0x1, 0x7D0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(1000)
    Fade(1000)
    OP_6D(17200, 7150, 22500, 0)
    OP_67(0, 5900, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(358, 0)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    OP_6D(-17200, 7150, 22500, 0)
    OP_67(0, 5900, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(358, 0)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    OP_6D(-5140, 7150, 180, 0)
    OP_67(0, 8960, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(411, 0)

    def lambda_650():
        OP_6D(-5140, 7150, -5180, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_650)
    SetChrPos(0x109, -1030, 0, -10040, 0)
    SetChrPos(0x10F, 390, 0, -10470, 0)
    SetChrPos(0xF0, -1390, 0, -11870, 0)
    SetChrPos(0xF1, 130, 0, -12450, 0)

    def lambda_6AC():
        OP_8E(0xFE, 0xFFFFFBFA, 0x0, 0xFFFFFB96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6AC)
    Sleep(100)

    def lambda_6CC():
        OP_8E(0xFE, 0x186, 0x0, 0xFFFFFB46, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_6CC)
    Sleep(100)

    def lambda_6EC():
        OP_8E(0xFE, 0xFFFFFA92, 0x0, 0xFFFFF3EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_6EC)
    Sleep(100)

    def lambda_70C():
        OP_8E(0xFE, 0x82, 0x0, 0xFFFFF420, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_70C)
    WaitChrThread(0x109, 0x1)
    Fade(500)
    OP_6D(780, 0, -800, 0)
    OP_67(0, 5260, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(263, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Sleep(500)

    ChrTalk(    #3
        0x109,
        (
            "#1063F#5P金色的门与银色的门……\x02\x03",

            "什么呀，\x01",
            "突然来到这么个故弄玄虚的场景。\x02",
        )
    )

    Jump("loc_7E9")

    label("loc_7E9")

    CloseMessageWindow()
    OP_22(0x15F, 0x0, 0x64)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_854")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8BB")

    label("loc_854")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87C")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8BB")

    label("loc_87C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A4")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8BB")

    label("loc_8A4")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_8BB")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E8")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_94F")

    label("loc_8E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_910")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_94F")

    label("loc_910")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_938")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_94F")

    label("loc_938")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_94F")

    Sleep(1000)

    ChrTalk(    #4
        0x109,
        "#1069F#5P难道又来了吗……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x109, 0x20)
    SetChrChipByIndex(0x109, 0)
    SetChrSubChip(0x109, 0)
    Sleep(500)
    PlayEffect(0x1, 0x0, 0x109, 270, 1250, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC9, 0x0, 0x64)
    OP_0D()
    Sleep(1000)

    def lambda_9EA():
        OP_6D(680, 0, 2800, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9EA)

    def lambda_A02():
        OP_67(0, 4710, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A02)

    def lambda_A1A():
        OP_6B(3370, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A1A)

    def lambda_A2A():
        OP_6C(33000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_A2A)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    SetChrFlags(0x10, 0x1)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 500, 4500, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_A6A():

        label("loc_A6A")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_A6A")

    QueueWorkItem2(0x10, 2, lambda_A6A)
    OP_22(0x99, 0x0, 0x64)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x50, 0x5DC)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE7")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B4E")

    label("loc_AE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0F")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B4E")

    label("loc_B0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B37")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B4E")

    label("loc_B37")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B4E")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7B")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BE2")

    label("loc_B7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA3")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BE2")

    label("loc_BA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCB")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BE2")

    label("loc_BCB")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_BE2")

    Sleep(1000)
    WaitChrThread(0x109, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C19")

    ChrTalk(    #5
        0x105,
        "#1164F#6P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC7")

    label("loc_C19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C45")

    ChrTalk(    #6
        0x107,
        "#065F#6P哇……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC7")

    label("loc_C45")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C71")

    ChrTalk(    #7
        0x10B,
        "#216F#6P哎……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC7")

    label("loc_C71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C9E")

    ChrTalk(    #8
        0x102,
        "#1504F#6P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC7")

    label("loc_C9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC7")

    ChrTalk(    #9
        0x10D,
        "#273F#6P唔……\x02",
    )

    CloseMessageWindow()

    label("loc_CC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CFD")

    ChrTalk(    #10
        0x10E,
        "#173F#6P是那时的……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_D27")

    label("loc_CFD")


    ChrTalk(    #11
        0x10F,
        "#1802F#6P是那个时候的……！？\x02",
    )

    CloseMessageWindow()

    label("loc_D27")

    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #12
        "\x07\x0C\x18#2S#80W……异邦者啊……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #13
        (
            "\x07\x0C\x18#2S#80W与『星杯』之法则相关的人啊……\x02\x03",

            "……你们……能听到吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)

    ChrTalk(    #14
        0x109,
        "#1078F#6P啊，没错……能听到！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #15
        "\x07\x0C\x18#2S#80W前方是……双子回廊……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #16
        (
            "\x07\x0C\x18#2S#80W……不同时通过这两扇门的话……\x01",
            "你们就不能……\x01",
            "……到达更深的深渊……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    PlayEffect(0x1, 0x1, 0x109, 270, 1250, 100, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_22(0x80, 0x0, 0x64)
    Sleep(500)
    OP_82(0x0, 0x0)

    def lambda_F22():
        OP_6D(4270, 0, 890, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F22)

    def lambda_F3A():
        OP_67(0, 5140, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F3A)

    def lambda_F52():
        OP_6B(3570, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F52)
    WaitChrThread(0x109, 0x0)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_A2(0x258A)
    OP_AA(1792)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1073")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_10DA")

    label("loc_1073")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109B")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_10DA")

    label("loc_109B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C3")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_10DA")

    label("loc_10C3")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_10DA")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1107")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_116E")

    label("loc_1107")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_112F")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_116E")

    label("loc_112F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1157")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_116E")

    label("loc_1157")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_116E")

    Sleep(500)

    def lambda_1179():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1179)
    Sleep(100)

    def lambda_118C():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_118C)
    Sleep(100)

    def lambda_119F():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_119F)
    Sleep(100)
    OP_8C(0xF0, 90, 400)
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #17
        (
            "\x07\x0C\x18#2S#80W门的控制权……\x01",
            "……已经交托于石碑……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #18
        (
            "\x07\x0C\x18#2S#80W请与『星杯』赐予的力量一起，\x01",
            "沿着各自的道路前进……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    Fade(500)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_23(0xC9)
    OP_0D()
    Fade(500)
    OP_6D(680, 0, 2800, 0)
    OP_67(0, 4710, -10000, 0)
    OP_6B(3370, 0)
    OP_6C(33000, 0)
    OP_6E(263, 0)

    def lambda_12D2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_12D2)
    Sleep(100)

    def lambda_12E5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_12E5)
    Sleep(100)

    def lambda_12F8():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_12F8)
    Sleep(100)
    OP_8C(0xF1, 0, 400)
    OP_0D()
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #19
        "\x07\x0C\x18#2S#80W……但是……请小心……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #20
        (
            "\x07\x0C\x18#2S#80W一旦进入了『门』……\x01",
            "……没有通过试炼的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    OP_22(0x99, 0x0, 0x64)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
    SetChrFlags(0x10, 0x80)
    Sleep(500)

    ChrTalk(    #21
        0x10F,
        "#1802F#6P啊……\x02",
    )

    CloseMessageWindow()

    def lambda_13FC():
        OP_6D(780, 0, -800, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_13FC)

    def lambda_1414():
        OP_67(0, 5260, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1414)

    def lambda_142C():
        OP_6B(3100, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_142C)

    def lambda_143C():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_143C)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x109, 0x2)
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    ClearChrFlags(0x109, 0x20)
    OP_0D()
    Sleep(500)

    ChrTalk(    #22
        0x109,
        (
            "#1065F#5P原来如此……\x02\x03",

            "我们至今为止所听到的声音\x01",
            "都是出自那女人的啊……\x02\x03",

            "#1063F但是……她到底是何方神圣呢？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15BB")

    ChrTalk(    #23
        0x105,
        (
            "#1163F#6P………………………………\x02\x03",

            "#1167F不过，不管怎么样……\x01",
            "她毕竟告诉了我们一件很重要的事。\x02\x03",

            "#1162F与『星杯』之力一起，\x01",
            "沿着各自的道路前进……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1854")

    label("loc_15BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1668")

    ChrTalk(    #24
        0x10E,
        (
            "#176F#6P………嗯……………\x02\x03",

            "#178F但不管怎么样……\x01",
            "她告诉了我们一件很关键的事。\x02\x03",

            "与『星杯』之力一起，\x01",
            "沿着各自的道路前进……是吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1854")

    label("loc_1668")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1717")

    ChrTalk(    #25
        0x102,
        (
            "#1503F#6P………………………………\x02\x03",

            "#1502F不管如何……\x01",
            "她告诉了我们一件很关键的事。\x02\x03",

            "与『星杯』之力一起，\x01",
            "沿着各自的道路前进，对吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1854")

    label("loc_1717")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17AE")

    ChrTalk(    #26
        0x107,
        (
            "#561F#6P嗯、嗯……\x02\x03",

            "#062F总之……\x01",
            "她告诉了我们一件很关键的事。\x02\x03",

            "与『星杯』之力一起，\x01",
            "沿着各自的道路前进……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1854")

    label("loc_17AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1854")

    ChrTalk(    #27
        0x10B,
        (
            "#416F#6P嗯，没错啊……\x02\x03",

            "#210F也罢，总而言之，\x01",
            "她告诉了我们一件很关键的事。\x02\x03",

            "与『星杯』之力一起，\x01",
            "沿着各自的道路前进，没错吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1854")


    def lambda_185A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_185A)
    OP_8C(0x10F, 225, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1906")

    ChrTalk(    #28
        0x109,
        (
            "#1065F#5P嗯嗯……\x01",
            "意思说得很明白了。\x02\x03",

            "#1063F在这种情况之下……\x01",
            "就是指我和莉丝要分别\x01",
            "进入两个不同的门吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1982")

    label("loc_1906")


    ChrTalk(    #29
        0x109,
        (
            "#1065F#5P啊啊……\x01",
            "意思说得很明白了。\x02\x03",

            "#1063F在这种情况之下……\x01",
            "就是指我和莉丝要分别\x01",
            "进入两个不同的门吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1982")


    ChrTalk(    #30
        0x10F,
        (
            "#1446F#5P……嗯，我也这样认为。\x02\x03",

            "#1443F大概，\x01",
            "如果不那么做的话\x01",
            "是不能到达下一个星层的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x109,
        (
            "#1075F#5P哼……\x01",
            "事情变得麻烦了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A97")

    ChrTalk(    #32
        0x10D,
        (
            "#276F#6P照这样看来，\x01",
            "这回必须要分两路前进不可了。\x02\x03",

            "以现在的人数来看，\x01",
            "有些令人担心呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C8B")

    label("loc_1A97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B18")

    ChrTalk(    #33
        0x10B,
        (
            "#215F#6P归根到底，\x01",
            "必须将现有的伙伴分成两组吧。\x02\x03",

            "可是，以现在的人数来看，\x01",
            "有些令人担心呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C8B")

    label("loc_1B18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B93")

    ChrTalk(    #34
        0x107,
        (
            "#063F#6P归、归根到底，\x01",
            "我们是要分成两组吧。\x02\x03",

            "可是，以现在的人数来看，\x01",
            "心里有些没底……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C8B")

    label("loc_1B93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C11")

    ChrTalk(    #35
        0x102,
        (
            "#1503F#6P无论怎么说，\x01",
            "必须将现有的伙伴分成两组。\x02\x03",

            "但以现在的人数来看，\x01",
            "有些令人担心呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C8B")

    label("loc_1C11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C8B")

    ChrTalk(    #36
        0x10E,
        (
            "#175F#6P无论怎么说，\x01",
            "非把现有的队友分成两组不可。\x02\x03",

            "但以现在的人数来看，\x01",
            "心里有些没底……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D2A")

    ChrTalk(    #37
        0x105,
        (
            "#1160F#6P如果真要这样的话……\x01",
            "不如请留在『据点』的伙伴一起参加，\x01",
            "这样方为上策。\x02\x03",

            "如此一来，\x01",
            "我们就可以每四个人分为一组了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_206C")

    label("loc_1D2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E3E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DC2")

    ChrTalk(    #38
        0x10E,
        (
            "#170F#6P那么……\x01",
            "也许要借助\x01",
            "留在『据点』的伙伴们的力量了。\x02\x03",

            "如此一来，\x01",
            "我们就可以每四个人分为一组了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E3B")

    label("loc_1DC2")


    ChrTalk(    #39
        0x10E,
        (
            "#170F#6P那么……\x01",
            "也许要借助\x01",
            "留在『据点』的伙伴们的力量了。\x02\x03",

            "如此一来，\x01",
            "我们就可以每四个人分为一组了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E3B")

    Jump("loc_206C")

    label("loc_1E3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F67")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1EE6")

    ChrTalk(    #40
        0x102,
        (
            "#1500F#6P那么……\x01",
            "叫上驻扎在『据点』的伙伴\x01",
            "一起参加会更加妥当。\x02\x03",

            "如此一来，\x01",
            "我们就可以每四个人分为一组了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F64")

    label("loc_1EE6")


    ChrTalk(    #41
        0x102,
        (
            "#1500F#6P那么……\x01",
            "叫上驻扎在『据点』的伙伴\x01",
            "一起参加会更加妥当。\x02\x03",

            "如此一来，\x01",
            "我们就可以每四个人分为一组了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F64")

    Jump("loc_206C")

    label("loc_1F67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FED")

    ChrTalk(    #42
        0x107,
        (
            "#560F#6P那、那样的话……\x01",
            "不如叫上留在『据点』的\x01",
            "伙伴们一起来吧？\x02\x03",

            "这样就能够\x01",
            "每四个人分为一组了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_206C")

    label("loc_1FED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_206C")

    ChrTalk(    #43
        0x10B,
        (
            "#210F#6P那么，\x01",
            "不如叫上留在『据点』的\x01",
            "那些人一起过来吧。\x02\x03",

            "这样我们才能\x01",
            "每四个人分为一组行动。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_206C")


    ChrTalk(    #44
        0x10F,
        (
            "#1444F#5P咦……\x02\x03",

            "#1802F但、但是，就刚才的提示来看，\x01",
            "我和凯文要分开行动…… \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x109,
        (
            "#1065F#5P……嗯，\x01",
            "不过从她的语气来看，\x01",
            "并没有说不可以叫帮手来啊。\x02\x03",

            "#1060F更何况，谁知道进去后会发生什么……\x01",
            "这次就老老实实地叫大伙帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10F,
        (
            "#1802F#5P………………………………\x02\x03",

            "#1446F……明白。\x01",
            "那么就请多关照了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2238")
    OP_A2(0x0)

    ChrTalk(    #47
        0x102,
        (
            "#1513F#6P彼此彼此。\x02\x03",

            "#1500F怎么办？\x01",
            "现在就把『据点』里的同伴\x01",
            "都叫到这里来吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2457")

    label("loc_2238")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22B8")
    OP_A2(0x1)

    ChrTalk(    #48
        0x10E,
        (
            "#170F#6P呵呵，彼此彼此。\x02\x03",

            "怎样办？\x01",
            "现在就把『据点』里的大家\x01",
            "都叫到这里来吗？\x02",
        )
    )

    Jump("loc_22B4")

    label("loc_22B4")

    CloseMessageWindow()
    Jump("loc_2457")

    label("loc_22B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2333")
    OP_A2(0x2)

    ChrTalk(    #49
        0x105,
        (
            "#1161F#6P呵呵，彼此彼此。\x02\x03",

            "#1382F怎么办？\x01",
            "现在就把『据点』里的大家\x01",
            "都叫到这里来吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2457")

    label("loc_2333")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23C0")
    OP_A2(0x3)

    ChrTalk(    #50
        0x10D,
        (
            "#277F#6P呵呵……\x01",
            "也要请你们多多关照。\x02\x03",

            "怎样办？\x01",
            "现在就把『据点』里的伙伴\x01",
            "都叫到这里来吗？\x02",
        )
    )

    Jump("loc_23BC")

    label("loc_23BC")

    CloseMessageWindow()
    Jump("loc_2457")

    label("loc_23C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2457")
    OP_A2(0x4)

    ChrTalk(    #51
        0x10B,
        (
            "#416F#6P既、既然这么说了，\x01",
            "那我也无法置身事外。\x02\x03",

            "#210F那，该怎么办？\x01",
            "现在就把留在『据点』的\x01",
            "那些人都叫到这里来吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2522")

    ChrTalk(    #52
        0x109,
        (
            "#1075F#5P不，就算立刻叫大伙儿过来，\x01",
            "大家也需要做好各自的准备，\x02\x03",

            "#1060F一旦进入『门』之后，\x01",
            "应该就不会那么容易回来了……\x02\x03",

            "做好万全的准备，\x01",
            "然后大家再集合在一起吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E1")

    label("loc_2522")


    ChrTalk(    #53
        0x109,
        (
            "#1075F#5P不，就算立刻叫大伙儿过来，\x01",
            "大伙儿也需要做好各自的准备，\x02\x03",

            "#1060F一旦进入『门』之后，\x01",
            "应该就不会那么容易回来了……\x02\x03",

            "做好万全的准备，\x01",
            "之后大家再集合在一起吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25E1")


    def lambda_25E7():
        OP_6B(3600, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_25E7)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #54
        "\x07\x05※关于第三星层的攻略\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #55
        (
            "\x07\x05前方的『第三星层』，\x01",
            "必须将凯文和莉丝分开\x01",
            "以进行各自的冒险和攻略。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #56
        (
            "\x07\x05其他队员可以自由分配到\x01",
            "凯文或者莉丝的队伍中，\x01",
            "可以根据自己的需要任意搭配。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #57
        (
            "\x07\x05另外，需要注意的是，\x01",
            "攻略一旦开始，\x01",
            "会有很长一段时间无法回到『庭院』。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #58
        (
            "\x07\x05＜注＞\x01",
            "要开始攻略的时候，请从石碑的菜单中\x01",
            "选择『开始第三星层的攻略』。\x02",
        )
    )

    Jump("loc_276C")

    label("loc_276C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2802)
    OP_28(0x2F, 0x1, 0x8)
    OP_28(0x2F, 0x1, 0x10)
    OP_28(0x2F, 0x1, 0x20)
    OP_28(0x2F, 0x1, 0x40)
    OP_28(0x2F, 0x1, 0x80)
    OP_6D(-310, 0, -3190, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -310, 0, -3190, 0)
    SetChrPos(0x1, -310, 0, -3190, 0)
    SetChrPos(0x2, -310, 0, -3190, 0)
    SetChrPos(0x3, -310, 0, -3190, 0)
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
    Return()

    # Function_2_19F end

    def Function_3_285A(): pass

    label("Function_3_285A")

    OP_8E(0xFE, 0xFFFFFC90, 0xFFFFFA24, 0xFFFFA7B8, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 225, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_3_285A end

    def Function_4_288E(): pass

    label("Function_4_288E")

    OP_8E(0xFE, 0x28A, 0xFFFFFA24, 0xFFFFA74A, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_4_288E end

    def Function_5_28C2(): pass

    label("Function_5_28C2")

    OP_8E(0xFE, 0xFFFFFAC4, 0xFFFFFA24, 0xFFFFA0C4, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_5_28C2 end

    def Function_6_28F6(): pass

    label("Function_6_28F6")

    OP_8E(0xFE, 0x172, 0xFFFFFA24, 0xFFFFA0A6, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_6_28F6 end

    def Function_7_292A(): pass

    label("Function_7_292A")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_293D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29EA")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "攻略开始\x01",          # 0
            "继续进行准备\x01",      # 1
        )
    )

    Jump("loc_2975")

    label("loc_2975")

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_2991"),
        (SWITCH_DEFAULT, "loc_29DA"),
    )


    label("loc_2991")

    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(300)
    ClearParty()
    OP_DD(0x2, 0x0, 0x0, 256, 16384, 0, 0)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 8)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29E7")

    label("loc_29DA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29E7")

    label("loc_29E7")

    Jump("loc_293D")

    label("loc_29EA")

    Return()

    # Function_7_292A end

    def Function_8_29EB(): pass

    label("Function_8_29EB")

    EventBegin(0x0)
    LoadEffect(0x0, "map\\mpU70_03.eff")
    OP_DF(0x0, 0x1, 0x1)
    Sleep(300)
    OP_6D(6770, 0, 470, 0)
    OP_67(0, 5410, -10000, 0)
    OP_6B(3550, 0)
    OP_6C(45000, 0)
    OP_6E(242, 0)
    SetChrPos(0x0, 6100, 0, -580, 90)
    SetChrPos(0x1, 3350, 0, -1290, 90)
    SetChrPos(0x2, 3220, 0, -2830, 45)
    SetChrPos(0x3, 1650, 0, -2610, 90)
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
    SetChrPos(0x4, 6000, 0, 900, 90)
    SetChrPos(0x5, 3290, 0, 140, 90)
    SetChrPos(0x6, 2530, 0, 1010, 90)
    SetChrPos(0x7, 1370, 0, -1020, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x109, 0x20)
    SetChrChipByIndex(0x109, 0)
    OP_22(0x8F, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 7760, 1000, -160, 0, 0, 0, 3000, 5000, 0, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x109, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x10F, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #59
        0x10F,
        "#1444F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x109,
        "#1060F#6P好像有反应了……\x02",
    )

    CloseMessageWindow()

    def lambda_2C51():
        OP_6D(18970, 8200, 23490, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2C51)

    def lambda_2C69():
        OP_67(0, 3180, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2C69)

    def lambda_2C81():
        OP_6B(4160, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2C81)

    def lambda_2C91():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2C91)

    def lambda_2CA1():
        OP_6E(270, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2CA1)
    WaitChrThread(0x109, 0x0)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_22(0x6C, 0x0, 0x64)
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x78)
    OP_73(0x0)
    OP_22(0x9A, 0x0, 0x64)
    Fade(500)
    OP_6D(-18730, 8200, 24490, 0)
    OP_67(0, 3180, -10000, 0)
    OP_6B(4160, 0)
    OP_6C(308000, 0)
    OP_6E(270, 0)
    OP_0D()
    OP_22(0x6C, 0x0, 0x64)
    OP_B0(0x1, 0x1E)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x78)
    OP_73(0x1)
    OP_22(0x9A, 0x0, 0x64)
    OP_23(0x6C)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    ClearChrFlags(0x109, 0x20)
    SetChrPos(0x0, 780, 0, 1620, 0)
    SetChrPos(0x1, -220, 0, -810, 0)
    SetChrPos(0x2, 1040, 0, -1170, 0)
    SetChrPos(0x3, -90, 0, -2620, 0)
    SetChrPos(0x4, -830, 0, 1540, 0)
    SetChrPos(0x5, -1720, 0, -1000, 0)
    SetChrPos(0x6, -3080, 0, -1530, 0)
    SetChrPos(0x7, -2450, 0, -2880, 0)
    Fade(500)
    OP_6D(660, 0, 1800, 0)
    OP_67(0, 5640, -10000, 0)
    OP_6B(3670, 0)
    OP_6C(45000, 0)
    OP_6E(238, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #61
        0x109,
        "#1065F#5P准备好了吗……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #62
        0x109,
        "#1063F#11P……莉丝，你做好觉悟了吗？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x4, 90, 400)
    Sleep(300)

    ChrTalk(    #63
        0x10F,
        (
            "#1443F#6P……没问题。\x02\x03",

            "#1445F凯文才是……那个……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x109,
        (
            "#1079F#11P嗯？怎么了？\x02\x03",

            "#1066F哈哈，\x01",
            "我不在的话你会很寂寞对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10F,
        (
            "#1446F#6P……怎么可能。\x02\x03",

            "#1448F算了……\x01",
            "我们赶快出发吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x109,
        "#1840F#11PＯＫ。\x02",
    )

    CloseMessageWindow()

    def lambda_2F90():
        OP_6D(690, 0, 950, 1300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2F90)

    def lambda_2FA8():
        OP_67(0, 4900, -10000, 1300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2FA8)

    def lambda_2FC0():
        OP_8C(0x109, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2FC0)
    OP_8C(0x4, 180, 400)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #67
        0x109,
        (
            "#1063F#5P那么……\x01",
            "大家开始进入『第三星层』吧。\x02\x03",

            "只要一直走下去，\x01",
            "就应该能在终点处会合的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x10F,
        (
            "#1446F#5P……说不定\x01",
            "还会碰到『恶魔』之类的敌人。\x02\x03",

            "#1443F前进的时候要谨慎一些，\x01",
            "不要太过勉强。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(360, 150, -1, -1)
    SetChrName("全员")

    AnonymousTalk(    #69
        "\x07\x00#4S 是！\x02",
    )

    Jump("loc_30E6")

    label("loc_30E6")

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)

    def lambda_310E():
        OP_8C(0x109, 45, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_310E)
    OP_8C(0x4, 315, 400)
    Fade(1000)
    OP_DF(0x1, 0x1, 0x1)
    OP_6D(20, -2450, 3710, 0)
    OP_67(0, 6580, -10000, 0)
    OP_6B(4130, 0)
    OP_6C(0, 0)
    OP_6E(380, 0)
    SetChrPos(0x0, 780, 0, 1620, 0)
    SetChrPos(0x1, -220, 0, -810, 0)
    SetChrPos(0x2, 1040, 0, -1170, 0)
    SetChrPos(0x3, -90, 0, -2620, 0)
    ClearChrFlags(0x4, 0x8)
    ClearChrFlags(0x5, 0x8)
    ClearChrFlags(0x6, 0x8)
    ClearChrFlags(0x7, 0x8)
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x4, -830, 0, 1540, 0)
    SetChrPos(0x5, -1720, 0, -1000, 0)
    SetChrPos(0x6, -3080, 0, -1530, 0)
    SetChrPos(0x7, -2450, 0, -2880, 0)
    OP_43(0x0, 0x0, 0x0, 0x9)
    OP_43(0x1, 0x0, 0x0, 0xA)
    OP_43(0x2, 0x0, 0x0, 0xB)
    OP_43(0x3, 0x0, 0x0, 0xC)
    OP_43(0x4, 0x0, 0x0, 0xD)
    OP_43(0x5, 0x0, 0x0, 0xE)
    OP_43(0x6, 0x0, 0x0, 0xF)
    OP_43(0x7, 0x0, 0x0, 0x10)

    def lambda_3269():
        OP_6D(0, 4150, 3710, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3269)

    def lambda_3281():
        OP_67(0, 7170, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_3281)

    def lambda_3299():
        OP_6B(4360, 4000)
        ExitThread()

    QueueWorkItem(0x2, 3, lambda_3299)

    def lambda_32A9():
        OP_6E(380, 4000)
        ExitThread()

    QueueWorkItem(0x3, 3, lambda_32A9)
    OP_0D()
    WaitChrThread(0x0, 0x3)
    Fade(1000)
    OP_6D(18800, 7050, 23300, 0)
    OP_67(0, 7020, -10000, 0)
    OP_6B(3610, 0)
    OP_6C(45000, 0)
    OP_6E(273, 0)
    OP_0D()
    Sleep(4000)
    Fade(1000)
    OP_6D(-19650, 7050, 23550, 0)
    OP_67(0, 7020, -10000, 0)
    OP_6B(3610, 0)
    OP_6C(309000, 0)
    OP_6E(273, 0)
    OP_0D()
    Sleep(3000)
    Fade(500)
    OP_6D(0, 850, 21390, 0)
    OP_67(0, 1390, -10000, 0)
    OP_6B(9200, 0)
    OP_6C(0, 0)
    OP_6E(373, 0)

    def lambda_3391():
        OP_6D(0, 850, 8290, 5000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3391)
    OP_0D()
    OP_22(0x6C, 0x0, 0x64)
    OP_6F(0x0, 120)
    OP_70(0x0, 0x0)
    OP_6F(0x1, 120)
    OP_70(0x1, 0x0)
    OP_73(0x0)
    OP_73(0x1)
    OP_22(0x9A, 0x0, 0x64)
    OP_23(0x6C)
    Sleep(300)
    WaitChrThread(0x0, 0x3)
    OP_20(0x7D0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1500)
    OP_AA(65282)
    SetMessageWindowPos(-1, 120, -1, -1)
    SetChrName("")

    AnonymousTalk(    #70
        "\x07\x05先进行哪一方的路线？\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3431")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34C4")

    Menu(
        3,
        -1,
        -1,
        0,
        (
            "金之道（凯文）\x01",      # 0
            "银之道（莉丝）\x01",      # 1
        )
    )

    MenuEnd(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x3)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3483"),
        (SWITCH_DEFAULT, "loc_34A2"),
    )


    label("loc_3483")

    OP_A2(0x2803)
    OP_DC(0x0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7102   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_34C1")

    label("loc_34A2")

    OP_A2(0x2804)
    OP_DC(0x0, 0x1)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7101   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_34C1")

    label("loc_34C1")

    Jump("loc_3431")

    label("loc_34C4")

    EventEnd(0x0)
    Return()

    # Function_8_29EB end

    def Function_9_34C7(): pass

    label("Function_9_34C7")

    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0x2116, 0x0, 0x1FFD, 0x1388, 0x0)
    OP_8E(0xFE, 0x492A, 0xFA0, 0x4ABA, 0x1388, 0x0)
    OP_8E(0xFE, 0x4952, 0xFA0, 0x5BB8, 0x1388, 0x0)

    def lambda_3514():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3514)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x4948, 0xFA0, 0x71E8, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_9_34C7 end

    def Function_10_353F(): pass

    label("Function_10_353F")

    Sleep(50)
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0x2116, 0x0, 0x1FFD, 0x1388, 0x0)
    OP_8E(0xFE, 0x492A, 0xFA0, 0x4ABA, 0x1388, 0x0)
    OP_8E(0xFE, 0x4952, 0xFA0, 0x5BB8, 0x1388, 0x0)

    def lambda_3591():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3591)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x4948, 0xFA0, 0x71E8, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_10_353F end

    def Function_11_35BC(): pass

    label("Function_11_35BC")

    Sleep(600)
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0x2116, 0x0, 0x1FFD, 0x1388, 0x0)
    OP_8E(0xFE, 0x492A, 0xFA0, 0x4ABA, 0x1388, 0x0)
    OP_8E(0xFE, 0x4952, 0xFA0, 0x5BB8, 0x1388, 0x0)

    def lambda_360E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_360E)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x4948, 0xFA0, 0x71E8, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_11_35BC end

    def Function_12_3639(): pass

    label("Function_12_3639")

    Sleep(800)
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0x2116, 0x0, 0x1FFD, 0x1388, 0x0)
    OP_8E(0xFE, 0x492A, 0xFA0, 0x4ABA, 0x1388, 0x0)
    OP_8E(0xFE, 0x4952, 0xFA0, 0x5BB8, 0x1388, 0x0)

    def lambda_368B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_368B)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x4948, 0xFA0, 0x71E8, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_12_3639 end

    def Function_13_36B6(): pass

    label("Function_13_36B6")

    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0xFFFFE1A6, 0x0, 0x1DF6, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFC41E, 0x7D0, 0x3BD8, 0x1388, 0x0)
    SetChrPos(0x4, -15330, 2000, 15320, 315)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFB62C, 0xFA0, 0x4AC4, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFB640, 0xFA0, 0x5A64, 0x1388, 0x0)

    def lambda_372D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_372D)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFB762, 0xFA0, 0x79B8, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_13_36B6 end

    def Function_14_3758(): pass

    label("Function_14_3758")

    Sleep(100)
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0xFFFFE1A6, 0x0, 0x1DF6, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFC41E, 0x7D0, 0x3BD8, 0x1388, 0x0)
    SetChrPos(0x5, -15330, 2000, 15320, 315)
    Sleep(3300)
    OP_8E(0xFE, 0xFFFFB62C, 0xFA0, 0x4AC4, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFB640, 0xFA0, 0x5A64, 0x1388, 0x0)

    def lambda_37D4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_37D4)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFB762, 0xFA0, 0x79B8, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_14_3758 end

    def Function_15_37FF(): pass

    label("Function_15_37FF")

    Sleep(500)
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0xFFFFE1A6, 0x0, 0x1DF6, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFC41E, 0x7D0, 0x3BD8, 0x1388, 0x0)
    SetChrPos(0x6, -15330, 2000, 15320, 315)
    Sleep(3500)
    OP_8E(0xFE, 0xFFFFB62C, 0xFA0, 0x4AC4, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFB640, 0xFA0, 0x5A64, 0x1388, 0x0)

    def lambda_387B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_387B)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFB762, 0xFA0, 0x79B8, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_15_37FF end

    def Function_16_38A6(): pass

    label("Function_16_38A6")

    Sleep(800)
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0xFFFFE1A6, 0x0, 0x1DF6, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFC41E, 0x7D0, 0x3BD8, 0x1388, 0x0)
    SetChrPos(0x6, -15330, 2000, 15320, 315)
    Sleep(3700)
    OP_8E(0xFE, 0xFFFFB62C, 0xFA0, 0x4AC4, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFB640, 0xFA0, 0x5A64, 0x1388, 0x0)

    def lambda_3922():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3922)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFB762, 0xFA0, 0x79B8, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_16_38A6 end

    def Function_17_394D(): pass

    label("Function_17_394D")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C42")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #71
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_3986")

    label("loc_3986")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3999")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C22")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "开始第三星层的攻略\x01",      # 0
            "回复ＨＰ·ＥＰ\x01",          # 1
            "获得武具\x01",                # 2
            "合成结晶回路\x01",            # 3
            "结束\x01",                    # 4
        )
    )

    Jump("loc_39FE")

    label("loc_39FE")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3A1F"),
        (1, "loc_3B39"),
        (2, "loc_3BB4"),
        (3, "loc_3BE3"),
        (SWITCH_DEFAULT, "loc_3C12"),
    )


    label("loc_3A1F")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #72
        (
            "\x07\x05前方的『第三星层』，\x01",
            "必须将凯文和莉丝分开\x01",
            "以进行各自的冒险和攻略。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #73
        (
            "\x07\x05其他队员可以自由分配到\x01",
            "凯文或者莉丝的队伍中，\x01",
            "可以根据自己的需要任意搭配。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #74
        (
            "\x07\x05另外，需要注意的是，\x01",
            "攻略一旦开始，\x01",
            "会有很长一段时间无法回到『庭院』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Call(0, 7)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C1F")

    label("loc_3B39")

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
    Jump("loc_3C1F")

    label("loc_3BB4")

    OP_A9(0x1A)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #75
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_3BE0")

    label("loc_3BE0")

    Jump("loc_3C1F")

    label("loc_3BE3")

    OP_A9(0x4)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #76
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_3C0F")

    label("loc_3C0F")

    Jump("loc_3C1F")

    label("loc_3C12")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C1F")

    label("loc_3C1F")

    Jump("loc_3999")

    label("loc_3C22")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3DF4")

    label("loc_3C42")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #77
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_3C6C")

    label("loc_3C6C")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DD7")

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

    Jump("loc_3CD1")

    label("loc_3CD1")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3CEE"),
        (1, "loc_3D69"),
        (2, "loc_3D98"),
        (SWITCH_DEFAULT, "loc_3DC7"),
    )


    label("loc_3CEE")

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
    Jump("loc_3DD4")

    label("loc_3D69")

    OP_A9(0x1A)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #78
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_3D95")

    label("loc_3D95")

    Jump("loc_3DD4")

    label("loc_3D98")

    OP_A9(0x4)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #79
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_3DC4")

    label("loc_3DC4")

    Jump("loc_3DD4")

    label("loc_3DC7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3DD4")

    label("loc_3DD4")

    Jump("loc_3C7F")

    label("loc_3DD7")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3DF4")

    TalkEnd(0xFF)
    Return()

    # Function_17_394D end

    def Function_18_3DF8(): pass

    label("Function_18_3DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E09")
    Call(0, 2)
    Return()

    label("loc_3E09")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 10, -1500, -27370, 0)
    SetChrPos(0x1, 700, -1500, -28360, 0)
    SetChrPos(0x2, -970, -1500, -28200, 0)
    SetChrPos(0x3, -250, -1500, -29110, 0)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -160, -1500, -28300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_18_3DF8 end

    def Function_19_3EE7(): pass

    label("Function_19_3EE7")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 10, -1500, -27370, 180)
    SetChrPos(0x2, 700, -1500, -28360, 180)
    SetChrPos(0x1, -970, -1500, -28200, 180)
    SetChrPos(0x0, -250, -1500, -29110, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -160, -1500, -28300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    NewScene("ED6_DT21/M4303   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_19_3EE7 end

    def Function_20_3FA3(): pass

    label("Function_20_3FA3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FCC")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3FC0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3FC0)

    label("loc_3FCC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FF5")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3FE9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3FE9)

    label("loc_3FF5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_401E")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4012():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4012)

    label("loc_401E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4047")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_403B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_403B)

    label("loc_4047")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4073")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4073")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_408A")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_408A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40A1")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_40A1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40B8")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_40B8")

    Return()

    # Function_20_3FA3 end

    def Function_21_40B9(): pass

    label("Function_21_40B9")


    def lambda_40BF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_40BF)

    def lambda_40D1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_40D1)

    def lambda_40E3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_40E3)

    def lambda_40F5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_40F5)
    Sleep(1000)
    Return()

    # Function_21_40B9 end

    SaveToFile()

Try(main)
