from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4221   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4221.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Revol',                                # 9
        'Scherazard',                           # 10
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


    AddCharChip(
        'ED6_DT26/CH20260 ._CH',             # 00
        'ED6_DT26/CH20234 ._CH',             # 01
        'ED6_DT07/CH00020 ._CH',             # 02
        'ED6_DT26/CH20261 ._CH',             # 03
        'ED6_DT07/CH01270 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT26/CH20260P._CP',             # 00
        'ED6_DT26/CH20234P._CP',             # 01
        'ED6_DT07/CH00020P._CP',             # 02
        'ED6_DT26/CH20261P._CP',             # 03
        'ED6_DT07/CH01270P._CP',             # 04
    )

    DeclNpc(
        X                   = 143260,
        Z                   = 0,
        Y                   = 3310,
        Direction           = 356,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_112",          # 00, 0
        "Function_1_11F",          # 01, 1
        "Function_2_19D",          # 02, 2
        "Function_3_422",          # 03, 3
        "Function_4_1081",         # 04, 4
        "Function_5_1268",         # 05, 5
    )


    def Function_0_112(): pass

    label("Function_0_112")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E")
    Event(0, 3)

    label("loc_11E")

    Return()

    # Function_0_112 end

    def Function_1_11F(): pass

    label("Function_1_11F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B")
    OP_B1("t4221_y")
    Jump("loc_144")

    label("loc_13B")

    OP_B1("t4221_n")

    label("loc_144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_159")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_181")
    OP_22(0x87, 0x1, 0x1E)
    OP_22(0xAE, 0x1, 0x1E)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    OP_77(0xFF, 0xBF, 0xB7, 0x0, 0x0)

    label("loc_181")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 6)), scpexpr(EXPR_END)), "loc_19C")
    OP_1B(0x1, 0x0, 0x4)
    OP_1B(0x2, 0x0, 0x4)
    OP_1B(0x3, 0x0, 0x5)
    OP_1B(0x4, 0x0, 0x5)

    label("loc_19C")

    Return()

    # Function_1_11F end

    def Function_2_19D(): pass

    label("Function_2_19D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_208")

    ChrTalk(    #0
        0xFE,
        (
            "I-I heard some screaming and\x01",
            "yelling outside the door...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Wh-What on earth happened?\x02",
    )

    CloseMessageWindow()
    Jump("loc_41E")

    label("loc_208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2B9")

    ChrTalk(    #2
        0xFE,
        (
            "Lady Klaudia will be residing at\x01",
            "the castle for some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "And I'm happier for it! Her mere\x01",
            "presence alone does plenty to\x01",
            "brighten the halls of this castle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41E")

    label("loc_2B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3A3")

    ChrTalk(    #4
        0xFE,
        "Kanone has been captured?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "With her out of the picture, that's\x01",
            "finally the end of the Intelligence\x01",
            "Division, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "I'm sure that's a weight off Julia's\x01",
            "shoulders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "Justice wins in the end, as it must.\x02",
    )

    CloseMessageWindow()
    Jump("loc_41E")

    label("loc_3A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_41E")

    ChrTalk(    #8
        0xFE,
        (
            "Why, Your Highness Klaudia,\x01",
            "welcome home!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Would you like something? I would\x01",
            "be happy to prepare some tea!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41E")

    TalkEnd(0xFE)
    Return()

    # Function_2_19D end

    def Function_3_422(): pass

    label("Function_3_422")

    OP_35(0x0, 0x0)
    OP_BB(0x0, 0x6, 0xE7)
    OP_31(0x0, 0xFE, 0x0)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x1)
    OP_6D(79650, 350, 55020, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 85060, 500, 60710, 180)
    OP_72(0x5, 0x4)
    OP_72(0x5, 0x20)
    OP_72(0x5, 0x8)
    OP_6F(0x5, 5)
    OP_71(0x6, 0x4)
    OP_71(0x7, 0x4)
    FadeToBright(2000, 0)

    def lambda_4D9():
        OP_6D(85310, 350, 60680, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D9)

    def lambda_4F1():
        OP_67(0, 8000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F1)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    NpcTalk(    #10
        0x101,
        "Estelle",
        "#6P#007F...Mrrrmrmrr... So...bright...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 16)
    Sleep(200)
    SetChrSubChip(0x101, 0)
    Sleep(200)
    SetChrSubChip(0x101, 16)
    Sleep(200)
    SetChrSubChip(0x101, 0)
    Sleep(1000)

    def lambda_575():
        OP_99(0x101, 0x0, 0x8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_575)
    Sleep(300)
    OP_71(0x5, 0x8)
    OP_6F(0x5, 5)
    OP_B0(0x5, 0x28)
    OP_70(0x5, 0x3B)
    Sleep(1500)

    def lambda_5A6():
        OP_99(0xFE, 0x8, 0xC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5A6)

    ChrTalk(    #11 op#5
        0x101,
        "#504F*yaaaaaaaaaawn*\x05\x02",
    )

    OP_9E(0x101, 0xF, 0x0, 0x7D0, 0xFA0)

    def lambda_5E3():
        OP_99(0xFE, 0xC, 0xE, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E3)
    Sleep(1000)
    SetChrSubChip(0x101, 14)
    Sleep(200)
    SetChrSubChip(0x101, 17)
    Sleep(200)
    SetChrSubChip(0x101, 18)
    Sleep(500)

    ChrTalk(    #12
        0x101,
        (
            "#501FAaaaahhhhh, that felt good.\x01",
            "I haven't slept like that since...\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x12, 0x15, 0x3E8)
    Sleep(500)
    OP_99(0x101, 0x15, 0x12, 0x3E8)
    SetChrSubChip(0x101, 23)
    Sleep(1000)
    SetChrSubChip(0x101, 18)
    Sleep(500)

    ChrTalk(    #13
        0x101,
        (
            "#004FWha...?\x02\x03",

            "...\x02\x03",

            "#505FOh, right.\x01",
            "We stayed in the castle last night.\x02\x03",

            "Joshua and I were out enjoying the\x01",
            "celebrations, then...we had some\x01",
            "ice cream on the way home...\x02\x03",

            "Then we all went to the dinner party...\x02\x03",

            "And then...\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_AD(0x2400B7, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #14
        0x101,
        (
            "#580F...\x02\x03",

            "N-N-N-No...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0)
    Sleep(100)
    OP_22(0x23B, 0x0, 0x3C)
    SetChrChipByIndex(0x101, 65535)
    OP_8C(0x101, 270, 0)

    def lambda_7EB():
        OP_96(0xFE, 0x1462C, 0x0, 0xECF4, 0x258, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7EB)
    WaitChrThread(0x101, 0x1)
    ClearChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x1)

    def lambda_818():
        OP_6D(83470, 0, 60260, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_818)

    def lambda_830():
        OP_67(0, 8000, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_830)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_8C(0x101, 180, 1000)
    Sleep(1000)
    OP_8C(0x101, 90, 1000)
    Sleep(1000)
    OP_8C(0x101, 270, 1000)
    Sleep(1000)
    OP_8C(0x101, 180, 1000)
    Sleep(1000)

    ChrTalk(    #15
        0x101,
        (
            "#587FThis is... This is Joshua's room.\x02\x03",

            "But I was staying in the same room\x01",
            "as Schera.\x02\x03",

            "Was... Was all that a dream?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(100)
    Fade(500)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 1)
    SetChrSubChip(0x101, 5)
    OP_0D()
    Sleep(500)

    ChrTalk(    #16
        0x101,
        (
            "#580FWhat...?\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #17
        0x101,
        "#005F#4SJOSHUAAAAAA!!!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()

    def lambda_995():
        OP_8E(0x101, 0x137AE, 0x0, 0xBDA6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_995)
    Sleep(100)

    def lambda_9B5():
        OP_6D(80350, 0, 51510, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B5)

    def lambda_9CD():
        OP_67(0, 8000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9CD)
    Sleep(1500)

    def lambda_9EA():
        OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0xFA)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9EA)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    ClearMapFlags(0x1)
    Fade(1000)
    OP_6D(79000, 0, 7200, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x101, 79210, 0, 9810, 180)
    SetChrPos(0x9, 67190, 0, 9780, 180)
    ClearChrFlags(0x9, 0x80)

    def lambda_A89():
        OP_8E(0x101, 0x13452, 0x0, 0x820, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A89)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3C)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    OP_8C(0x101, 90, 1000)
    Sleep(1000)
    OP_8C(0x101, 270, 1000)
    Sleep(1000)
    OP_8C(0x101, 90, 1000)
    OP_69(0x9, 0x7D0)

    def lambda_AE3():

        label("loc_AE3")

        OP_69(0x9, 0x0)
        OP_48()
        Jump("loc_AE3")

    QueueWorkItem2(0x9, 3, lambda_AE3)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3C)
    OP_73(0x0)
    OP_8E(0x9, 0x103BA, 0x0, 0x6F4, 0x7D0, 0x0)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x9, 0x101, 500)
    Sleep(500)
    OP_44(0x9, 0x3)

    def lambda_B45():
        OP_6D(76750, 0, 2160, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B45)

    def lambda_B5D():
        OP_67(0, 8000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B5D)

    def lambda_B75():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B75)

    def lambda_B85():
        OP_6E(262, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B85)
    OP_8E(0x9, 0x12426, 0x0, 0x834, 0x7D0, 0x0)

    ChrTalk(    #18
        0x9,
        (
            "#3P#020FA-ha! Good morning, sleepyhead.\x01",
            "You took your sweet time waking up.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(    #19
        0x101,
        "#587F#4PSch-Schera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x9,
        (
            "#3P#021FReally, warn me the next time you\x01",
            "aren't going to come back for the\x01",
            "evening. I was getting a bit worried!\x02\x03",

            "Althoooough, it looks to me like you\x01",
            "and Joshua managed to talk about\x01",
            "QUITE a bi--\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x101, 0x9, 0x7D0, 0x1388, 0x0)

    ChrTalk(    #21
        0x101,
        "#005F#4PSchera! Where's Joshua?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x9,
        "#3P#023FWhat? Where's...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#005F#4PI'm looking for Joshua!\x02\x03",

            "Schera, have you seen him?!\x01",
            "This is important!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x9,
        (
            "#3P#023FI...haven't seen him yet this morning,\x01",
            "no.\x02\x03",

            "But weren't you tired yesterday\x01",
            "and stayed over in his room?\x02\x03",

            "He wasn't there when you woke up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#580F#4PWh-Wha...?!\x02\x03",

            "I-I... What?\x01",
            "Who did you hear that from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x9,
        "#3P#023FUm, from Cassius, but why does that--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#580F#4PFrom Dad?!\x02\x03",

            "#005FO-Okay! Where's Dad, then?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        (
            "#3P#022FWell, last I saw, he was heading up\x01",
            "toward the Garden Terrace, but now wh--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#002F#4PThe Garden Terrace! Okaythanksbye!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 800)

    def lambda_F68():
        OP_6D(78660, 0, 2110, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_F68)

    def lambda_F80():
        OP_8E(0xFE, 0x16512, 0x0, 0x938, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F80)
    Sleep(500)

    ChrTalk(    #30
        0x9,
        "#023FAh, wait, Estelle! WAIT A...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    OP_69(0x9, 0x5DC)

    ChrTalk(    #31
        0x9,
        "#022FWhat on earth has gotten into her...?\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_100D():
        OP_6E(240, 1000)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_100D)
    Fade(1000)
    SetChrChipByIndex(0x9, 3)
    OP_0D()
    Sleep(500)

    ChrTalk(    #32
        0x9,
        (
            "#022F...\x02\x03",

            "#522FOh. Oh, Goddess.\x01",
            "The 'Lovers.' Reversed...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1002)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_422 end

    def Function_4_1081(): pass

    label("Function_4_1081")

    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_10A3"),
        (1, "loc_10E9"),
        (2, "loc_112A"),
        (5, "loc_1176"),
        (7, "loc_11B4"),
        (6, "loc_11FC"),
        (SWITCH_DEFAULT, "loc_1247"),
    )


    label("loc_10A3")


    ChrTalk(    #33
        0x101,
        (
            "#1002FNo, not this way. We need to hurry\x01",
            "to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1247")

    label("loc_10E9")


    ChrTalk(    #34
        0x102,
        (
            "#1042FNo, not this way. Let's hurry to the\x01",
            "queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1247")

    label("loc_112A")


    ChrTalk(    #35
        0x103,
        (
            "#022FWe have no business this way.\x01",
            "Let's hurry to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1247")

    label("loc_1176")


    ChrTalk(    #36
        0x106,
        (
            "#057FCan't waste time.\x01",
            "Let's get to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1247")

    label("loc_11B4")


    ChrTalk(    #37
        0x108,
        (
            "#072FNo time for side trips.\x01",
            "We must hurry to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1247")

    label("loc_11FC")


    ChrTalk(    #38
        0x107,
        (
            "#062FUm, wait, not this way. We need to\x01",
            "hurry to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1247")

    label("loc_1247")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_4_1081 end

    def Function_5_1268(): pass

    label("Function_5_1268")

    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_128A"),
        (1, "loc_12D0"),
        (2, "loc_1311"),
        (5, "loc_135D"),
        (7, "loc_139B"),
        (6, "loc_13E3"),
        (SWITCH_DEFAULT, "loc_142E"),
    )


    label("loc_128A")


    ChrTalk(    #39
        0x101,
        (
            "#1002FNo, not this way. We need to hurry\x01",
            "to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142E")

    label("loc_12D0")


    ChrTalk(    #40
        0x102,
        (
            "#1042FNo, not this way. Let's hurry to the\x01",
            "queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142E")

    label("loc_1311")


    ChrTalk(    #41
        0x103,
        (
            "#022FWe have no business this way.\x01",
            "Let's hurry to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142E")

    label("loc_135D")


    ChrTalk(    #42
        0x106,
        (
            "#057FCan't waste time.\x01",
            "Let's get to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142E")

    label("loc_139B")


    ChrTalk(    #43
        0x108,
        (
            "#072FNo time for side trips.\x01",
            "We must hurry to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142E")

    label("loc_13E3")


    ChrTalk(    #44
        0x107,
        (
            "#062FUm, wait, not this way. We need to\x01",
            "hurry to the queen's room!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142E")

    label("loc_142E")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_5_1268 end

    SaveToFile()

Try(main)
