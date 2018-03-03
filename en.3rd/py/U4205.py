from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4205   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4205.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60230",
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
        'Celeste D Auslese',                    # 9
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
        'ED6_DT07/CH02890 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH02890P._CP',             # 00
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 2000,
        TriggerZ            = 12000,
        TriggerY            = 65850,
        TriggerRange        = 1000,
        ActorX              = 2000,
        ActorZ              = 12300,
        ActorY              = 65850,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F6",           # 00, 0
        "Function_1_10C",          # 01, 1
        "Function_2_16D",          # 02, 2
        "Function_3_A95",          # 03, 3
    )


    def Function_0_F6(): pass

    label("Function_0_F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10B")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_10B")

    Return()

    # Function_0_F6 end

    def Function_1_10C(): pass

    label("Function_1_10C")

    OP_82(0x80, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 2)), scpexpr(EXPR_END)), "loc_11D")
    OP_64(0x0, 0x1)
    Jump("loc_16C")

    label("loc_11D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 1)), scpexpr(EXPR_END)), "loc_16C")
    LoadEffect(0x0, "map\\mp257_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 2000, 12300, 65850, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    label("loc_16C")

    Return()

    # Function_1_10C end

    def Function_2_16D(): pass

    label("Function_2_16D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 1250, 12000, 47300, 0)
    SetChrPos(0x10F, 2490, 12000, 47420, 0)
    SetChrPos(0xF0, 1250, 12000, 47300, 0)
    SetChrPos(0xF1, 2490, 12000, 47420, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 2000, 12500, 65850, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x96, 0x12C)

    def lambda_1E4():

        label("loc_1E4")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_1E4")

    QueueWorkItem2(0x10, 2, lambda_1E4)
    OP_6D(2990, 12000, 53560, 0)
    OP_67(0, 12150, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(45000, 0)
    OP_6E(303, 0)

    def lambda_234():
        OP_6D(2230, 12000, 55370, 4500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_234)

    def lambda_24C():
        OP_67(0, 9500, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_24C)

    def lambda_264():
        OP_6B(2420, 4500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_264)

    def lambda_274():
        OP_6E(308, 4500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_274)
    FadeToBright(1000, 0)

    def lambda_28D():
        OP_8E(0xFE, 0x442, 0x2EE0, 0xDB2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_28D)
    Sleep(300)

    def lambda_2AD():
        OP_8E(0xFE, 0x97E, 0x2EE0, 0xDAF2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2AD)
    Sleep(500)

    def lambda_2CD():
        OP_8E(0xFE, 0x492, 0x2EE0, 0xD5A2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2CD)
    Sleep(230)

    def lambda_2ED():
        OP_8E(0xFE, 0x9A6, 0x2EE0, 0xD548, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2ED)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37B")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3E2")

    label("loc_37B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A3")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3E2")

    label("loc_3A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CB")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3E2")

    label("loc_3CB")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3E2")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40F")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_476")

    label("loc_40F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_437")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_476")

    label("loc_437")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45F")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_476")

    label("loc_45F")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_476")

    Sleep(1000)

    ChrTalk(    #0
        0x10F,
        "#1444F#4PWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x109,
        "#1063F#6PWh-What the...?\x02",
    )

    CloseMessageWindow()

    def lambda_4B6():
        OP_6D(2760, 12800, 66410, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4B6)

    def lambda_4CE():
        OP_67(0, 6000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4CE)

    def lambda_4E6():
        OP_6B(2200, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4E6)

    def lambda_4F6():
        OP_6C(33000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_4F6)

    def lambda_506():
        OP_6E(340, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_506)
    WaitChrThread(0x109, 0x0)
    Sleep(300)
    SetChrPos(0x109, 1540, 12000, 55880, 0)
    SetChrPos(0x10F, 2880, 12000, 55830, 0)
    SetChrPos(0xF0, 1400, 12000, 54380, 0)
    SetChrPos(0xF1, 2790, 12000, 54400, 0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x200, 0x82, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x200, 0xFFFFFF, 0x1, "C_VIS419._CH")
    OP_C6(0x0, 0x0, 150000, 0, 500)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1500)
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #2
        "\x07\x0C\x18#2S#80WThank you for...coming this far...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #3
        "\x07\x0C\x18#2S#80WI entrust this...to you...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #4
        "\x07\x0C\x18#2S#80W...Please...my...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    FadeToBright(300, 0)
    Sleep(1000)
    OP_22(0x99, 0x0, 0x64)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
    SetChrFlags(0x10, 0x80)
    LoadEffect(0x0, "map\\mp257_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 2000, 12300, 65850, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Fade(500)
    OP_6D(3060, 12000, 56330, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(45000, 0)
    OP_6E(283, 0)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75C")
    OP_62(0xF0, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_7B4")

    label("loc_75C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77F")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_7B4")

    label("loc_77F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A2")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_7B4")

    label("loc_7A2")

    OP_62(0xF0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_7B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D7")
    OP_62(0xF1, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_82F")

    label("loc_7D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FA")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_82F")

    label("loc_7FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81D")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_82F")

    label("loc_81D")

    OP_62(0xF1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_82F")

    Sleep(2000)
    OP_63(0x109)
    OP_63(0x10F)
    OP_63(0xF0)
    OP_63(0xF1)
    Sleep(300)

    ChrTalk(    #5
        0x109,
        "#1063F#6P...Who, or what, was that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10F,
        "#1802F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10E,
        (
            "#173F#6PA-A ghost...?\x02\x03",

            "#175FPerhaps not. There was something...\x01",
            "familiar about it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_932")

    ChrTalk(    #8
        0x102,
        (
            "#1503F#6PAt the very least, it didn't seem like\x01",
            "any ordinary ghost.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A84")

    label("loc_932")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B0")

    ChrTalk(    #9
        0x107,
        (
            "#063F#6PIt surprised me when I first saw it,\x01",
            "but...\x02\x03",

            "I don't know. It didn't feel all that\x01",
            "scary to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A84")

    label("loc_9B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A3C")

    ChrTalk(    #10
        0x10B,
        (
            "#212F#6PI-It surprised me when I first saw it,\x01",
            "sure...\x02\x03",

            "...but it's weird. It didn't seem all that\x01",
            "scary for a ghost.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A84")

    label("loc_A3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A84")

    ChrTalk(    #11
        0x10D,
        "#272F#6PAt the very least, it was no ordinary ghost.\x02",
    )

    CloseMessageWindow()

    label("loc_A84")

    OP_A2(0x2719)
    OP_28(0x2D, 0x1, 0x40)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_16D end

    def Function_3_A95(): pass

    label("Function_3_A95")

    TalkBegin(0xFF)
    OP_82(0x0, 0x2)
    Sleep(500)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05Obtained \x1F\x2A\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x32A, 1)
    OP_A2(0x271A)
    OP_28(0x2D, 0x1, 0x80)
    OP_64(0x0, 0x1)
    TalkEnd(0xFF)
    Return()

    # Function_3_A95 end

    SaveToFile()

Try(main)
