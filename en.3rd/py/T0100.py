from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0100   ._SN',
        MapName             = 'rolent',
        Location            = 'T0100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        'Stella',                               # 9
        'Elissa',                               # 10
        'Mayor Klaus',                          # 11
        'Target Camera',                        # 12
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
        'ED6_DT07/CH01690 ._CH',             # 00
        'ED6_DT07/CH02730 ._CH',             # 01
        'ED6_DT07/CH02350 ._CH',             # 02
        'ED6_DT26/CH20789 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01690P._CP',             # 00
        'ED6_DT07/CH02730P._CP',             # 01
        'ED6_DT07/CH02350P._CP',             # 02
        'ED6_DT26/CH20789P._CP',             # 03
    )

    DeclNpc(
        X                   = -86130,
        Z                   = 0,
        Y                   = 71210,
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
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 82247,
        Z                   = 0,
        Y                   = 2548,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_14A",          # 00, 0
        "Function_1_1A7",          # 01, 1
        "Function_2_1C6",          # 02, 2
        "Function_3_27E",          # 03, 3
        "Function_4_CD6",          # 04, 4
        "Function_5_204A",         # 05, 5
        "Function_6_20A3",         # 06, 6
        "Function_7_20FC",         # 07, 7
        "Function_8_2162",         # 08, 8
        "Function_9_21EF",         # 09, 9
    )


    def Function_0_14A(): pass

    label("Function_0_14A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_175")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 9)
    Jump("loc_1A6")

    label("loc_175")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_194")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_1A6")

    label("loc_194")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_1A6")

    Return()

    # Function_0_14A end

    def Function_1_1A7(): pass

    label("Function_1_1A7")

    OP_B1("T0100_n")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C5")
    OP_71(0x42F, 0x0)
    ExitThread()
    OP_82(0x89, 0x0)

    label("loc_1C5")

    Return()

    # Function_1_1A7 end

    def Function_2_1C6(): pass

    label("Function_2_1C6")

    EventBegin(0x0)
    SetChrPos(0x0, 46140, 0, 20660, 270)
    OP_6D(39440, 250, 23160, 0)
    OP_67(0, 6380, -10000, 0)
    OP_6B(3210, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    def lambda_21C():
        OP_6B(3850, 9000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21C)

    def lambda_22C():
        OP_6D(39440, 250, 23160, 9000)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_22C)

    def lambda_244():
        OP_6C(306000, 9000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_244)
    OP_77(0xFF, 0x92, 0x59, 0x0, 0xFA0)
    Sleep(4000)
    Sleep(2000)
    OP_77(0x40, 0x4C, 0xAA, 0x0, 0xBB8)
    Sleep(3000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T0101   ._SN", 100, 1, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_2_1C6 end

    def Function_3_27E(): pass

    label("Function_3_27E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00#40WThe next day...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_6D(49000, 0, 10440, 0)
    OP_67(0, 3280, -10000, 0)
    OP_6B(3660, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ClearParty()
    AddParty(0x54, 0xEE, 0xFF)
    SetChrPos(0x155, 49000, 0, -6000, 0)
    OP_1D(0xC0)

    def lambda_322():
        OP_6D(49000, 0, 17020, 5000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_322)

    def lambda_33A():
        OP_67(0, 3780, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_33A)
    FadeToBright(2000, 0)
    Sleep(1500)

    def lambda_360():
        OP_8E(0xFE, 0xBF68, 0x0, 0x3BD8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_360)
    WaitChrThread(0x155, 0x1)
    Sleep(500)

    ChrTalk(    #1
        0x155,
        (
            "#296FI can't believe him...\x02\x03",

            "Not even a jumbo mantis or double seahorse\x01",
            "were enough to get a reaction...\x02\x03",

            "#292FHe must have REALLY fancy tastes.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x155, 180, 400)
    Sleep(500)

    ChrTalk(    #2
        0x155,
        (
            "#290F#5PHeehee. OKAY! Today will be the day I'll\x01",
            "impress him! Oh, YES!\x02\x03",

            "#294F#3SNo one can resist the power of the \x01",
            "Bug of Legends!#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(53920, 0, 19930, 0)
    OP_67(0, 6210, -10000, 0)
    OP_6B(3270, 0)
    OP_6C(39000, 0)
    OP_6E(262, 0)
    Sleep(1000)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 54450, 250, 18980, 270)
    OP_70(0x9, 0x1E)
    OP_73(0x9)

    def lambda_51B():
        OP_8E(0xFE, 0xCAA8, 0x0, 0x4A24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_51B)
    Sleep(1000)
    OP_72(0x9, 0x8)
    ExitThread()
    OP_6F(0x9, 30)
    OP_70(0x9, 0x0)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x10, 0x1)
    TurnDirection(0x10, 0x155, 400)
    Sleep(300)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_581():
        OP_6D(49180, 0, 17760, 1500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_581)

    def lambda_599():
        OP_67(0, 4090, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_599)

    def lambda_5B1():
        OP_6C(347000, 1500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_5B1)

    def lambda_5C1():
        OP_8E(0xFE, 0xC364, 0x0, 0x4218, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5C1)

    ChrTalk(    #3
        0x10,
        "#11PWell, hello there, Estelle!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x155, 0x10, 400)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x13, 0x0)

    ChrTalk(    #4
        0x10,
        "#11PWhat are you doing standing around out here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        "#11PAre you off to do some bug catching?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x155,
        (
            "#290F#6PI sure am! But today's not gonna be just\x01",
            "ANY bug-catching day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        "#11POh? Do tell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x155,
        (
            "#291F#6PHeeheehee...\x02\x03",

            "Today, I'm gonna make a special syrup\x01",
            "that attracts bugs!\x02\x03",

            "And with it, I'll be able to catch a super\x01",
            "amazing one!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        "#11PReally? That's interesting!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        "#11P...But seriously. Sweetie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        "#11PYou're eleven now. And a girl.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#11PI think you should be starting to dress a bit\x01",
            "more like one at your age...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x155,
        (
            "#296F#6PBut these're comfier and way easy to move\x01",
            "around in!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_86D():

        label("loc_86D")

        TurnDirection(0xFE, 0x155, 400)
        OP_48()
        Jump("loc_86D")

    QueueWorkItem2(0x10, 2, lambda_86D)

    def lambda_87E():
        OP_8E(0xFE, 0xBF68, 0x0, 0x9218, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_87E)

    ChrTalk(    #14 op#A
        0x155,
        "#291F#6P#10AAnyway, bye!\x02",
    )

    Sleep(1500)

    ChrTalk(    #15
        0x10,
        "#6PE-Estelle?!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x155, 0x1)
    Sleep(1000)

    ChrTalk(    #16
        0x10,
        "#6P*sigh* Some things never change...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(50100, 0, 41020, 0)
    OP_67(0, 6390, -10000, 0)
    OP_6B(3270, 0)
    OP_6C(72000, 0)
    OP_6E(262, 0)
    SetChrPos(0x155, 49730, 0, 29510, 0)
    Sleep(1000)

    def lambda_95D():
        OP_8E(0xFE, 0xC242, 0x0, 0x9FC4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_95D)
    WaitChrThread(0x155, 0x1)
    OP_8C(0x155, 300, 400)
    Sleep(300)

    ChrTalk(    #17
        0x155,
        (
            "#296FOkay! First, I need to get all the ingredients\x01",
            "I need to make my super-duper syrup.\x02\x03",

            "#290FElissa should be able to give me some dragon\x01",
            "beans, so that's easy.\x02\x03",

            "Then there's the fresh milk and fresh eggs...\x01",
            "Tio'll give me some if I ask nicely. Maybe.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Visit Elissa First\x01",          # 0
            "Visit Tio First\x01",             # 1
            "Check for New Sneakers\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    SetMapFlags(0x2000000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B92")

    ChrTalk(    #18
        0x155,
        (
            "#291FI wanna go see Elissa!\x02\x03",

            "#290FI think she's still helping out at the bar\x01",
            "right now...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B6B():
        OP_8E(0xFE, 0x8F7A, 0x0, 0x9FC4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_B6B)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Call(0, 4)
    Jump("loc_CD5")

    label("loc_B92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C23")

    ChrTalk(    #19
        0x155,
        (
            "#290FYou can't beat Tio's place for fresh ingredients!\x02\x03",

            "#291FTo the farm!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BF4():
        OP_8E(0xFE, 0x8F7A, 0x0, 0x9FC4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_BF4)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T0400   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_CD5")

    label("loc_C23")


    ChrTalk(    #20
        0x155,
        (
            "#296FHmm... Actually...\x02\x03",

            "#291F...it might be more fun to go check the\x01",
            "shop for new sneakers right now!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x155, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)

    def lambda_CAC():
        OP_8E(0xFE, 0xC242, 0x0, 0x7346, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_CAC)
    FadeToDark(2000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T0121   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_CD5")

    Return()

    # Function_3_27E end

    def Function_4_CD6(): pass

    label("Function_4_CD6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 29540, 0, 46220, 0)
    OP_44(0x155, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 2)), scpexpr(EXPR_END)), "loc_D54")
    OP_6D(26620, 0, 45190, 0)
    OP_67(0, 6850, -10000, 0)
    OP_6B(3190, 0)
    OP_6C(325000, 0)
    OP_6E(262, 0)
    SetChrPos(0x155, 22320, 0, 38470, 90)
    Jump("loc_DA2")

    label("loc_D54")

    OP_6D(31120, 0, 46190, 0)
    OP_67(0, 6850, -10000, 0)
    OP_6B(3190, 0)
    OP_6C(325000, 0)
    OP_6E(262, 0)
    SetChrPos(0x155, 41170, 0, 43630, 270)

    label("loc_DA2")


    def lambda_DA8():
        OP_6B(3090, 2000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_DA8)
    FadeToBright(2000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 2)), scpexpr(EXPR_END)), "loc_1713")

    ChrTalk(    #21
        0x155,
        "#291F#2PElissaaa!\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_DE1():
        OP_6D(28900, 0, 46160, 3000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_DE1)

    def lambda_DF9():
        OP_67(0, 7150, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_DF9)

    def lambda_E11():
        OP_6C(317000, 3000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_E11)

    def lambda_E21():
        OP_6B(2760, 3000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_E21)
    OP_43(0x155, 0x3, 0x0, 0x6)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_E54():

        label("loc_E54")

        TurnDirection(0xFE, 0x155, 400)
        OP_48()
        Jump("loc_E54")

    QueueWorkItem2(0x11, 2, lambda_E54)
    WaitChrThread(0x155, 0x3)
    OP_44(0x11, 0x2)
    Sleep(300)

    ChrTalk(    #22
        0x11,
        "#11PHi, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x11,
        (
            "#11PI still can't get over how cool Joshua was\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x11,
        "#11PI want to hear him play the harmonica again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x155,
        (
            "#296F#6PYou'll be lucky to get that out of him...\x02\x03",

            "He won't even talk now. He hasn't said a word\x01",
            "since we heard him playing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x11,
        "#11PWhat? For real?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x155,
        (
            "#295F#6PYeah...\x02\x03",

            "Maybe it was my fault for taking his harmonica\x01",
            "without permission and trying to play it, too...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #28
        0x11,
        "#11P*sigh* Oh, you silly thing...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #29
        0x11,
        "#11P...Listen. Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x11,
        "#11PJoshua doesn't seem to want to talk about it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x11,
        (
            "#11P...but it feels to me like he's had some kind of\x01",
            "painful experience that's bothering him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x11,
        "#11PSo...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x155,
        "#290F#6POh, I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x11,
        "#11PYou do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x155,
        (
            "#295F#6PHe's got something serious on his mind--I can\x01",
            "tell. Sometimes, I look at him and he looks like\x01",
            "he's really in pain about something.\x02\x03",

            "#295F...But I don't think I'd be able to help him with\x01",
            "whatever it is, even if I knew.\x02\x03",

            "So that's that.\x02\x03",

            "#290FI just want to try and cheer him up in my own\x01",
            "way for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x11,
        "#11PAww... That's really sweet of you.\x02",
    )

    CloseMessageWindow()
    OP_62(0x155, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x155)
    Sleep(500)

    ChrTalk(    #37
        0x155,
        "#291F#6PAnyway! Gimme some dragon beans!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x11,
        "#11PWhat? Like, the coffee beans?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x11,
        "#11PAnd you're going to use those for...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x155,
        "#290F#6PThat's a secret!\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #41
        0x11,
        "#11PYou're so weird, Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x11,
        (
            "#11PWell, okay. Hold on a sec!\x01",
            "I'll go get some.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x11, 0x3, 0x0, 0x8)

    def lambda_140F():

        label("loc_140F")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_140F")

    QueueWorkItem2(0x155, 2, lambda_140F)
    WaitChrThread(0x11, 0x3)
    OP_44(0x155, 0x2)
    Sleep(300)

    ChrTalk(    #43
        0x11,
        "#11PHere you go.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #44
        "\x07\x05Elissa handed Estelle some \x07\x02Dragon Beans\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2F61)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 2)), scpexpr(EXPR_END)), "loc_16F9")

    ChrTalk(    #45
        0x155,
        (
            "#290F#6PPhew. That's everything I need.\x02\x03",

            "#292FNow all that's left is to put 'em together,\x01",
            "aaaaaand...\x02\x03",

            "...Mistwald, here I come!\x02\x03",

            "#291FHeeheeheeeeee...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #46
        0x11,
        "#11PE-Estelle? What are you planning?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x155,
        (
            "#291F#6PI'll show you later.\x02\x03",

            "#290FYou might pass out from surprise, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x11,
        (
            "#11PYou know what? I think I'm okay with not\x01",
            "knowing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x155,
        "#291F#6PAnyway, see you later!\x02",
    )

    CloseMessageWindow()

    def lambda_1643():

        label("loc_1643")

        TurnDirection(0xFE, 0x155, 400)
        OP_48()
        Jump("loc_1643")

    QueueWorkItem2(0x11, 2, lambda_1643)

    def lambda_1654():
        OP_8E(0xFE, 0x7F08, 0x0, 0xA334, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_1654)
    WaitChrThread(0x155, 0x1)

    def lambda_1674():
        OP_8E(0xFE, 0xB90A, 0x0, 0xA334, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_1674)
    WaitChrThread(0x155, 0x1)
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #50
        0x11,
        "#5P...Aww. Now I wish she told me...\x02",
    )

    CloseMessageWindow()

    def lambda_16DD():
        OP_6B(2660, 3000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_16DD)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Call(0, 9)
    Jump("loc_1710")

    label("loc_16F9")


    ChrTalk(    #51
        0x155,
        "#290F◆Impossible\x02",
    )

    CloseMessageWindow()

    label("loc_1710")

    Jump("loc_2049")

    label("loc_1713")


    ChrTalk(    #52
        0x155,
        "#290F#1PElissaaa!\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_1731():
        OP_6D(29570, 0, 47050, 2000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1731)

    def lambda_1749():
        OP_67(0, 7150, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1749)

    def lambda_1761():
        OP_6C(317000, 2000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_1761)

    def lambda_1771():
        OP_6B(2760, 2000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_1771)
    OP_43(0x155, 0x3, 0x0, 0x5)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_17A4():

        label("loc_17A4")

        TurnDirection(0xFE, 0x155, 400)
        OP_48()
        Jump("loc_17A4")

    QueueWorkItem2(0x11, 2, lambda_17A4)
    WaitChrThread(0x155, 0x3)
    OP_44(0x11, 0x2)
    Sleep(300)

    ChrTalk(    #53
        0x11,
        "#5POh, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x11,
        (
            "#5PI still can't get over how cool Joshua was\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x11,
        "#5PI want to hear him play the harmonica again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x155,
        (
            "#296F#12PYou'll be lucky to get that out of him...\x02\x03",

            "He won't even talk now. He hasn't said a word\x01",
            "since we heard him playing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x11,
        "#5PWhat? For real?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x155,
        (
            "#295F#12PYeah...\x02\x03",

            "Maybe it was my fault for taking his harmonica\x01",
            "without permission and trying to play it, too...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #59
        0x11,
        "#5P*sigh* Oh, you silly thing...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #60
        0x11,
        "#5P...Listen. Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x11,
        "#5PJoshua doesn't seem to want to talk about it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x11,
        (
            "#5P...but it feels to me like he's had some kind of\x01",
            "painful experience that's bothering him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x11,
        "#5PSo...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x155,
        "#290F#12P...Oh, I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x11,
        "#5PYou do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x155,
        (
            "#295F#12PHe's got something serious on his mind--I can\x01",
            "tell. Sometimes, I look at him and he looks like\x01",
            "he's really in pain about something.\x02\x03",

            "#295F...But I don't think I'd be able to help him with\x01",
            "whatever it is, even if I knew.\x02\x03",

            "So...\x02\x03",

            "#290F...that's why I just want to try and cheer him up\x01",
            "in my own way for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x11,
        "#5PAww... That's really sweet of you.\x02",
    )

    CloseMessageWindow()
    OP_62(0x155, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x155)
    Sleep(500)

    ChrTalk(    #68
        0x155,
        "#291F#12PAnyway! Gimme some dragon beans!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x11,
        "#5PWhat? Like, the coffee beans?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x11,
        "#5PAnd you're going to use those for...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x155,
        "#290F#12PThat's a secret!\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #72
        0x11,
        "#5PYou're so weird, Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x11,
        (
            "#5PWell, okay. Hold on a sec!\x01",
            "I'll go get some.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x11, 0x3, 0x0, 0x7)

    def lambda_1D5D():

        label("loc_1D5D")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1D5D")

    QueueWorkItem2(0x155, 2, lambda_1D5D)

    def lambda_1D6E():
        OP_8F(0xFE, 0x7918, 0x0, 0xB0B8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_1D6E)
    WaitChrThread(0x155, 0x1)
    WaitChrThread(0x11, 0x3)
    OP_44(0x155, 0x2)
    Sleep(300)

    ChrTalk(    #74
        0x11,
        "#11PHere you go.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #75
        "\x07\x05Elissa handed Estelle some \x07\x02Dragon Beans\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2F61)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 2)), scpexpr(EXPR_END)), "loc_1E30")

    ChrTalk(    #76
        0x155,
        "#290F◆Impossible\x02",
    )

    CloseMessageWindow()
    Jump("loc_2049")

    label("loc_1E30")


    ChrTalk(    #77
        0x155,
        (
            "#291F#6PThanks! Now I gotta go to Tio's house.\x02\x03",

            "#291FI need to get some fresh milk and eggs\x01",
            "from her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x11,
        "#11PWhat the heck are you planning, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x155,
        (
            "#291F#6PHeeheehee... I'll show you later.\x02\x03",

            "#290FYou might pass out from surprise, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x11,
        (
            "#11PYou know what? I think I'm okay with not\x01",
            "knowing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x155,
        "#291F#6PAnyway, see you later!\x02",
    )

    CloseMessageWindow()

    def lambda_1F91():

        label("loc_1F91")

        TurnDirection(0xFE, 0x155, 400)
        OP_48()
        Jump("loc_1F91")

    QueueWorkItem2(0x11, 2, lambda_1F91)

    def lambda_1FA2():
        OP_8E(0xFE, 0x7918, 0x0, 0xA7E4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_1FA2)
    WaitChrThread(0x155, 0x1)

    def lambda_1FC2():
        OP_8E(0xFE, 0x27A6, 0x0, 0xA7E4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_1FC2)
    WaitChrThread(0x155, 0x1)
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #82
        0x11,
        "...Aww. Now I wish she told me...\x02",
    )

    CloseMessageWindow()

    def lambda_2028():
        OP_6B(2660, 3000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_2028)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T0400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2049")

    Return()

    # Function_4_CD6 end

    def Function_5_204A(): pass

    label("Function_5_204A")

    SetChrPos(0x155, 41930, 0, 42750, 270)

    def lambda_2061():
        OP_8E(0xFE, 0x828C, 0x0, 0xA6FE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_2061)
    WaitChrThread(0x155, 0x1)

    def lambda_2081():
        OP_8E(0xFE, 0x7954, 0x0, 0xB4A0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_2081)
    WaitChrThread(0x155, 0x1)
    TurnDirection(0x155, 0x11, 500)
    Return()

    # Function_5_204A end

    def Function_6_20A3(): pass

    label("Function_6_20A3")

    SetChrPos(0x155, 16329, 0, 41520, 90)

    def lambda_20BA():
        OP_8E(0xFE, 0x7364, 0x0, 0xA230, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_20BA)
    WaitChrThread(0x155, 0x1)

    def lambda_20DA():
        OP_8E(0xFE, 0x7364, 0x0, 0xAD98, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_20DA)
    WaitChrThread(0x155, 0x1)
    TurnDirection(0x155, 0x11, 500)
    Return()

    # Function_6_20A3 end

    def Function_7_20FC(): pass

    label("Function_7_20FC")


    def lambda_2102():
        OP_8E(0xFE, 0x7918, 0x0, 0xB48C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2102)
    WaitChrThread(0x11, 0x1)

    def lambda_2122():
        OP_8E(0xFE, 0x7918, 0x1F4, 0xC81E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2122)
    WaitChrThread(0x11, 0x1)
    Sleep(1500)

    def lambda_2147():
        OP_8E(0xFE, 0x7918, 0x0, 0xB748, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2147)
    WaitChrThread(0x11, 0x1)
    Return()

    # Function_7_20FC end

    def Function_8_2162(): pass

    label("Function_8_2162")


    def lambda_2168():
        OP_8E(0xFE, 0x7918, 0x0, 0xB48C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2168)
    WaitChrThread(0x11, 0x1)

    def lambda_2188():
        OP_8E(0xFE, 0x7918, 0x1F4, 0xC81E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2188)
    WaitChrThread(0x11, 0x1)
    Sleep(1500)

    def lambda_21AD():
        OP_8E(0xFE, 0x7918, 0x0, 0xB48C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_21AD)
    WaitChrThread(0x11, 0x1)

    def lambda_21CD():
        OP_8E(0xFE, 0x7364, 0x0, 0xB48C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_21CD)
    WaitChrThread(0x11, 0x1)
    TurnDirection(0x11, 0x155, 500)
    Return()

    # Function_8_2162 end

    def Function_9_21EF(): pass

    label("Function_9_21EF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x155, 32640, 0, 41530, 90)
    OP_6D(32640, 0, 41530, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    OP_6A(0x155)

    def lambda_2252():
        OP_8E(0xFE, 0xD14C, 0x0, 0xA23A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_2252)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x155, 0x1)
    Sleep(500)
    OP_6A(0xFF)
    OP_62(0x155, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x155)

    def lambda_229E():
        OP_8C(0xFE, 350, 200)
        ExitThread()

    QueueWorkItem(0x155, 2, lambda_229E)

    def lambda_22AC():
        OP_6D(56000, 6000, 48460, 4000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_22AC)

    def lambda_22C4():
        OP_67(0, 4560, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_22C4)

    def lambda_22DC():
        OP_6C(35000, 4000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_22DC)

    def lambda_22EC():
        OP_6B(3440, 4000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_22EC)
    WaitChrThread(0x13, 0x0)
    Sleep(300)
    SetChrFlags(0x155, 0x4)
    SetChrPos(0x155, 53580, 3000, 41530, 350)

    ChrTalk(    #83
        0x155,
        (
            "#296F#5P...\x02\x03",

            "Maybe I'll stop by for a little bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    ClearChrFlags(0x155, 0x4)
    Fade(2000)
    OP_6D(55030, 0, 49600, 0)
    OP_67(0, 8730, -10000, 0)
    OP_6B(2740, 0)
    OP_6C(119000, 0)
    OP_6E(243, 0)
    OP_62(0x155, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    SetChrPos(0x155, 51000, 0, 46100, 0)

    def lambda_23BE():
        OP_8E(0xFE, 0xC738, 0x0, 0xC544, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_23BE)
    WaitChrThread(0x155, 0x1)

    def lambda_23DE():
        OP_8E(0xFE, 0xCD14, 0x0, 0xC544, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_23DE)
    WaitChrThread(0x155, 0x1)
    OP_8C(0x155, 180, 400)
    Sleep(2000)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 59400, 0, 46000, 180)

    def lambda_2420():
        OP_8E(0xFE, 0xE808, 0x0, 0xC544, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2420)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 270, 400)
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #84
        0x12,
        (
            "#600FOh?\x02\x03",

            "If it isn't young Estelle. What are you doing\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_24A1():
        OP_8E(0xFE, 0xD41C, 0x0, 0xC544, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_24A1)
    OP_63(0x155)
    Sleep(200)
    TurnDirection(0x155, 0x12, 500)
    OP_62(0x155, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #85
        0x155,
        "#293F#12POh! Hi, Mr. Mayor!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 0x1)
    OP_8C(0x155, 180, 400)
    Sleep(100)
    OP_8C(0x12, 180, 400)
    Sleep(300)

    ChrTalk(    #86
        0x12,
        (
            "#602F#5PWere you thinking of playing in the clock\x01",
            "tower?\x02\x03",

            "The repairs on it were finally finished last\x01",
            "month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x155,
        "#296F#6PYeah. I know...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x12,
        (
            "#600F#5PThe artisans of the town all put their heads\x01",
            "together to try and make it as close to the\x01",
            "original as possible.\x02\x03",

            "They tried to use as many of the original \x01",
            "materials as they could, too.\x02\x03",

            "So what do you think? It looks almost exactly\x01",
            "like it did, doesn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x155,
        (
            "#295F#6PI guess...\x02\x03",

            "I don't really remember it that well,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x12,
        (
            "#603F#5P...\x02\x03",

            "#600FYou know, looking at this clock tower fills\x01",
            "me with a magical energy.\x02\x03",

            "It makes me feel like everyone in Rolent...\x02\x03",

            "No, like everyone I've ever met is supporting\x01",
            "this town and wishing it well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x155,
        "#296F#6PIt does...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x12,
        "#603F#5PThat's why this spot is really important to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x155,
        "#296F#6POh...\x02",
    )

    CloseMessageWindow()
    OP_62(0x155, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x155)

    ChrTalk(    #94
        0x155,
        "#292F#6PI got'cha!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x155, 290, 500)

    ChrTalk(    #95
        0x155,
        (
            "#294F#5PYou just wait, Joshua!\x02\x03",

            "I'm gonna go catch me the Bug of Legends!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28D2():

        label("loc_28D2")

        TurnDirection(0xFE, 0x155, 500)
        OP_48()
        Jump("loc_28D2")

    QueueWorkItem2(0x12, 2, lambda_28D2)

    ChrTalk(    #96
        0x12,
        (
            "#604F#5PP-Pardon?\x02\x03",

            "U-Umm... Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x155,
        "#291F#5P#3SFull speed ahead!\x02",
    )

    CloseMessageWindow()

    def lambda_292F():
        OP_8E(0xFE, 0xC8F0, 0x0, 0xC544, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_292F)
    WaitChrThread(0x155, 0x1)

    def lambda_294F():
        OP_8E(0xFE, 0xC8F0, 0x0, 0x9178, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_294F)
    WaitChrThread(0x155, 0x1)
    Sleep(1000)

    ChrTalk(    #98
        0x12,
        "#600F#5P...Whatever was that about?\x02",
    )

    CloseMessageWindow()

    def lambda_299D():
        OP_6B(3300, 3000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_299D)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitChrThread(0x13, 0x0)
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    NewScene("ED6_DT21/C0301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_21EF end

    SaveToFile()

Try(main)
