from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M3112   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M3112.x',
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
        'Lt. Colonel Cid',                      # 9
        'Royal Army Soldier',                   # 10
        'Royal Army Soldier',                   # 11
        'Royal Army Soldier',                   # 12
        'Royal Army Soldier',                   # 13
        'Royal Army Soldier',                   # 14
        'Royal Army Soldier',                   # 15
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
        'ED6_DT27/CH03590 ._CH',             # 00
        'ED6_DT27/CH04590 ._CH',             # 01
        'ED6_DT27/CH04591 ._CH',             # 02
        'ED6_DT27/CH04596 ._CH',             # 03
        'ED6_DT27/CH04594 ._CH',             # 04
        'ED6_DT27/CH04595 ._CH',             # 05
        'ED6_DT07/CH00320 ._CH',             # 06
        'ED6_DT07/CH00321 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT27/CH03590P._CP',             # 00
        'ED6_DT27/CH04590P._CP',             # 01
        'ED6_DT27/CH04591P._CP',             # 02
        'ED6_DT27/CH04596P._CP',             # 03
        'ED6_DT27/CH04594P._CP',             # 04
        'ED6_DT27/CH04595P._CP',             # 05
        'ED6_DT07/CH00320P._CP',             # 06
        'ED6_DT07/CH00321P._CP',             # 07
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1CA",          # 00, 0
        "Function_1_1E7",          # 01, 1
        "Function_2_1E8",          # 02, 2
        "Function_3_1F1",          # 03, 3
        "Function_4_1604",         # 04, 4
        "Function_5_1653",         # 05, 5
        "Function_6_16A2",         # 06, 6
        "Function_7_16F1",         # 07, 7
        "Function_8_1740",         # 08, 8
        "Function_9_178F",         # 09, 9
        "Function_10_17DE",        # 0A, 10
        "Function_11_26D0",        # 0B, 11
    )


    def Function_0_1CA(): pass

    label("Function_0_1CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E6")
    Event(0, 2)

    label("loc_1E6")

    Return()

    # Function_0_1CA end

    def Function_1_1E7(): pass

    label("Function_1_1E7")

    Return()

    # Function_1_1E7 end

    def Function_2_1E8(): pass

    label("Function_2_1E8")

    Call(0, 3)
    Call(0, 10)
    Return()

    # Function_2_1E8 end

    def Function_3_1F1(): pass

    label("Function_3_1F1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x7D0)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    LoadEffect(0x2, "monster\\msc1000.eff")
    OP_E0(238, 0x48, 0x2)
    OP_E0(238, 0x49, 0x3)
    OP_E0(239, 0x4A, 0x2)
    OP_E0(239, 0x4B, 0x3)
    OP_E0(240, 0x4C, 0x2)
    OP_E0(240, 0x4D, 0x3)
    OP_E0(241, 0x4E, 0x2)
    OP_E0(241, 0x4F, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 9830, 0, 640, 270)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x109, -570, 0, -3980, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D6")
    SetChrPos(0xEF, -2180, 0, -3890, 0)
    SetChrPos(0xF2, -410, 0, -5470, 0)
    SetChrPos(0xF0, -2310, 0, -5500, 0)
    Jump("loc_35B")

    label("loc_2D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31A")
    SetChrPos(0xF0, -2180, 0, -3890, 0)
    SetChrPos(0xF1, -410, 0, -5470, 0)
    SetChrPos(0xEF, -2310, 0, -5500, 0)
    Jump("loc_35B")

    label("loc_31A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35B")
    SetChrPos(0xF1, -2180, 0, -3890, 0)
    SetChrPos(0xF0, -410, 0, -5470, 0)
    SetChrPos(0xEF, -2310, 0, -5500, 0)

    label("loc_35B")

    OP_6D(-380, 0, -3800, 0)
    OP_67(0, 6030, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(45000, 0)
    OP_6E(259, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #0
        0x10,
        "Man's Voice",
        "#6PI suppose this is where I should welcome you all?\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42C")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_493")

    label("loc_42C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_454")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_493")

    label("loc_454")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47C")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_493")

    label("loc_47C")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_493")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C0")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_527")

    label("loc_4C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E8")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_527")

    label("loc_4E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_510")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_527")

    label("loc_510")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_527")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_554")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5BB")

    label("loc_554")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57C")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5BB")

    label("loc_57C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A4")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5BB")

    label("loc_5A4")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5BB")

    Sleep(1000)
    Fade(500)
    OP_6D(10510, 0, 1480, 0)
    OP_67(0, 5510, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(45000, 0)
    OP_6E(259, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #1
        0x109,
        "#1063F#2PLieutenant Colonel Cid?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10C,
        "#112F#2PSo you're our first opponent...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrPos(0x109, 690, 0, -460, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B6")
    SetChrPos(0xEF, -470, 0, 1320, 90)
    SetChrPos(0xF1, -2240, 0, -810, 90)
    SetChrPos(0xF0, -840, 0, -1340, 90)
    Jump("loc_73B")

    label("loc_6B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FA")
    SetChrPos(0xF0, -470, 0, 1320, 90)
    SetChrPos(0xF1, -2240, 0, -810, 90)
    SetChrPos(0xEF, -840, 0, -1340, 90)
    Jump("loc_73B")

    label("loc_6FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73B")
    SetChrPos(0xF1, -470, 0, 1320, 90)
    SetChrPos(0xF0, -2240, 0, -810, 90)
    SetChrPos(0xEF, -840, 0, -1340, 90)

    label("loc_73B")

    SetChrChipByIndex(0xEE, 8)
    SetChrChipByIndex(0xEF, 10)
    SetChrChipByIndex(0xF0, 12)
    SetChrChipByIndex(0xF1, 14)

    def lambda_755():
        OP_6D(7820, 0, 2250, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_755)

    def lambda_76D():
        OP_67(0, 4690, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_76D)

    def lambda_785():
        OP_6B(2950, 2000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_785)

    def lambda_795():
        OP_6E(305, 2000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_795)
    Sleep(500)

    def lambda_7AA():
        OP_8F(0xFE, 0xF3C, 0x0, 0xFFFFFEC0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7AA)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_830")

    def lambda_7D8():
        OP_8F(0xFE, 0xF8C, 0x0, 0x564, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_7D8)
    Sleep(100)

    def lambda_7F8():
        OP_8F(0xFE, 0x88E, 0x0, 0x4C4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_7F8)
    Sleep(100)

    def lambda_818():
        OP_8F(0xFE, 0x820, 0x0, 0xFFFFFD58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_818)
    Jump("loc_905")

    label("loc_830")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89C")

    def lambda_844():
        OP_8F(0xFE, 0xF8C, 0x0, 0x564, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_844)
    Sleep(100)

    def lambda_864():
        OP_8F(0xFE, 0x88E, 0x0, 0x4C4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_864)
    Sleep(100)

    def lambda_884():
        OP_8F(0xFE, 0x820, 0x0, 0xFFFFFD58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_884)
    Jump("loc_905")

    label("loc_89C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_905")

    def lambda_8B0():
        OP_8F(0xFE, 0xF8C, 0x0, 0x564, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_8B0)
    Sleep(100)

    def lambda_8D0():
        OP_8F(0xFE, 0x88E, 0x0, 0x4C4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_8D0)
    Sleep(100)

    def lambda_8F0():
        OP_8F(0xFE, 0x820, 0x0, 0xFFFFFD58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_8F0)

    label("loc_905")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x1)
    Sleep(500)

    ChrTalk(    #3
        0x10,
        (
            "#701F#11PIt seems like you've been through quite a lot\x01",
            "since we last met, Father Graham.\x02\x03",

            "I certainly hadn't expected this was what was\x01",
            "going to happen back when we met in Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        (
            "#1068F#6PAll of this still feels like a bad dream to me,\x01",
            "too, to be honest...\x02\x03",

            "#1063FYou remember all that happened under Grancel\x01",
            "Cathedral, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        (
            "#703F#2PI do. I can't be sure exactly when the me that\x01",
            "stands before you was created here...\x02\x03",

            "#700F...but I can say it must have been after that if\x01",
            "my memories are anything to go by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        "#1067F#6PHmm...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B78")

    ChrTalk(    #7
        0x10F,
        "#1443F#6PThat's interesting...\x02",
    )

    CloseMessageWindow()

    label("loc_B78")


    ChrTalk(    #8
        0x10,
        (
            "#703F#11PIt's good to see you again, too, Richard.\x02\x03",

            "#701FThis was hardly how I envisioned our reunion\x01",
            "going...but it's good to be able to have one all\x01",
            "the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10C,
        (
            "#119F#6PI could say the same to you.\x02\x03",

            "#118FThat being said, I wasn't expecting a soldier\x01",
            "as formidable as you to be our first opponent.\x01",
            "This bodes poorly for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "#701F#11PHaha. Don't count yourselves out just yet.\x02\x03",

            "#703FEven if I have no intention of being defeated.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)
    SetChrChipByIndex(0x10, 5)

    def lambda_D5D():

        label("loc_D5D")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_D5D")

    QueueWorkItem2(0x10, 3, lambda_D5D)
    PlayEffect(0x2, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, 9470, 100, 3510, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 6730, 100, 4930, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0xFF, 3450, 100, 5170, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x4, 0xFF, 9430, 100, -2260, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x5, 0xFF, 6420, 100, -4250, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x6, 0xFF, 2980, 100, -4470, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F14")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F7B")

    label("loc_F14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F3C")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F7B")

    label("loc_F3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F64")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F7B")

    label("loc_F64")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_F7B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA8")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_100F")

    label("loc_FA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD0")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_100F")

    label("loc_FD0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF8")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_100F")

    label("loc_FF8")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_100F")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_103C")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_10A3")

    label("loc_103C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1064")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_10A3")

    label("loc_1064")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_108C")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_10A3")

    label("loc_108C")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_10A3")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D0")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1137")

    label("loc_10D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F8")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1137")

    label("loc_10F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1120")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1137")

    label("loc_1120")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1137")

    Sleep(1000)

    def lambda_1142():
        OP_6D(7180, 0, 1230, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1142)

    def lambda_115A():
        OP_67(0, 7000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_115A)

    def lambda_1172():
        OP_6B(3320, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1172)

    def lambda_1182():
        OP_6E(255, 3000)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1182)

    def lambda_1192():
        OP_6C(56000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1192)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x11, 9470, -3000, 3510, 225)
    SetChrPos(0x12, 6730, -3000, 4930, 225)
    SetChrPos(0x13, 3450, -3000, 5170, 225)
    SetChrPos(0x14, 9430, -3000, -2260, 270)
    SetChrPos(0x15, 6420, -3000, -4250, 315)
    SetChrPos(0x16, 2980, -3000, -4470, 0)
    OP_22(0x85, 0x1, 0x64)

    def lambda_122B():

        label("loc_122B")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_122B")

    QueueWorkItem2(0x109, 3, lambda_122B)
    OP_43(0x11, 0x0, 0x0, 0x4)
    OP_43(0x12, 0x0, 0x0, 0x5)
    OP_43(0x13, 0x0, 0x0, 0x6)
    OP_43(0x14, 0x0, 0x0, 0x7)
    OP_43(0x15, 0x0, 0x0, 0x8)
    OP_43(0x16, 0x0, 0x0, 0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12BB")

    def lambda_127E():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_127E)
    Sleep(50)

    def lambda_1291():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1291)
    Sleep(50)

    def lambda_12A4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_12A4)
    Sleep(50)
    OP_8C(0xF1, 0, 400)
    Jump("loc_135A")

    label("loc_12BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_130C")

    def lambda_12CF():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_12CF)
    Sleep(50)

    def lambda_12E2():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_12E2)
    Sleep(50)

    def lambda_12F5():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_12F5)
    Sleep(50)
    OP_8C(0xF1, 0, 400)
    Jump("loc_135A")

    label("loc_130C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135A")

    def lambda_1320():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1320)
    Sleep(50)

    def lambda_1333():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1333)
    Sleep(50)

    def lambda_1346():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1346)
    Sleep(50)
    OP_8C(0xF0, 0, 400)

    label("loc_135A")

    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x14, 0x0)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x16, 0x0)
    OP_44(0x109, 0x3)
    OP_44(0x10, 0x3)
    OP_23(0x85)
    OP_1D(0xC4)
    Fade(1000)
    OP_82(0x0, 0x0)
    LoadEffect(0x1, "map\\mp250_00.eff")
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_82(0x5, 0x0)
    OP_82(0x6, 0x0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #11
        0x109,
        "#1063F#6PBah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10C,
        "#112F#6PWe're surrounded!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "#703F#11POn my honor as former garrison commander\x01",
            "of Leiston Fortress...\x02\x03",

            "#704F...I, Lieutenant Colonel Maximillian Cid,\x01",
            "will defeat you!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)
    Sleep(150)
    SetChrSubChip(0x10, 1)
    Sleep(100)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_14CA():
        OP_6D(5800, 0, 1100, 300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_14CA)

    def lambda_14E2():
        OP_67(0, 7350, -10000, 300)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_14E2)

    def lambda_14FA():
        OP_6B(2580, 300)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_14FA)

    def lambda_150A():
        OP_6E(240, 300)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_150A)
    SetChrChipByIndex(0x11, 7)

    def lambda_151F():
        OP_8F(0xFE, 0x1914, 0x0, 0x55A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_151F)
    SetChrChipByIndex(0x12, 7)

    def lambda_153F():
        OP_8F(0xFE, 0x13A6, 0x0, 0x8A2, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_153F)
    SetChrChipByIndex(0x13, 7)

    def lambda_155F():
        OP_8F(0xFE, 0xC94, 0x0, 0x910, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_155F)
    SetChrChipByIndex(0x14, 7)
    OP_8C(0x14, 315, 0)

    def lambda_1586():
        OP_8F(0xFE, 0x17DE, 0x0, 0xFFFFFDB2, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1586)
    SetChrChipByIndex(0x15, 7)
    OP_8C(0x15, 0, 0)

    def lambda_15AD():
        OP_8F(0xFE, 0x12F2, 0x0, 0xFFFFFB5A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_15AD)
    SetChrChipByIndex(0x16, 7)

    def lambda_15CD():
        OP_8F(0xFE, 0xC4E, 0x0, 0xFFFFF8C6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_15CD)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x2A7, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_1F1 end

    def Function_4_1604(): pass

    label("Function_4_1604")

    PlayEffect(0x1, 0xFF, 0xFF, 9470, 100, 3510, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_4_1604 end

    def Function_5_1653(): pass

    label("Function_5_1653")

    PlayEffect(0x1, 0xFF, 0xFF, 6730, 100, 4930, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_5_1653 end

    def Function_6_16A2(): pass

    label("Function_6_16A2")

    PlayEffect(0x1, 0xFF, 0xFF, 3450, 100, 5170, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_6_16A2 end

    def Function_7_16F1(): pass

    label("Function_7_16F1")

    PlayEffect(0x1, 0xFF, 0xFF, 9430, 100, -2260, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_7_16F1 end

    def Function_8_1740(): pass

    label("Function_8_1740")

    PlayEffect(0x1, 0xFF, 0xFF, 6420, 100, -4250, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_8_1740 end

    def Function_9_178F(): pass

    label("Function_9_178F")

    PlayEffect(0x1, 0xFF, 0xFF, 2980, 100, -4470, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_9_178F end

    def Function_10_17DE(): pass

    label("Function_10_17DE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x13, 0x0)
    OP_44(0x14, 0x0)
    OP_44(0x15, 0x0)
    OP_44(0x16, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, 8220, 0, 800, 270)
    SetChrChipByIndex(0x10, 4)
    SetChrSubChip(0x10, 3)
    OP_43(0x10, 0x3, 0x0, 0xB)
    LoadEffect(0x0, "map\\mp259_02.eff")
    LoadEffect(0x1, "map\\mp256_00.eff")
    OP_22(0x146, 0x1, 0x3C)
    PlayEffect(0x0, 0x0, 0x10, 50, 600, 100, 0, 0, 0, 2200, 2400, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x109, 5360, 0, -400, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_190A")
    SetChrPos(0xEF, 5560, 0, 1260, 90)
    SetChrPos(0xF1, 3720, 0, 1170, 90)
    SetChrPos(0xF0, 3700, 0, -530, 90)
    Jump("loc_198F")

    label("loc_190A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_194E")
    SetChrPos(0xF0, 5560, 0, 1260, 90)
    SetChrPos(0xF1, 3720, 0, 1170, 90)
    SetChrPos(0xEF, 3700, 0, -530, 90)
    Jump("loc_198F")

    label("loc_194E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_198F")
    SetChrPos(0xF1, 5560, 0, 1260, 90)
    SetChrPos(0xF0, 3720, 0, 1170, 90)
    SetChrPos(0xEF, 3700, 0, -530, 90)

    label("loc_198F")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(7460, 0, 1820, 0)
    OP_67(0, 4970, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(45000, 0)
    OP_6E(273, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #14
        0x10,
        (
            "#703F#11P...I expected no less from you, Richard...\x02\x03",

            "#701FWith a knight of the Gralsritter on your side,\x01",
            "my loss was likely guaranteed from the start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10C,
        (
            "#110F#6PNot at all. Breaking through your defensive\x01",
            "formation was a real challenge.\x02\x03",

            "It's clear you've already surpassed me as a \x01",
            "commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "#701F#11POh, hardly. I've still got a long way to go before\x01",
            "I can say that with confidence.\x02\x03",

            "#703FAnd while I wouldn't ordinarily tell you as much,\x01",
            "I won't waste this chance fate has granted me...\x02\x03",

            "#700FI still deeply regret that you decided to leave\x01",
            "the army behind, Richard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10C,
        (
            "#119F#6PHaha... That was how I felt about Brigadier\x01",
            "General Bright, and I'm sure you remember\x01",
            "where that led me.\x02\x03",

            "#111FOur paths have parted, but we both inherited\x01",
            "at least part of him.\x02\x03",

            "I have the path of the sword and you have\x01",
            "the path of a soldier. While they may differ,\x01",
            "we can both work towards the same goal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        "#701F#11PHaha... You're right, I suppose.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x10, 0x800)
    PlayEffect(0x0, 0x0, 0x10, -100, 800, 100, 0, 0, 0, 2200, 3500, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)

    def lambda_1E19():

        label("loc_1E19")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1E19")

    QueueWorkItem2(0x109, 3, lambda_1E19)

    def lambda_1E2A():
        OP_6D(7050, 0, 1890, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1E2A)
    OP_8F(0x10, 0x1B58, 0x0, 0x3E8, 0x3E8, 0x0)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #19
        0x10,
        "#701F#11PTake this.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05Lt. Colonel Cid handed Richard the \x1F\x32\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x332, 1)
    OP_8F(0x10, 0x1F40, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_44(0x109, 0x3)
    Sleep(300)

    ChrTalk(    #21
        0x10C,
        "#113F#6PThe key to the barracks?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "#703F#11PAs it seems you're aware, I'm but the first\x01",
            "of several opponents you will face here.\x02\x03",

            "#701FYou'll want to prepare yourselves. The worst\x01",
            "is still yet to come.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20D4")
    Sleep(500)

    ChrTalk(    #23
        0x10,
        (
            "#703F#11PKevin, Ries...\x02\x03",

            "#700FPlease, do all that you can to lead everyone\x01",
            "trapped in this world safely back out of it.\x02\x03",

            "I have a feeling you're the only ones who can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10F,
        "#1802F#6PHow could we say no...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x109,
        "#1840F#6PLeave it to us. We will.\x02",
    )

    CloseMessageWindow()
    Jump("loc_21AC")

    label("loc_20D4")

    Sleep(500)

    ChrTalk(    #26
        0x10,
        (
            "#703F#2PFather Graham...\x02\x03",

            "#700FPlease, do all that you can to lead everyone\x01",
            "trapped in this world safely back out of it.\x02\x03",

            "I have a feeling you're the only one who can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x109,
        "#1840F#6PLeave it to me. I will.\x02",
    )

    CloseMessageWindow()

    label("loc_21AC")

    Sleep(300)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x10, -100, -600, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_21F6():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_21F6)
    OP_23(0x146)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_44(0x10, 0x3)

    def lambda_2215():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2215)
    Sleep(800)
    Fade(1000)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_0D()
    SetChrFlags(0x10, 0x80)
    OP_6D(6450, 0, 1710, 1000)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2271")

    ChrTalk(    #28
        0x107,
        "#063F#6POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_22B7")

    label("loc_2271")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2295")

    ChrTalk(    #29
        0x10A,
        "#813F#6POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_22B7")

    label("loc_2295")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22B7")

    ChrTalk(    #30
        0x10F,
        "#1445F#6POh...\x02",
    )

    CloseMessageWindow()

    label("loc_22B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22F2")

    ChrTalk(    #31
        0x10E,
        "#176F#6PHe always was a dutiful man.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2400")

    label("loc_22F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2338")

    ChrTalk(    #32
        0x106,
        "#552F#6PHonestly...he's always been a good guy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2400")

    label("loc_2338")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_237B")

    ChrTalk(    #33
        0x103,
        "#1534F#6PHaha... He's quite the dutiful man.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2400")

    label("loc_237B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23C4")

    ChrTalk(    #34
        0x10B,
        "#215F#6PS-Seems like a pretty upstanding guy, huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2400")

    label("loc_23C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2400")

    ChrTalk(    #35
        0x110,
        "#267F#6PSeems like a pretty dutiful guy.\x02",
    )

    CloseMessageWindow()

    label("loc_2400")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2435")

    ChrTalk(    #36
        0x105,
        "#1383F#6PHeehee. How very him.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2467")

    label("loc_2435")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2467")

    ChrTalk(    #37
        0x101,
        "#1025F#6PHeehee. How very him.\x02",
    )

    CloseMessageWindow()

    label("loc_2467")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24BA")

    ChrTalk(    #38
        0x10D,
        (
            "#278F#6PI wonder if all Liberlian soldiers are this\x01",
            "upstanding?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24FD")

    ChrTalk(    #39
        0x104,
        "#1541F#6PHeh. He's the very model of a soldier.\x02",
    )

    CloseMessageWindow()

    label("loc_24FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2542")

    ChrTalk(    #40
        0x102,
        "#1513F#6PIt's hard not to respect him, really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2579")

    label("loc_2542")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2579")

    ChrTalk(    #41
        0x108,
        "#070F#6PHaha... He's quite the guy.\x02",
    )

    CloseMessageWindow()

    label("loc_2579")


    ChrTalk(    #42
        0x10C,
        "#116F#5P...\x02",
    )

    CloseMessageWindow()

    def lambda_2590():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_2590)
    Sleep(200)
    OP_8C(0x109, 0, 400)
    Sleep(300)

    ChrTalk(    #43
        0x10C,
        (
            "#110F#5PWell, we should move on.\x02\x03",

            "He's shown us the path forward--we shouldn't\x01",
            "let his good will go to waste.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2680")

    ChrTalk(    #44
        0x109,
        "#1060F#12PGot it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10F,
        "#1806F#6PWe should make our way to the barracks, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_26BF")

    label("loc_2680")


    ChrTalk(    #46
        0x109,
        (
            "#1075F#12PGot it.\x02\x03",

            "#1060FOff to the barracks we go, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26BF")

    OP_A2(0x2B1A)
    OP_28(0x39, 0x1, 0x20)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_10_17DE end

    def Function_11_26D0(): pass

    label("Function_11_26D0")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26F1")
    Sleep(100)
    Jump("loc_276C")

    label("loc_26F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2706")
    Sleep(200)
    Jump("loc_276C")

    label("loc_2706")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_271B")
    Sleep(300)
    Jump("loc_276C")

    label("loc_271B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2730")
    Sleep(400)
    Jump("loc_276C")

    label("loc_2730")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2745")
    Sleep(500)
    Jump("loc_276C")

    label("loc_2745")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_275A")
    Sleep(600)
    Jump("loc_276C")

    label("loc_275A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_276C")
    Sleep(700)

    label("loc_276C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_278E")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_276C")

    label("loc_278E")

    Return()

    # Function_11_26D0 end

    SaveToFile()

Try(main)
