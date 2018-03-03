from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Female Ghost',                         # 9
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
        "Function_3_2F1E",         # 03, 3
        "Function_4_2F52",         # 04, 4
        "Function_5_2F86",         # 05, 5
        "Function_6_2FBA",         # 06, 6
        "Function_7_2FEE",         # 07, 7
        "Function_8_30AB",         # 08, 8
        "Function_9_3BDB",         # 09, 9
        "Function_10_3C53",        # 0A, 10
        "Function_11_3CD0",        # 0B, 11
        "Function_12_3D4D",        # 0C, 12
        "Function_13_3DCA",        # 0D, 13
        "Function_14_3E6C",        # 0E, 14
        "Function_15_3F13",        # 0F, 15
        "Function_16_3FBA",        # 10, 16
        "Function_17_4061",        # 11, 17
        "Function_18_4549",        # 12, 18
        "Function_19_4638",        # 13, 19
        "Function_20_46F4",        # 14, 20
        "Function_21_480A",        # 15, 21
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
        "#1444F#5P...Where are we now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x109,
        (
            "#1067F#5PSomething similar to the Jade Corridor\x01",
            "by the look of it.\x02",
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
        "#1443F#6PKevin. Over there.\x02",
    )

    CloseMessageWindow()

    def lambda_49E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_49E)
    Sleep(100)

    def lambda_4B1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_4B1)
    Sleep(100)
    OP_8C(0xF0, 0, 400)
    OP_1D(0xDE)
    Fade(1000)
    OP_6D(0, 0, -9000, 0)
    OP_67(0, 8790, -10000, 0)
    OP_6B(3780, 0)
    OP_6C(0, 0)
    OP_6E(429, 0)

    def lambda_50F():
        OP_6D(0, 13800, 0, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_50F)

    def lambda_527():
        OP_67(0, 8200, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_527)

    def lambda_53F():
        OP_6B(4800, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_53F)

    def lambda_54F():
        OP_6E(429, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_54F)
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

    def lambda_651():
        OP_6D(-5140, 7150, -5180, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_651)
    SetChrPos(0x109, -1030, 0, -10040, 0)
    SetChrPos(0x10F, 390, 0, -10470, 0)
    SetChrPos(0xF0, -1390, 0, -11870, 0)
    SetChrPos(0xF1, 130, 0, -12450, 0)

    def lambda_6AD():
        OP_8E(0xFE, 0xFFFFFBFA, 0x0, 0xFFFFFB96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6AD)
    Sleep(100)

    def lambda_6CD():
        OP_8E(0xFE, 0x186, 0x0, 0xFFFFFB46, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_6CD)
    Sleep(100)

    def lambda_6ED():
        OP_8E(0xFE, 0xFFFFFA92, 0x0, 0xFFFFF3EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_6ED)
    Sleep(100)

    def lambda_70D():
        OP_8E(0xFE, 0x82, 0x0, 0xFFFFF420, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_70D)
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
            "#1063F#5PA golden and silver gate?\x02\x03",

            "Well, this is foreboding.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x15F, 0x0, 0x64)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_830")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_897")

    label("loc_830")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_858")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_897")

    label("loc_858")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_880")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_897")

    label("loc_880")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_897")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C4")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_92B")

    label("loc_8C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EC")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_92B")

    label("loc_8EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_914")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_92B")

    label("loc_914")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_92B")

    Sleep(1000)

    ChrTalk(    #4
        0x109,
        "#1069F#5PAgain?!\x02",
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

    def lambda_9B4():
        OP_6D(680, 0, 2800, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9B4)

    def lambda_9CC():
        OP_67(0, 4710, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9CC)

    def lambda_9E4():
        OP_6B(3370, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9E4)

    def lambda_9F4():
        OP_6C(33000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_9F4)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    SetChrFlags(0x10, 0x1)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 500, 4500, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_A34():

        label("loc_A34")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_A34")

    QueueWorkItem2(0x10, 2, lambda_A34)
    OP_22(0x99, 0x0, 0x64)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x50, 0x5DC)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB1")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B18")

    label("loc_AB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD9")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B18")

    label("loc_AD9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B01")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B18")

    label("loc_B01")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B18")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B45")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BAC")

    label("loc_B45")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6D")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BAC")

    label("loc_B6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B95")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BAC")

    label("loc_B95")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_BAC")

    Sleep(1000)
    WaitChrThread(0x109, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BDB")

    ChrTalk(    #5
        0x105,
        "#1164F#6POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_C68")

    label("loc_BDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFE")

    ChrTalk(    #6
        0x107,
        "#065F#6PHuh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_C68")

    label("loc_BFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C21")

    ChrTalk(    #7
        0x10B,
        "#216F#6PHuh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_C68")

    label("loc_C21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C46")

    ChrTalk(    #8
        0x102,
        "#1504F#6POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_C68")

    label("loc_C46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C68")

    ChrTalk(    #9
        0x10D,
        "#273F#6PHmm...\x02",
    )

    CloseMessageWindow()

    label("loc_C68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA3")

    ChrTalk(    #10
        0x10E,
        "#173F#6PThe ghost we saw in Grancel!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CCE")

    label("loc_CA3")


    ChrTalk(    #11
        0x10F,
        "#1802F#6PThe ghost we saw in Grancel!\x02",
    )

    CloseMessageWindow()

    label("loc_CCE")

    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #12
        "\x07\x0C\x18#2S#80W...Visitors from afar...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #13
        (
            "\x07\x0C\x18#2S#80WBearers of the grail emblem...\x02\x03",

            "Can you...hear me...?\x02",
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
        "#1078F#6PY-Yeah! We can!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #15
        (
            "\x07\x0C\x18#2S#80WBefore you stands the entrances to the twin\x01",
            "corridors...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #16
        (
            "\x07\x0C\x18#2S#80WProceed through them both in sync...or never\x01",
            "shall you reach the dark depths beyond...\x02",
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

    def lambda_ED3():
        OP_6D(4270, 0, 890, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_ED3)

    def lambda_EEB():
        OP_67(0, 5140, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_EEB)

    def lambda_F03():
        OP_6B(3570, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F03)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1024")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_108B")

    label("loc_1024")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_104C")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_108B")

    label("loc_104C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1074")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_108B")

    label("loc_1074")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_108B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B8")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_111F")

    label("loc_10B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E0")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_111F")

    label("loc_10E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1108")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_111F")

    label("loc_1108")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_111F")

    Sleep(500)

    def lambda_112A():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_112A)
    Sleep(100)

    def lambda_113D():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_113D)
    Sleep(100)

    def lambda_1150():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1150)
    Sleep(100)
    OP_8C(0xF0, 90, 400)
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #17
        (
            "\x07\x0C\x18#2S#80WI entrust their operation...to the monument\x01",
            "before you...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #18
        (
            "\x07\x0C\x18#2S#80WStep forth into the corridors, the power of the \x01",
            "grail with you, and move onward...\x02",
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

    def lambda_12A9():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_12A9)
    Sleep(100)

    def lambda_12BC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_12BC)
    Sleep(100)

    def lambda_12CF():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_12CF)
    Sleep(100)
    OP_8C(0xF1, 0, 400)
    OP_0D()
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #19
        "\x07\x0C\x18#2S#80W...But beware...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #20
        (
            "\x07\x0C\x18#2S#80WOnce you have stepped through the doors...\x01",
            "the trial must be completed...\x02",
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
        "#1802F#6POh...\x02",
    )

    CloseMessageWindow()

    def lambda_13D3():
        OP_6D(780, 0, -800, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_13D3)

    def lambda_13EB():
        OP_67(0, 5260, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13EB)

    def lambda_1403():
        OP_6B(3100, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1403)

    def lambda_1413():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1413)
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
            "#1065F#5PWell, that's one question answered.\x02\x03",

            "That voice we've been hearing all this\x01",
            "time was hers.\x02\x03",

            "#1063F...Although now the next question is:\x01",
            "'Who is she, anyway?'\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15C6")

    ChrTalk(    #23
        0x105,
        (
            "#1163F#6P...\x02\x03",

            "#1167FWhoever she is, she gave us some valuable\x01",
            "advice on how to proceed.\x02\x03",

            "#1162F'Step forth into the corridors, the power of\x01",
            "the grail with you, and move onward...'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18EF")

    label("loc_15C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_168B")

    ChrTalk(    #24
        0x10E,
        (
            "#176F#6PHmm...\x02\x03",

            "#178FWhoever she is, she gave us some valuable\x01",
            "advice on how to proceed.\x02\x03",

            "'Step forth into the corridors, the power of\x01",
            "the grail with you, and move onward...'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18EF")

    label("loc_168B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_174F")

    ChrTalk(    #25
        0x102,
        (
            "#1503F#6P...\x02\x03",

            "#1502FWhoever she is, she gave us some valuable\x01",
            "advice on how to proceed.\x02\x03",

            "'Step forth into the corridors, the power of\x01",
            "the grail with you, and move onward...'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18EF")

    label("loc_174F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_181B")

    ChrTalk(    #26
        0x107,
        (
            "#561F#6PYeah...\x02\x03",

            "#062FWell, either way, she gave us some real\x01",
            "helpful advice on how to proceed.\x02\x03",

            "'Step forth into the corridors, the power\x01",
            "of the grail with you, and move onward...'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18EF")

    label("loc_181B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18EF")

    ChrTalk(    #27
        0x10B,
        (
            "#416F#6PYeah...\x02\x03",

            "#210FStill, whoever she is, she managed to give\x01",
            "us some good advice on how to keep going.\x02\x03",

            "'Step forth into the corridors, the power of\x01",
            "the grail with you, and move onward...'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18EF")


    def lambda_18F5():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_18F5)
    OP_8C(0x10F, 225, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A09")

    ChrTalk(    #28
        0x109,
        (
            "#1065F#5PAnd I say we take her up on that advice.\x01",
            "Moving 'in sync' means we're gonna have\x01",
            "to split up, though.\x02\x03",

            "#1063FOr more like Ries and I have to each take\x01",
            "a door at the same time while you guys tag\x01",
            "along with whoever.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC7")

    label("loc_1A09")


    ChrTalk(    #29
        0x109,
        (
            "#1065F#5PAnd I say we take her up on that advice.\x01",
            "Moving 'in sync' means we're gonna have\x01",
            "to split up, though.\x02\x03",

            "#1063FOr more like Ries and I have to each take\x01",
            "a door at the same time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC7")


    ChrTalk(    #30
        0x10F,
        (
            "#1446F#5PThat's how I took it, too.\x02\x03",

            "#1443FIf we don't do it the way she said,\x01",
            "I doubt we'll be able to advance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x109,
        (
            "#1075F#5PHeh. They sure aren't making it easy for us,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C6A")

    ChrTalk(    #32
        0x10D,
        (
            "#276F#6PThat being the case, we're going to have to divide\x01",
            "ourselves in half to ensure no one goes alone.\x02\x03",

            "That still doesn't make much of a team against\x01",
            "any impending danger, but it's what we'll have to\x01",
            "work with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2004")

    label("loc_1C6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D57")

    ChrTalk(    #33
        0x10B,
        (
            "#215F#6PThat means we're going to need to divide us\x01",
            "among the two groups, right?\x02\x03",

            "With all the stuff we've fought so far, going\x01",
            "up against a new area with only a couple of\x01",
            "people feels...dangerous, don't you think?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2004")

    label("loc_1D57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E16")

    ChrTalk(    #34
        0x107,
        (
            "#063F#6PThat means that we'll have to split up to follow\x01",
            "one of you, right?\x02\x03",

            "With all the stuff we've fought so far, going on\x01",
            "with such small teams feels...dangerous...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2004")

    label("loc_1E16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F0F")

    ChrTalk(    #35
        0x102,
        (
            "#1503F#6PThat means we're going to need to split up us\x01",
            "two so that you guys don't go in alone.\x02\x03",

            "It's still not the most ideal situation when there\x01",
            "are only four of us and things are so dangerous,\x01",
            "but it's what we have to do...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2004")

    label("loc_1F0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2004")

    ChrTalk(    #36
        0x10E,
        (
            "#175F#6PThat means we're going to need to split up us\x01",
            "two so that you guys don't go in alone.\x02\x03",

            "It's still not the most ideal situation when there\x01",
            "are only four of us and things are so dangerous,\x01",
            "but it's what we have to do...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2004")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20C9")

    ChrTalk(    #37
        0x105,
        (
            "#1160F#6PWhy not ask the rest back in the garden to\x01",
            "help us?\x02\x03",

            "That way we could form two groups of four,\x01",
            "and that should hopefully be good enough for\x01",
            "any challenges up ahead.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2526")

    label("loc_20C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2247")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2196")

    ChrTalk(    #38
        0x10E,
        (
            "#170F#6PWhy not ask the rest back in the garden to\x01",
            "help us?\x02\x03",

            "That way we could form two groups of four,\x01",
            "and that should hopefully be plenty for any\x01",
            "challenges up ahead.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2244")

    label("loc_2196")


    ChrTalk(    #39
        0x10E,
        (
            "#170F#6PWhy not ask the rest back in the garden to\x01",
            "help us?\x02\x03",

            "That way we could form two groups of four,\x01",
            "and that should hopefully be plenty for any\x01",
            "challenges up ahead.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2244")

    Jump("loc_2526")

    label("loc_2247")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23E3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2325")

    ChrTalk(    #40
        0x102,
        (
            "#1500F#6PWhy not ask the rest back in the garden to\x01",
            "help us?\x02\x03",

            "That way we could form two groups of four,\x01",
            "and that should hopefully be good enough for\x01",
            "any challenges up ahead.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23E0")

    label("loc_2325")


    ChrTalk(    #41
        0x102,
        (
            "#1500F#6PWhy not go back to the garden and ask the\x01",
            "rest to help us?\x02\x03",

            "That way we could form two groups of four,\x01",
            "and that should hopefully be good enough for\x01",
            "any challenges up ahead.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23E0")

    Jump("loc_2526")

    label("loc_23E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2489")

    ChrTalk(    #42
        0x107,
        (
            "#560F#6PWhy not go back to the garden and ask the\x01",
            "rest to help us?\x02\x03",

            "With them, that should be plenty of people\x01",
            "for anything we come up against.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2526")

    label("loc_2489")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2526")

    ChrTalk(    #43
        0x10B,
        (
            "#210F#6PWhy not ask the rest of the gang to help us?\x02\x03",

            "That way we could form two groups of four.\x01",
            "That's good enough for each door, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2526")


    ChrTalk(    #44
        0x10F,
        (
            "#1444F#5PBut...\x02\x03",

            "#1802FBut that voice said that Kevin and I needed to be\x01",
            "the ones who stepped through the gates...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x109,
        (
            "#1065F#5PSure, but that's all she specified--that you and me\x01",
            "needed to go through different ones.\x02\x03",

            "#1060FShe didn't say anything about what these guys have\x01",
            "to do. Plus, there's no telling what's waiting for us\x01",
            "on the other side. We could use their help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10F,
        (
            "#1802F#5P...\x02\x03",

            "#1446FAll right, then. Thank you.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_274E")
    OP_A2(0x0)

    ChrTalk(    #47
        0x102,
        (
            "#1513F#6PNot a problem.\x02\x03",

            "#1500FSo, what should we do? Should we call everyone\x01",
            "here right away?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_299F")

    label("loc_274E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27D3")
    OP_A2(0x1)

    ChrTalk(    #48
        0x10E,
        (
            "#170F#6PI'll be more than happy to assist.\x02\x03",

            "So, what should we do? Should we call everyone\x01",
            "here right away?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_299F")

    label("loc_27D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2865")
    OP_A2(0x2)

    ChrTalk(    #49
        0x105,
        (
            "#1161F#6PHeehee. I'll be more than happy to help.\x02\x03",

            "#1382FSo, what should we do? Should we call everyone\x01",
            "here right away?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_299F")

    label("loc_2865")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28E3")
    OP_A2(0x3)

    ChrTalk(    #50
        0x10D,
        (
            "#277F#6PHeh. I'll be happy to help.\x02\x03",

            "So, what should we do? Should we call everyone\x01",
            "here right away?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_299F")

    label("loc_28E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_299F")
    OP_A2(0x4)

    ChrTalk(    #51
        0x10B,
        (
            "#416F#6PHey, we've been fighting together up until now...\x01",
            "and we want to get through here, too.\x02\x03",

            "#210FSo, what should we do? Should we call everyone\x01",
            "here right away?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_299F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AEE")

    ChrTalk(    #52
        0x109,
        (
            "#1075F#5PEven if we did, I wouldn't blame them if they\x01",
            "wanted some time to prep before heading out.\x02\x03",

            "#1060FEspecially since I've got a hunch that once we\x01",
            "go in those gates, there's no going back out.\x02\x03",

            "So instead of calling them here, let's go back\x01",
            "to them. Then we'll all come here once we feel\x01",
            "up to the challenge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C2F")

    label("loc_2AEE")


    ChrTalk(    #53
        0x109,
        (
            "#1075F#5PEven if we did, I wouldn't blame them if they\x01",
            "wanted some time to prep before heading out.\x02\x03",

            "#1060FEspecially since I've got a hunch that once we\x01",
            "go in those gates, there's no going back out.\x02\x03",

            "So instead of calling them here, let's go back\x01",
            "to them. Then we'll all come here once we feel\x01",
            "up to the challenge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C2F")


    def lambda_2C35():
        OP_6B(3600, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2C35)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #54
        "\x07\x05The Third Plane\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #55
        (
            "\x07\x05The dungeon on this plane requires you to form two\x01",
            "parties, with Kevin and Ries as their leaders, in order\x01",
            "to advance.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #56
        (
            "\x07\x05Each of the characters you have at this point will\x01",
            "need to be placed in one of these parties.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #57
        (
            "\x07\x05Furthermore, after beginning the dungeon, you won't\x01",
            "be able to return to the garden until it is complete.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #58
        (
            "\x07\x05To begin exploring, inspect the monument at the start\x01",
            "of the third plane and choose 'Explore Third Plane.'\x02",
        )
    )

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

    def Function_3_2F1E(): pass

    label("Function_3_2F1E")

    OP_8E(0xFE, 0xFFFFFC90, 0xFFFFFA24, 0xFFFFA7B8, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 225, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_3_2F1E end

    def Function_4_2F52(): pass

    label("Function_4_2F52")

    OP_8E(0xFE, 0x28A, 0xFFFFFA24, 0xFFFFA74A, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_4_2F52 end

    def Function_5_2F86(): pass

    label("Function_5_2F86")

    OP_8E(0xFE, 0xFFFFFAC4, 0xFFFFFA24, 0xFFFFA0C4, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_5_2F86 end

    def Function_6_2FBA(): pass

    label("Function_6_2FBA")

    OP_8E(0xFE, 0x172, 0xFFFFFA24, 0xFFFFA0A6, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_6_2FBA end

    def Function_7_2FEE(): pass

    label("Function_7_2FEE")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3001")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30AA")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Start Exploring\x01",      # 0
            "Prepare First\x01",        # 1
        )
    )

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_3051"),
        (SWITCH_DEFAULT, "loc_309A"),
    )


    label("loc_3051")

    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(300)
    ClearParty()
    OP_DD(0x2, 0x0, 0x0, 256, 16384, 0, 0)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 8)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30A7")

    label("loc_309A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30A7")

    label("loc_30A7")

    Jump("loc_3001")

    label("loc_30AA")

    Return()

    # Function_7_2FEE end

    def Function_8_30AB(): pass

    label("Function_8_30AB")

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
        "#1444F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x109,
        "#1060F#6PIt's reacting to us.\x02",
    )

    CloseMessageWindow()

    def lambda_3306():
        OP_6D(18970, 8200, 23490, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3306)

    def lambda_331E():
        OP_67(0, 3180, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_331E)

    def lambda_3336():
        OP_6B(4160, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3336)

    def lambda_3346():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3346)

    def lambda_3356():
        OP_6E(270, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_3356)
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
        (
            "#1065F#5PWell, now all that's left is to head through\x01",
            "the doors and see what awaits us.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #62
        0x109,
        "#1063F#11PYou ready to go, Ries?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x4, 90, 400)
    Sleep(300)

    ChrTalk(    #63
        0x10F,
        (
            "#1443F#6P...I am.\x02\x03",

            "#1445FErm... Kevin...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x109,
        (
            "#1079F#11PHmm? What's up?\x02\x03",

            "#1066FHaha. Oh, I get it. Gonna feel all lonely without\x01",
            "me to cuddle up against?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10F,
        (
            "#1446F#6PNot a chance.\x02\x03",

            "#1448FIt's nothing. Let's just get this over with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x109,
        "#1840F#11PYes, ma'am.\x02",
    )

    CloseMessageWindow()

    def lambda_367D():
        OP_6D(690, 0, 950, 1300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_367D)

    def lambda_3695():
        OP_67(0, 4900, -10000, 1300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3695)

    def lambda_36AD():
        OP_8C(0x109, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_36AD)
    OP_8C(0x4, 180, 400)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #67
        0x109,
        (
            "#1063F#5PAll right! Time to make our way through\x01",
            "this plane.\x02\x03",

            "See you guys on the other side. Till then,\x01",
            "take care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x10F,
        (
            "#1446F#5PThere's every chance we might find ourselves\x01",
            "face to face with another devil, too.\x02\x03",

            "#1443FSo stay on guard, and proceed cautiously.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(360, 150, -1, -1)
    SetChrName("Everyone")

    AnonymousTalk(    #69
        "\x07\x00#4SRight!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)

    def lambda_381A():
        OP_8C(0x109, 45, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_381A)
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

    def lambda_3975():
        OP_6D(0, 4150, 3710, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3975)

    def lambda_398D():
        OP_67(0, 7170, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_398D)

    def lambda_39A5():
        OP_6B(4360, 4000)
        ExitThread()

    QueueWorkItem(0x2, 3, lambda_39A5)

    def lambda_39B5():
        OP_6E(380, 4000)
        ExitThread()

    QueueWorkItem(0x3, 3, lambda_39B5)
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

    def lambda_3A9D():
        OP_6D(0, 850, 8290, 5000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3A9D)
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
        "\x07\x05Do Which Route First?\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BD8")

    Menu(
        3,
        -1,
        -1,
        0,
        (
            "Golden Road (Kevin)\x01",      # 0
            "Silver Road (Ries)\x01",       # 1
        )
    )

    MenuEnd(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x3)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3B97"),
        (SWITCH_DEFAULT, "loc_3BB6"),
    )


    label("loc_3B97")

    OP_A2(0x2803)
    OP_DC(0x0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7102   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BD5")

    label("loc_3BB6")

    OP_A2(0x2804)
    OP_DC(0x0, 0x1)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7101   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BD5")

    label("loc_3BD5")

    Jump("loc_3B3C")

    label("loc_3BD8")

    EventEnd(0x0)
    Return()

    # Function_8_30AB end

    def Function_9_3BDB(): pass

    label("Function_9_3BDB")

    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0x2116, 0x0, 0x1FFD, 0x1388, 0x0)
    OP_8E(0xFE, 0x492A, 0xFA0, 0x4ABA, 0x1388, 0x0)
    OP_8E(0xFE, 0x4952, 0xFA0, 0x5BB8, 0x1388, 0x0)

    def lambda_3C28():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C28)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x4948, 0xFA0, 0x71E8, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_9_3BDB end

    def Function_10_3C53(): pass

    label("Function_10_3C53")

    Sleep(50)
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0x2116, 0x0, 0x1FFD, 0x1388, 0x0)
    OP_8E(0xFE, 0x492A, 0xFA0, 0x4ABA, 0x1388, 0x0)
    OP_8E(0xFE, 0x4952, 0xFA0, 0x5BB8, 0x1388, 0x0)

    def lambda_3CA5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CA5)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x4948, 0xFA0, 0x71E8, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_10_3C53 end

    def Function_11_3CD0(): pass

    label("Function_11_3CD0")

    Sleep(600)
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0x2116, 0x0, 0x1FFD, 0x1388, 0x0)
    OP_8E(0xFE, 0x492A, 0xFA0, 0x4ABA, 0x1388, 0x0)
    OP_8E(0xFE, 0x4952, 0xFA0, 0x5BB8, 0x1388, 0x0)

    def lambda_3D22():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D22)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x4948, 0xFA0, 0x71E8, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_11_3CD0 end

    def Function_12_3D4D(): pass

    label("Function_12_3D4D")

    Sleep(800)
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0x2116, 0x0, 0x1FFD, 0x1388, 0x0)
    OP_8E(0xFE, 0x492A, 0xFA0, 0x4ABA, 0x1388, 0x0)
    OP_8E(0xFE, 0x4952, 0xFA0, 0x5BB8, 0x1388, 0x0)

    def lambda_3D9F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D9F)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x4948, 0xFA0, 0x71E8, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_12_3D4D end

    def Function_13_3DCA(): pass

    label("Function_13_3DCA")

    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0xFFFFE1A6, 0x0, 0x1DF6, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFC41E, 0x7D0, 0x3BD8, 0x1388, 0x0)
    SetChrPos(0x4, -15330, 2000, 15320, 315)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFB62C, 0xFA0, 0x4AC4, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFB640, 0xFA0, 0x5A64, 0x1388, 0x0)

    def lambda_3E41():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E41)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFB762, 0xFA0, 0x79B8, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_13_3DCA end

    def Function_14_3E6C(): pass

    label("Function_14_3E6C")

    Sleep(100)
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0xFFFFE1A6, 0x0, 0x1DF6, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFC41E, 0x7D0, 0x3BD8, 0x1388, 0x0)
    SetChrPos(0x5, -15330, 2000, 15320, 315)
    Sleep(3300)
    OP_8E(0xFE, 0xFFFFB62C, 0xFA0, 0x4AC4, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFB640, 0xFA0, 0x5A64, 0x1388, 0x0)

    def lambda_3EE8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3EE8)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFB762, 0xFA0, 0x79B8, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_14_3E6C end

    def Function_15_3F13(): pass

    label("Function_15_3F13")

    Sleep(500)
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0xFFFFE1A6, 0x0, 0x1DF6, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFC41E, 0x7D0, 0x3BD8, 0x1388, 0x0)
    SetChrPos(0x6, -15330, 2000, 15320, 315)
    Sleep(3500)
    OP_8E(0xFE, 0xFFFFB62C, 0xFA0, 0x4AC4, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFB640, 0xFA0, 0x5A64, 0x1388, 0x0)

    def lambda_3F8F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F8F)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFB762, 0xFA0, 0x79B8, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_15_3F13 end

    def Function_16_3FBA(): pass

    label("Function_16_3FBA")

    Sleep(800)
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0xFFFFE1A6, 0x0, 0x1DF6, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFC41E, 0x7D0, 0x3BD8, 0x1388, 0x0)
    SetChrPos(0x6, -15330, 2000, 15320, 315)
    Sleep(3700)
    OP_8E(0xFE, 0xFFFFB62C, 0xFA0, 0x4AC4, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFB640, 0xFA0, 0x5A64, 0x1388, 0x0)

    def lambda_4036():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4036)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFB762, 0xFA0, 0x79B8, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_16_3FBA end

    def Function_17_4061(): pass

    label("Function_17_4061")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43A9")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #71
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_40AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4389")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Explore the Third Plane\x01",      # 0
            "Restore HP/EP\x01",                # 1
            "Shop\x01",                         # 2
            "Synthesize Quartz\x01",            # 3
            "End\x01",                          # 4
        )
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4124"),
        (1, "loc_42A2"),
        (2, "loc_431D"),
        (3, "loc_434B"),
        (SWITCH_DEFAULT, "loc_4379"),
    )


    label("loc_4124")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #72
        (
            "\x07\x05The dungeon on this plane requires you to form two\x01",
            "parties, with Kevin and Ries as their leaders, in order\x01",
            "to advance.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #73
        (
            "\x07\x05Each of the characters you have at this point will\x01",
            "need to be placed in one of these parties.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #74
        (
            "\x07\x05Furthermore, after beginning the dungeon, you won't\x01",
            "be able to return to the garden until it is complete.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Call(0, 7)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4386")

    label("loc_42A2")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    Jump("loc_4386")

    label("loc_431D")

    OP_A9(0x1A)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #75
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_4386")

    label("loc_434B")

    OP_A9(0x4)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #76
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_4386")

    label("loc_4379")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4386")

    label("loc_4386")

    Jump("loc_40AC")

    label("loc_4389")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4545")

    label("loc_43A9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #77
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_43E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4528")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Restore HP/EP\x01",          # 0
            "Shop\x01",                   # 1
            "Synthesize Quartz\x01",      # 2
            "End\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4441"),
        (1, "loc_44BC"),
        (2, "loc_44EA"),
        (SWITCH_DEFAULT, "loc_4518"),
    )


    label("loc_4441")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    Jump("loc_4525")

    label("loc_44BC")

    OP_A9(0x1A)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #78
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_4525")

    label("loc_44EA")

    OP_A9(0x4)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #79
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_4525")

    label("loc_4518")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4525")

    label("loc_4525")

    Jump("loc_43E5")

    label("loc_4528")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4545")

    TalkEnd(0xFF)
    Return()

    # Function_17_4061 end

    def Function_18_4549(): pass

    label("Function_18_4549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_455A")
    Call(0, 2)
    Return()

    label("loc_455A")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_18_4549 end

    def Function_19_4638(): pass

    label("Function_19_4638")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_19_4638 end

    def Function_20_46F4(): pass

    label("Function_20_46F4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_471D")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4711():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4711)

    label("loc_471D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4746")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_473A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_473A)

    label("loc_4746")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_476F")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4763():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4763)

    label("loc_476F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4798")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_478C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_478C)

    label("loc_4798")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47C4")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_47C4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47DB")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_47DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47F2")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_47F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4809")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4809")

    Return()

    # Function_20_46F4 end

    def Function_21_480A(): pass

    label("Function_21_480A")


    def lambda_4810():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4810)

    def lambda_4822():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4822)

    def lambda_4834():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4834)

    def lambda_4846():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4846)
    Sleep(1000)
    Return()

    # Function_21_480A end

    SaveToFile()

Try(main)
