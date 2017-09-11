from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1303   ._SN',
        MapName             = 'Bose',
        Location            = 'C1303.x',
        MapIndex            = 52,
        MapDefaultBGM       = "ed60031",
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
        'Josette',                              # 9
        'Kyle',                                 # 10
        'Don',                                  # 11
        'Bottle',                               # 12
        'Target Camera',                        # 13
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
        Unknown_3A              = 52,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00310 ._CH',             # 00
        'ED6_DT07/CH00300 ._CH',             # 01
        'ED6_DT07/CH00290 ._CH',             # 02
        'ED6_DT07/CH02130 ._CH',             # 03
        'ED6_DT07/CH02120 ._CH',             # 04
        'ED6_DT07/CH02110 ._CH',             # 05
        'ED6_DT07/CH00292 ._CH',             # 06
        'ED6_DT07/CH00100 ._CH',             # 07
        'ED6_DT07/CH00101 ._CH',             # 08
        'ED6_DT07/CH00110 ._CH',             # 09
        'ED6_DT07/CH00111 ._CH',             # 0A
        'ED6_DT07/CH00130 ._CH',             # 0B
        'ED6_DT07/CH00131 ._CH',             # 0C
        'ED6_DT07/CH00120 ._CH',             # 0D
        'ED6_DT07/CH00121 ._CH',             # 0E
        'ED6_DT07/CH00314 ._CH',             # 0F
        'ED6_DT07/CH00304 ._CH',             # 10
        'ED6_DT07/CH00294 ._CH',             # 11
        'ED6_DT07/CH00311 ._CH',             # 12
        'ED6_DT07/CH00301 ._CH',             # 13
        'ED6_DT07/CH00291 ._CH',             # 14
        'ED6_DT07/CH00305 ._CH',             # 15
        'ED6_DT06/CH20065 ._CH',             # 16
        'ED6_DT06/CH20066 ._CH',             # 17
        'ED6_DT06/CH20067 ._CH',             # 18
    )

    AddCharChipPat(
        'ED6_DT07/CH00310P._CP',             # 00
        'ED6_DT07/CH00300P._CP',             # 01
        'ED6_DT07/CH00290P._CP',             # 02
        'ED6_DT07/CH02130P._CP',             # 03
        'ED6_DT07/CH02120P._CP',             # 04
        'ED6_DT07/CH02110P._CP',             # 05
        'ED6_DT07/CH00292P._CP',             # 06
        'ED6_DT07/CH00100P._CP',             # 07
        'ED6_DT07/CH00101P._CP',             # 08
        'ED6_DT07/CH00110P._CP',             # 09
        'ED6_DT07/CH00111P._CP',             # 0A
        'ED6_DT07/CH00130P._CP',             # 0B
        'ED6_DT07/CH00131P._CP',             # 0C
        'ED6_DT07/CH00120P._CP',             # 0D
        'ED6_DT07/CH00121P._CP',             # 0E
        'ED6_DT07/CH00314P._CP',             # 0F
        'ED6_DT07/CH00304P._CP',             # 10
        'ED6_DT07/CH00294P._CP',             # 11
        'ED6_DT07/CH00311P._CP',             # 12
        'ED6_DT07/CH00301P._CP',             # 13
        'ED6_DT07/CH00291P._CP',             # 14
        'ED6_DT07/CH00305P._CP',             # 15
        'ED6_DT06/CH20065P._CP',             # 16
        'ED6_DT06/CH20066P._CP',             # 17
        'ED6_DT06/CH20067P._CP',             # 18
    )

    DeclNpc(
        X                   = -36460,
        Z                   = 0,
        Y                   = -82960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35810,
        Z                   = 0,
        Y                   = -83940,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -34100,
        Z                   = 0,
        Y                   = -82100,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -34310,
        Z                   = 1000,
        Y                   = -83180,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1C0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 1000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -22008,
        Y                   = -3000,
        Z                   = -168710,
        Range               = -26065,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFD625F,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )


    DeclActor(
        TriggerX            = -36040,
        TriggerZ            = 0,
        TriggerY            = -121030,
        TriggerRange        = 800,
        ActorX              = -36040,
        ActorZ              = 1000,
        ActorY              = -121030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -75460,
        TriggerZ            = 0,
        TriggerY            = -119560,
        TriggerRange        = 1000,
        ActorX              = -75450,
        ActorZ              = 1500,
        ActorY              = -118890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_27A",          # 00, 0
        "Function_1_27B",          # 01, 1
        "Function_2_2C5",          # 02, 2
        "Function_3_2DB",          # 03, 3
        "Function_4_281B",         # 04, 4
        "Function_5_2874",         # 05, 5
        "Function_6_28BA",         # 06, 6
        "Function_7_28E5",         # 07, 7
        "Function_8_290B",         # 08, 8
        "Function_9_2A87",         # 09, 9
    )


    def Function_0_27A(): pass

    label("Function_0_27A")

    Return()

    # Function_0_27A end

    def Function_1_27B(): pass

    label("Function_1_27B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28D")
    OP_6F(0x2, 0)
    Jump("loc_294")

    label("loc_28D")

    OP_6F(0x2, 60)

    label("loc_294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB")
    OP_6F(0x0, 0)
    OP_72(0x0, 0x10)
    Jump("loc_2AF")

    label("loc_2AB")

    OP_64(0x0, 0x1)

    label("loc_2AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x389), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C4")

    Return()

    # Function_1_27B end

    def Function_2_2C5(): pass

    label("Function_2_2C5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2C5")

    label("loc_2DA")

    Return()

    # Function_2_2C5 end

    def Function_3_2DB(): pass

    label("Function_3_2DB")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05A familiar voice can be heard.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #1
        0x101,
        "#002FIs this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        (
            "#012FYep...it looks like the sky bandit\x01",
            "boss' room.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Eavesdrop and then raid the room]\x01",      # 0
            "[Not yet]\x01",                               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_3EE"),
        (0, "loc_3F3"),
        (SWITCH_DEFAULT, "loc_281A"),
    )


    label("loc_3EE")

    EventEnd(0x1)
    Jump("loc_281A")

    label("loc_3F3")

    OP_20(0x5DC)
    Fade(1000)
    OP_6D(-34780, 0, -82570, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0xB, -34290, 500, -83750, 45)
    SetMapFlags(0x400000)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x2)
    SetChrSubChip(0xB, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    TurnDirection(0x8, 0xA, 0)
    TurnDirection(0x9, 0xA, 0)
    OP_8C(0xA, 225, 0)
    OP_51(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    OP_21()
    OP_1D(0x57)
    Sleep(500)

    ChrTalk(    #3
        0xA,
        (
            "#193FBwa ha ha...so the queen's gonna\x01",
            "pay out the ransom, is she?\x02\x03",

            "Now, we can finally say goodbye\x01",
            "to this meager living.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        (
            "#6P#200FDon't get careless, Bro. We haven't\x01",
            "got the money in hand yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#211FYeah, and we'll need to decide on a\x01",
            "plan on how to let the hostages go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xA,
        (
            "#193FLet the hostages go?\x02\x03",

            "Now hold on a minute. Why do\x01",
            "we have to bother with that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        "#213FEh? But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xA,
        (
            "#193FOnce we get our mira, we'll just kill\x01",
            "them all and be done with it.\x02\x03",

            "We've no need to leave them alive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        "#216FD-Don...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x9,
        "#6P#201FY-You're joking, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xA,
        (
            "#193FThey know exactly what we look\x01",
            "like, remember?\x02\x03",

            "Even if we left Liberl for good,\x01",
            "we could still be tracked, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#214FB-But there are old people and\x01",
            "kids among them!\x02\x03",

            "Do you really intend to kill\x01",
            "them all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xA,
        (
            "#193FI swear, no matter how old you\x01",
            "get, you never grow up.\x02\x03",

            "This isn't play time, get it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        "#215FB-But...I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x9,
        (
            "#6P#203FI'm sorry to say this, Bro, but I'm\x01",
            "against killing the hostages too.\x02\x03",

            "Aidios will never forgive us if\x01",
            "we do that.\x02\x03",

            "#200FAnd...I don't want to get our home\x01",
            "back with mira stained in the blood\x01",
            "of innocent people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xA,
        (
            "#193F...\x02\x03",

            "Kyle...since when did you become\x01",
            "the boss around here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x9,
        "#6P#200FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xA,
        (
            "#195FI think it's about time you learned\x01",
            "your place!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)
    SetChrChipByIndex(0xA, 22)
    SetChrSubChip(0xA, 0)
    Sleep(150)
    TurnDirection(0xA, 0x9, 0)
    SetChrChipByIndex(0xB, 23)

    def lambda_9DD():

        label("loc_9DD")

        OP_99(0xFE, 0x0, 0x7, 0x6A4)
        OP_48()
        Jump("loc_9DD")

    QueueWorkItem2(0xB, 1, lambda_9DD)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x80)
    OP_22(0x84, 0x0, 0x64)
    SetChrSubChip(0xA, 1)
    Sleep(150)
    SetChrSubChip(0xA, 2)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -34270, 980, -81780, 225)
    OP_96(0xB, 0xFFFF73C4, 0x190, 0xFFFEB902, 0x3E8, 0x1770)

    def lambda_A3B():
        OP_95(0xB, 0x0, 0xFFFFFC18, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_A3B)

    def lambda_A59():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A59)
    OP_22(0x22B, 0x0, 0x64)
    OP_22(0xF8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x32)
    OP_44(0x9, 0xFF)
    OP_96(0x9, 0xFFFF704A, 0x0, 0xFFFEB3F8, 0x1F4, 0x1388)
    SetChrChipByIndex(0x9, 16)
    SetChrSubChip(0x9, 3)
    SetChrChipByIndex(0xA, 5)

    ChrTalk(    #19
        0x9,
        "#205FGaaah!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x80)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #20
        0x8,
        "#216FKyle?!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)
    OP_92(0x8, 0x9, 0x2BC, 0xBB8, 0x0)

    ChrTalk(    #21
        0xA,
        (
            "#194FBwa ha ha, who cares about our\x01",
            "old home?!\x02\x03",

            "With this kind of mira coming in, what\x01",
            "could you possibly want with our old,\x01",
            "worthless land?\x02\x03",

            "Ha! We're gonna go blow all this cash\x01",
            "somewhere near the southern resort\x01",
            "and enjoy the good life for a while!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x9,
        "#201FWhat...did you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xA,
        (
            "#193FAnd once we run out of mira,\x01",
            "we'll just hijack another airship.\x02\x03",

            "This is going to be the future of\x01",
            "the Capua sky bandits!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #24
        0xA,
        "#194F#5SBwa ha ha ha ha ha ha!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 400)

    ChrTalk(    #25
        0x8,
        (
            "#215FDon...what's happened to you...?\x02\x03",

            "#214FWhat in Aidios' name has happened\x01",
            "to you?!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 7)
    SetChrFlags(0x101, 0x80)
    SetChrPos(0x101, -35150, 0, -91730, 0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #26
        0x101,
        (
            "#1PSorry to interrupt...\x02\x03",

            "But could you have your little\x01",
            "family feud later?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_E03():
        OP_6D(-34550, 0, -85900, 1500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_E03)
    SetChrChipByIndex(0x102, 9)
    SetChrChipByIndex(0x104, 11)
    SetChrChipByIndex(0x103, 13)

    def lambda_E2A():
        OP_8C(0xA, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E2A)

    def lambda_E38():
        OP_8C(0x8, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E38)
    ClearChrFlags(0x101, 0x80)

    def lambda_E4B():
        OP_8E(0xFE, 0xFFFF768A, 0x0, 0xFFFEA9B2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E4B)
    Sleep(200)
    SetChrPos(0x103, -35150, 0, -91730, 0)

    def lambda_E7C():
        OP_8E(0xFE, 0xFFFF7B4E, 0x0, 0xFFFEA886, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E7C)
    Sleep(200)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, -35150, 0, -91730, 0)

    def lambda_EB2():
        OP_8E(0xFE, 0xFFFF7112, 0x0, 0xFFFEA750, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EB2)
    Sleep(200)
    SetChrPos(0x104, -35150, 0, -91730, 0)

    def lambda_EE3():
        OP_8E(0xFE, 0xFFFF7644, 0x0, 0xFFFEA412, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EE3)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x104, 0x1)
    WaitChrThread(0x103, 0x1)
    ClearChrFlags(0x102, 0x4)

    ChrTalk(    #27
        0x8,
        "#213FY-You again?!\x02",
    )

    CloseMessageWindow()
    OP_96(0x9, 0xFFFF6D02, 0x0, 0xFFFEB434, 0x12C, 0xBB8)
    SetChrChipByIndex(0x9, 4)
    SetChrSubChip(0x9, 0)

    def lambda_F50():
        OP_8C(0x9, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F50)

    ChrTalk(    #28
        0x9,
        (
            "#201FBracers?!\x02\x03",

            "Wh-Why are you here...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x104,
        (
            "#035FHow can you say something\x01",
            "so heartless...?\x02\x03",

            "Especially after you gave us a\x01",
            "lift here in your own airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x9,
        (
            "#201FI-Impossible... What are you talking\x01",
            "about...?\x02\x03",

            "...It can't be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#006FYou had your airship sitting in front\x01",
            "of the Amberl Tower, right?\x02\x03",

            "We just slipped in when you weren't\x01",
            "looking and hid in the cargo hull.\x02\x03",

            "#001FIn other words, we stole a ride\x01",
            "from a bandit! Ha! Take that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "#214FFor a dimwit, you've really outdone\x01",
            "yourself this time!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #33
        0x101,
        (
            "#509FWh-Who are you calling a dimwit?\x02\x03",

            "Y-You two-faced tomboy!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #34
        0x8,
        (
            "#214FWhat'd you just call me?!\x02\x03",

            "You bimbo! Airhead brute!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#005FJ-Just try and say that again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        (
            "#017FAll right, all right. Enough of the\x01",
            "bickering between you two.\x02\x03",

            "#012FWe've liberated the hostages and\x01",
            "defeated the other members of your\x01",
            "group...\x02\x03",

            "So it looks like all that's left is\x01",
            "you three.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x103,
        (
            "#027FIn accordance with the laws of the Bracer\x01",
            "Guild, you are hereby placed under arrest.\x02\x03",

            "It would be best not to resist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        "#201FMan...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        "#212FCr-crap...\x02",
    )

    CloseMessageWindow()

    def lambda_13B9():
        OP_6D(-34330, 0, -83800, 1000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_13B9)
    Sleep(1000)

    ChrTalk(    #40
        0xA,
        (
            "#193F#6PKyle, Josette...\x02\x03",

            "What is the meaning of this?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        "#203FS-Sorry, Bro...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        "#215FI'm sorry, Don...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        (
            "#193F#6PBwa ha ha! That's okay.\x01",
            "I'll forgive you just this once.\x02\x03",

            "Once I kill them, that'll be that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#005FWhaaat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        (
            "#194F#6PBwa ha ha! What a bunch of fools\x01",
            "you are!\x02\x03",

            "To think with that pitiful number\x01",
            "of people that you could ever\x01",
            "capture Don Capua!\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x4)
    OP_96(0xA, 0xFFFF79C8, 0x3E8, 0xFFFEB9AC, 0x5DC, 0x1388)
    OP_22(0x8E, 0x0, 0x64)
    SetChrChipByIndex(0xA, 6)
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(500)

    def lambda_1598():
        OP_6D(-34220, 0, -85300, 1000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1598)
    Sleep(1000)

    def lambda_15B5():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_15B5)
    Sleep(200)
    OP_22(0x1FA, 0x0, 0x64)
    LoadEffect(0x2, "map\\\\mp019_00.eff")
    SetChrPos(0xC, -35030, 0, -87040, 0)
    PlayEffect(0x2, 0xFF, 0xA, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xC, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_162E():
        OP_96(0xFE, 0xFFFF72AC, 0x0, 0xFFFEA818, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_162E)

    def lambda_164C():
        OP_96(0xFE, 0xFFFF7A5E, 0x0, 0xFFFEA7FA, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_164C)

    def lambda_166A():
        OP_96(0xFE, 0xFFFF6E56, 0x0, 0xFFFEA386, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_166A)

    def lambda_1688():
        OP_96(0xFE, 0xFFFF7C5C, 0x0, 0xFFFEA2DC, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1688)
    Sleep(500)
    LoadEffect(0x1, "map\\\\mp019_01.eff")
    PlayEffect(0x1, 0xFF, 0xFF, -35030, 0, -87040, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6B(3100, 0)
    OP_6B(3000, 80)
    TurnDirection(0x103, 0xA, 0)
    TurnDirection(0x101, 0xA, 0)
    TurnDirection(0x102, 0x9, 0)
    TurnDirection(0x104, 0xA, 0)
    Sleep(600)

    ChrTalk(    #46
        0x101,
        "#504FAhhhhh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x102,
        (
            "#016FLook at how effortlessly he handles\x01",
            "that orbal cannon...!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 225, 0)

    ChrTalk(    #48
        0xA,
        (
            "#195F#6PKyle, Josette!\x01",
            "It's time to hunt some game!\x02\x03",

            "And I like my sport BLOODY.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 0)
    Sleep(100)
    SetChrChipByIndex(0x8, 18)
    Sleep(100)
    SetChrChipByIndex(0x9, 19)
    Sleep(500)
    SetChrChipByIndex(0xA, 20)
    SetChrSubChip(0xA, 0)

    def lambda_1804():
        OP_96(0xFE, 0xFFFF768A, 0x0, 0xFFFEAC5A, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1804)
    Sleep(100)

    def lambda_1827():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1827)
    Sleep(100)

    def lambda_1841():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1841)
    Sleep(200)
    Battle(0x389, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_186E"),
        (SWITCH_DEFAULT, "loc_1871"),
    )


    label("loc_186E")

    OP_B4(0x0)
    Return()

    label("loc_1871")

    EventBegin(0x0)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrChipByIndex(0x8, 3)
    SetChrChipByIndex(0x9, 4)
    SetChrChipByIndex(0xA, 17)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, -36430, 0, -82700, 225)
    SetChrPos(0x9, -38890, 0, -82380, 135)
    SetChrPos(0xA, -37360, 0, -81500, 180)
    SetChrPos(0x101, -38990, 0, -84930, 0)
    SetChrPos(0x102, -38900, 0, -86070, 0)
    SetChrPos(0x104, -37640, 0, -86250, 0)
    SetChrPos(0x103, -37780, 0, -84870, 0)
    OP_6D(-37600, 0, -82870, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    Sleep(1000)

    ChrTalk(    #49
        0x9,
        (
            "#203FThese guys...are tough...\x02\x03",

            "So this is the strength of a\x01",
            "bracer, huh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "#215FCr-Crap...\x01",
            "How can I lose to this girl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#502FAnd that's how it's done.\x01",
            "Have you learned your lesson yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x103,
        (
            "#027FNow that this has been settled,\x01",
            "I'm going to ask that you surrender\x01",
            "nicely.\x02\x03",

            "#021FAny more trouble out of you...and, well,\x01",
            "you know what'll happen, right?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #53
        "\x07\x05Scherazard stroked her whip and smiled at Josette.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #54
        0x8,
        "#216FYikes... N-No, anything but that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        (
            "#203FWhy me...? Why do I have to go\x01",
            "down like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xA,
        "...Umm...\x02",
    )

    CloseMessageWindow()
    OP_6D(-37530, 0, -82040, 1000)
    OP_99(0xA, 0x3, 0x0, 0x258)

    ChrTalk(    #57
        0xA,
        (
            "#197FOw... What's going on?\x02\x03",

            "I hurt all over...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0xA, 5)
    OP_0D()

    ChrTalk(    #58
        0xA,
        (
            "#192FAnd when did I get an orbal cannon...?\x02\x03",

            "What the heck...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 400)

    ChrTalk(    #59
        0x9,
        "#201FBro?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 400)

    ChrTalk(    #60
        0x8,
        "#212FDon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xA,
        (
            "#191FOh, Josette! Are you back from\x01",
            "Rolent already?\x02\x03",

            "If you're back this quickly then\x01",
            "I guess things didn't work out,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        "#213FEh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        (
            "#191FHa ha ha! Don't try and cover it up!\x02\x03",

            "If you've had enough, then how\x01",
            "about leaving the bread-winning\x01",
            "to us men?\x02\x03",

            "We probably won't be able to earn\x01",
            "a whole lot, but be patient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        "#216FD-Don, what are you talking about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "#201FDid you hit your head, Bro?\x02\x03",

            "Josette came back from Rolent\x01",
            "like forever ago.\x02\x03",

            "I went to pick her up right after\x01",
            "we attacked the airliner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "#192FWhat? Attacked an airliner?\x02\x03",

            "What's all this crazy talk?\x02\x03",

            "We'd never do something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        "#201F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        "#213F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#002F(What is this guy talking about?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x102,
        (
            "#012F(I don't think he's trying to cover\x01",
            "his butt... I think he really doesn't\x01",
            "know!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        (
            "#190FCome to think of it...who are these\x01",
            "strangers?\x02\x03",

            "Don't tell me they're new recruits...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x103,
        (
            "#020FSorry to burst your bubble,\x01",
            "but we're not.\x02\x03",

            "We're with the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #73
        0xA,
        "#192F#5SHuh?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #74
        0xA,
        (
            "#192FWhat are a bunch of bracers doing\x01",
            "up here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#007FThis guy's completely lost his\x01",
            "marbles...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x104,
        (
            "#031FHa ha ha. What an interesting\x01",
            "turn of events.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x103,
        (
            "#022FWhether you've forgotten or not,\x01",
            "you're still under arrest.\x02\x03",

            "You're charged with hijacking an airliner,\x01",
            "hostage-taking, demanding a ransom, and\x01",
            "other such offenses.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2300, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #78
        0xA,
        (
            "#192FHijacking an airliner...hostage-taking,\x01",
            "and demanding a ransom?!\x02\x03",

            "Kyle! Josette! T-Tell me that this\x01",
            "is some kind of joke!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        "#215FDon...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        (
            "#204FI think that's my line...\x02\x03",

            "#201FBut thanks to you, Bro...we've got\x01",
            "a chance to escape!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 21)
    OP_8C(0x9, 180, 400)
    Sleep(200)
    OP_99(0x9, 0x4, 0x5, 0x320)
    LoadEffect(0x0, "map\\\\mp004_00.eff")
    SetChrPos(0xC, -38180, -3000, -85370, 0)
    PlayEffect(0x0, 0xFF, 0x9, 250, 900, 330, 0, 0, 0, 1000, 1000, 1000, 0xC, 0, 0, 0, 0)
    SetChrChipByIndex(0x9, 1)
    Sleep(1300)
    OP_22(0x7F, 0x0, 0x64)
    FadeToDark(500, 16777215, -1)
    OP_0D()
    SetChrPos(0x9, -35240, 0, -89190, 0)
    SetChrPos(0x8, -35240, 0, -89190, 0)
    SetChrPos(0xA, -35240, 0, -89190, 0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)

    ChrTalk(    #81
        0x101,
        "#004F#1PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x103,
        "#024F#1POh hell! Not again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xA,
        "#192FH-Hey...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        "#213FKyle?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x9,
        (
            "#201FWe'll talk about this later! Let's\x01",
            "just focus on getting out of here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x104,
        (
            "#034F#5P*cough cough*\x02\x03",

            "I'm...*cough*...never going to *cough*\x01",
            "*cough* get the smell of this out of my\x01",
            "*cough* hair...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x102,
        (
            "#016F#5PLet's hurry and get out of this\x01",
            "room!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_6D(-35986, 0, -121600, 0)
    OP_6F(0x0, 20)
    Sleep(500)
    FadeToBright(1000, 16777215)
    OP_0D()
    OP_43(0x101, 0x1, 0x0, 0x4)
    OP_43(0x102, 0x1, 0x0, 0x5)
    OP_43(0x103, 0x1, 0x0, 0x6)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #88
        0x101,
        "#005FWhich way did they go?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x102,
        (
            "#016FThey went up... They're going to\x01",
            "try and escape in their airship!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #90
        0x101,
        "#580FAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x103,
        (
            "#024F#5PAfter tracking them this far,\x01",
            "we can't let them get away!\x02\x03",

            "We've got to catch them!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #92
        0x101,
        "#002FRight!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(    #93
        0x102,
        "#012FUnderstood!\x02",
    )

    CloseMessageWindow()
    OP_43(0x104, 0x1, 0x0, 0x7)
    WaitChrThread(0x104, 0x1)

    ChrTalk(    #94
        0x104,
        (
            "#034F*cough cough*\x01",
            "I-I made it out alive...\x02\x03",

            "Oh, what a tragedy this has become!\x01",
            "My delicate nasal cavity...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2721():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2721)

    def lambda_272F():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_272F)
    TurnDirection(0x101, 0x104, 400)
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #95
        0x101,
        (
            "#005FHey, Olivier! You'd better hurry or\x01",
            "we're going to leave you behind!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #96
        0x104,
        "#036FAh! W-Wait for me!\x02",
    )

    CloseMessageWindow()
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0x5DC)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27EF")
    OP_8E(0x104, 0xFFFF7360, 0x0, 0xFFFE22BC, 0xBB8, 0x0)

    label("loc_27EF")

    OP_A2(0x358)
    OP_28(0x39, 0x1, 0x40)
    OP_28(0x39, 0x1, 0x80)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    OP_70(0x0, 0x0)
    OP_71(0x0, 0x10)
    OP_64(0x0, 0x1)
    OP_21()
    OP_1E()
    Jump("loc_281A")

    label("loc_281A")

    Return()

    # Function_3_2DB end

    def Function_4_281B(): pass

    label("Function_4_281B")

    SetChrPos(0xFE, -36050, 0, -119700, 0)
    OP_8E(0xFE, 0xFFFF7266, 0x0, 0xFFFE21F4, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF6EB0, 0x0, 0xFFFE1C72, 0x1388, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(200)
    OP_8C(0xFE, 265, 400)
    Sleep(200)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_4_281B end

    def Function_5_2874(): pass

    label("Function_5_2874")

    Sleep(800)
    SetChrPos(0xFE, -36050, 0, -119700, 0)
    OP_8E(0xFE, 0xFFFF7266, 0x0, 0xFFFE21F4, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF7586, 0x0, 0xFFFE1DBC, 0x1388, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_5_2874 end

    def Function_6_28BA(): pass

    label("Function_6_28BA")

    Sleep(1600)
    SetChrPos(0xFE, -36050, 0, -119700, 0)
    OP_8E(0xFE, 0xFFFF7266, 0x0, 0xFFFE21F4, 0x1388, 0x0)
    Return()

    # Function_6_28BA end

    def Function_7_28E5(): pass

    label("Function_7_28E5")

    SetChrPos(0xFE, -36050, 0, -119700, 0)
    OP_8E(0xFE, 0xFFFF7388, 0x0, 0xFFFE27A8, 0x7D0, 0x0)
    Return()

    # Function_7_28E5 end

    def Function_8_290B(): pass

    label("Function_8_290B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A86")
    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #97
        "\x07\x05There is a rock wall at the end of the passage.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #98
        0x101,
        "#505FIs this a dead end?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x102,
        (
            "#012FNo...it looks like there's something\x01",
            "here.\x02\x03",

            "Shall we try pushing on it?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Push on the rock wall]\x01",      # 0
            "[Leave it alone]\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A59"),
        (1, "loc_2A68"),
        (SWITCH_DEFAULT, "loc_2A86"),
    )


    label("loc_2A59")

    OP_A2(0x3FB)
    NewScene("ED6_DT01/C1401   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2A86")

    label("loc_2A68")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_2A86")

    label("loc_2A86")

    Return()

    # Function_8_290B end

    def Function_9_2A87(): pass

    label("Function_9_2A87")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B82")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_2B01")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #100
        "\x07\x00Found \x07\x02Reviving Balm\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x384)
    Jump("loc_2B7F")

    label("loc_2B01")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #101
        (
            "\x07\x00Found \x07\x02Reviving Balm\x07\x00 in chest.\x01",
            "Inventory full so gave up \x07\x02Reviving Balm\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_2B7F")

    Jump("loc_2C04")

    label("loc_2B82")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #102
        (
            "\x07\x05The treasure chest is offended that you have returned.\x01",
            "Was the first time not good enough for you?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0xF)

    label("loc_2C04")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_2A87 end

    SaveToFile()

Try(main)
