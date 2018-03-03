from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4152   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4152.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        'Man in Black',                         # 9
        'Man in Black',                         # 10
        'Target Camera',                        # 11
        'Grancel - North Block',                # 12
        'Grancel - South Block',                # 13
        'Grancel - Port',                       # 14
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01680 ._CH',             # 01
        'ED6_DT27/CH03460 ._CH',             # 02
        'ED6_DT26/CH20608 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01680P._CP',             # 01
        'ED6_DT27/CH03460P._CP',             # 02
        'ED6_DT26/CH20608P._CP',             # 03
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

    DeclNpc(
        X                   = -39960,
        Z                   = 0,
        Y                   = 43920,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -7520,
        Z                   = 300,
        Y                   = -20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -117000,
        Z                   = 0,
        Y                   = -4090,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -63040,
        Y                   = -3750,
        Z                   = -33480,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 16,
    )

    DeclEvent(
        X                   = -63390,
        Y                   = -3750,
        Z                   = -24940,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = -78840,
        Y                   = 1250,
        Z                   = 12430,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 18,
    )


    ScpFunction(
        "Function_0_1EA",          # 00, 0
        "Function_1_24C",          # 01, 1
        "Function_2_26B",          # 02, 2
        "Function_3_28F",          # 03, 3
        "Function_4_314",          # 04, 4
        "Function_5_3A1",          # 05, 5
        "Function_6_1C4C",         # 06, 6
        "Function_7_1C68",         # 07, 7
        "Function_8_1CC4",         # 08, 8
        "Function_9_1CF7",         # 09, 9
        "Function_10_1D6C",        # 0A, 10
        "Function_11_1DA1",        # 0B, 11
        "Function_12_1DD8",        # 0C, 12
        "Function_13_1FA0",        # 0D, 13
        "Function_14_1FE1",        # 0E, 14
        "Function_15_2022",        # 0F, 15
        "Function_16_2643",        # 10, 16
        "Function_17_2647",        # 11, 17
        "Function_18_264B",        # 12, 18
        "Function_19_264F",        # 13, 19
    )


    def Function_0_1EA(): pass

    label("Function_0_1EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_215")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 15)
    Jump("loc_22F")

    label("loc_215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22F")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 12)

    label("loc_22F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_24B")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 5)

    label("loc_24B")

    Return()

    # Function_0_1EA end

    def Function_1_24C(): pass

    label("Function_1_24C")

    OP_16(0x2, 0xFA0, 0xFFFD2D58, 0xFFFE0048, 0x23005D)
    OP_71(0x100C, 0x0)
    ExitThread()
    OP_72(0x100A, 0x0)
    ExitThread()
    Return()

    # Function_1_24C end

    def Function_2_26B(): pass

    label("Function_2_26B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28E")
    OP_8D(0xFE, -83110, 1920, -74690, -5430, 3000)
    Jump("Function_2_26B")

    label("loc_28E")

    Return()

    # Function_2_26B end

    def Function_3_28F(): pass

    label("Function_3_28F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_313")
    OP_8E(0xFE, 0xFFFF63CA, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFF291E, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFF259A, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    Jump("Function_3_28F")

    label("loc_313")

    Return()

    # Function_3_28F end

    def Function_4_314(): pass

    label("Function_4_314")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A0")
    OP_8E(0xFE, 0xFFFED716, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFECB72, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFEC014, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFECB72, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    Jump("Function_4_314")

    label("loc_3A0")

    Return()

    # Function_4_314 end

    def Function_5_3A1(): pass

    label("Function_5_3A1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -78640, 1750, 14010, 180)
    SetChrPos(0x10F, -78960, 1750, 14190, 180)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-71540, 9350, 9960, 0)
    OP_67(0, 7060, -10000, 0)
    OP_6B(4600, 0)
    OP_6C(309000, 0)
    OP_6E(310, 0)

    def lambda_428():
        OP_6D(-74440, 8750, 4160, 5500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_428)

    def lambda_440():
        OP_67(0, 6730, -10000, 5500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_440)

    def lambda_458():
        OP_6B(4570, 5500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_458)

    def lambda_468():
        OP_6C(333000, 5500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_468)

    def lambda_478():
        OP_6E(303, 5500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_478)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x1)
    Sleep(500)
    Fade(1000)
    OP_6D(-79260, 1750, 13830, 0)
    OP_67(0, 6190, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(332000, 0)
    OP_6E(323, 0)

    def lambda_4DE():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_4DE)
    OP_0D()
    Sleep(500)
    OP_72(0x100C, 0x0)
    ExitThread()
    OP_72(0x200C, 0x0)
    ExitThread()
    OP_6F(0xC, 0)
    OP_70(0xC, 0x3B)
    OP_73(0xC)
    OP_43(0x109, 0x0, 0x0, 0x8)
    Sleep(800)
    OP_43(0x10F, 0x0, 0x0, 0x9)
    Sleep(1000)

    def lambda_529():
        OP_6D(-80200, 0, 1610, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_529)

    def lambda_541():
        OP_67(0, 5590, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_541)

    def lambda_559():
        OP_6B(2690, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_559)

    def lambda_569():
        OP_6C(315000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_569)

    def lambda_579():
        OP_6E(295, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_579)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x10F, 0x3)

    ChrTalk(    #0
        0x109,
        (
            "#1068FWhew... I thought we were never gonna escape.\x02\x03",

            "Erika sure doesn't know when to quit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10F,
        "#1440F#5P...That's a kind way of putting it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1078FI couldn't believe what I was hearing right at the\x01",
            "end, though.\x02\x03",

            "Just as I thought she'd maxed out her crazy talk\x01",
            "to spew, she goes and shouts, 'Well, if you're\x01",
            "going to be taking THAT, then I'll be taking HER!'\x02\x03",

            "#1077FHaha... I thought Anelace was a one-of-a-kind\x01",
            "cuteness freak, but she might actually have some\x01",
            "stiff competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10F,
        "#1444F#5PAnelace?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        (
            "#1078FOh, sorry. She's a girl I met while I was here\x01",
            "last time.\x02\x03",

            "She's a bracer...errr...about your age, I think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10F,
        "#1446F#5P...Oh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        (
            "#1062FHaha... Uh...\x01",
            "#40W...\x02\x03",

            "#1068F#20WUmm... Ries?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10F,
        "#1440F#5PYes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x109,
        (
            "#1840FYou're not...mad at me, are you?\x02\x03",

            "For not keeping in touch with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10F,
        "#1446F#5PFather Graham.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x109,
        "#1064F#3SY-Yes?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10F,
        (
            "#1446F#5PFive years is a long time.\x02\x03",

            "Just as you have changed and progressed in rank \x01",
            "significantly during those years, so have I.\x02\x03",

            "#1443FThe Ries Argent standing before you is a squire of\x01",
            "the Gralsritter--not the girl you once knew.\x02\x03",

            "I am here to serve and to protect you. Nothing more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x109,
        "#1063FCome on, Ries...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10F,
        (
            "#1446F#5PYou need not concern yourself with how I feel.\x02\x03",

            "If you don't treat me as a subordinate, then there\x01",
            "is little reason for me to be here serving you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x109,
        "#1067F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10F,
        (
            "#1448F#5PAnd with that talk out of the way, we need to board\x01",
            "the last international liner out of Grancel, don't we?\x02\x03",

            "We should start making our way to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_B98():
        OP_6D(-76280, 0, 180, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B98)

    def lambda_BB0():
        OP_67(0, 6380, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BB0)

    def lambda_BC8():
        OP_6B(2390, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_BC8)

    def lambda_BD8():
        OP_6C(69000, 2500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_BD8)

    def lambda_BE8():
        OP_6E(326, 2500)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_BE8)

    def lambda_BF8():

        label("loc_BF8")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_BF8")

    QueueWorkItem2(0x109, 0, lambda_BF8)
    OP_43(0x10F, 0x0, 0x0, 0xA)
    Sleep(300)
    Sleep(800)

    ChrTalk(    #16 op#A op#5
        0x109,
        "#1079F#6P#12AW-Wait a sec...\x05\x02",
    )

    WaitChrThread(0x10F, 0x0)
    OP_44(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    OP_22(0x160, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    OP_63(0x10F)
    Sleep(500)

    ChrTalk(    #17
        0x109,
        "#1079F#6PWas that your...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10F,
        (
            "#1440F#5P...\x02\x03",

            "#1446FIt was a figment of your imagination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x109,
        "#1064F#6PHuh?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10F, 315, 400)
    Sleep(300)

    ChrTalk(    #20
        0x10F,
        (
            "#1447F#2PYou seem to be tired, Father Graham.\x02\x03",

            "I see no other explanation as to why you're hearing\x01",
            "sounds that clearly don't exist in reality.\x02\x03",

            "#1448FI think you ought to try and have some rest when\x01",
            "we reach the airsh--\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x160, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x10F)
    Sleep(500)

    ChrTalk(    #21
        0x10F,
        (
            "#1800F#2P...As I was saying, I think you ought to try and have\x01",
            "some rest.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x109, 0x0, 0x0, 0x7)

    ChrTalk(    #22
        0x109,
        "#1840F#6PPffft...\x02",
    )

    CloseMessageWindow()
    OP_44(0x109, 0x0)
    OP_43(0x109, 0x0, 0x0, 0x6)
    Sleep(500)

    ChrTalk(    #23
        0x109,
        (
            "#1061F#6P#3SHahaha! Don't even TRY and tell me that one\x01",
            "was my imagination!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    CloseMessageWindow()
    Sleep(100)
    WaitChrThread(0x109, 0x0)
    Fade(500)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    ClearChrFlags(0x109, 0x2)
    OP_0D()
    Sleep(200)

    ChrTalk(    #24
        0x109,
        (
            "#1066F#6P#2SMan, for a second I thought you'd changed,\x01",
            "but you haven't. Not one bit!\x02\x03",

            "You're still the same perpetually-hungry Ries\x01",
            "I remember.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x10F, 0x2)
    SetChrChipByIndex(0x10F, 3)
    SetChrSubChip(0x10F, 8)
    OP_99(0x10F, 0x8, 0xC, 0x5DC)
    OP_62(0x10F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_99(0x10F, 0xA, 0xC, 0x5DC)
    Sleep(500)

    ChrTalk(    #25
        0x10F,
        (
            "#1445F#2PTh-This is just a simple physiological phenomenon.\x02\x03",

            "My lack of control is proof that I still have plenty\x01",
            "of training ahead of me.\x02\x03",

            "I can only apologize for my own inability.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        (
            "#1840F#6PHaha... Since when did not being able to turn\x01",
            "off your stomach become something you have\x01",
            "to apologize for?\x02\x03",

            "#1071FBesides, I wouldn't have you any other way.\x02\x03",

            "You're forever gonna be the girl who was\x01",
            "always getting caught sneaking into the\x01",
            "kitchen and trying to stuff her face to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x10F, 0xC, 0xD, 0x5DC)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    ClearChrFlags(0x10F, 0x2)

    ChrTalk(    #27
        0x10F,
        "#1800F#2P...I'll be going on ahead!\x02",
    )

    CloseMessageWindow()

    def lambda_1217():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1217)
    Sleep(300)

    def lambda_122A():
        OP_6D(-74700, 0, -1800, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_122A)

    def lambda_1242():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_1242)
    OP_43(0x109, 0x0, 0x0, 0xB)

    ChrTalk(    #28 op#A op#5
        0x109,
        "#1078F#2P#15AHey! Wait a sec!\x05\x02",
    )

    WaitChrThread(0x10F, 0x0)
    Sleep(300)
    OP_8F(0x10F, 0xFFFED7D4, 0x0, 0xFFFFF7CC, 0x3E8, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x1)
    Sleep(500)

    ChrTalk(    #29
        0x10F,
        "#1443F#6PYou're in my way. Please move.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x109,
        (
            "#1840F#2PI'm sorry, okay? I didn't mean to push my luck.\x02\x03",

            "I just got carried away thinking of old times,\x01",
            "that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10F,
        (
            "#1446F#6PYou have no reason to apologize.\x02\x03",

            "Nor do I see any point in you doing so, because\x01",
            "there are few things in this world that carry less\x01",
            "weight than one of your apologies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x109,
        (
            "#1066F#2PDamn. Finally biting back, huh?\x02\x03",

            "Well, while I've only got a 50-50 chance of you\x01",
            "listening to me...can you knock if off with the\x01",
            "Father Graham? Or even 'Father,' for that matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10F,
        "#1802F#6P...For what reason?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x109,
        (
            "#1840F#2PI don't know if you're doing it because you feel\x01",
            "like you have to or because you want to act all\x01",
            "distant...\x02\x03",

            "...but there's no way I can get used to it. Like,\x01",
            "ever. It weirds me out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10F,
        "#1445F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x109,
        (
            "#1840F#2PSo...please?\x02\x03",

            "Call me Kevin. Same as you always did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10F,
        "#1446F#6PWhat if I refuse?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x109,
        (
            "#1075F#2PThen I'll beg you until you change your mind.\x02\x03",

            "#1060FI'll get down on my knees if I have to!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10F,
        "#1445F#6P...You certainly would.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x109,
        (
            "#1066F#2PWell, you know what they say: you can't teach an\x01",
            "old dog new tricks.\x02\x03",

            "I know it's been a while since, but I'm way too set\x01",
            "in my ways now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10F,
        (
            "#1802F#6P...\x02\x03",

            "#1445F#40W...the one...\x01",
            "...left me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x109,
        "#1079F#2PSorry? Didn't quite catch that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10F,
        (
            "#1446F#6P...It was nothing.\x02\x03",

            "#1443FStill, I can't very well refuse an order\x01",
            "from my superior, so--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x109,
        (
            "#1071F#2POhhh, no. You're not playing that game.\x01",
            "It's not an order--it's a favor.\x02\x03",

            "#1062FVeeery important distinction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10F,
        (
            "#1441F#6PBlech...\x02\x03",

            "#1446F#40W...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #46
        0x10F,
        "#1801F#6PYou're so selfish, Kevin.\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #47
        0x109,
        (
            "#1840F#2P...!\x02\x03",

            "#1066FHeh... Theeere we go! That's what I wanted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10F,
        (
            "#1800F#6PBut just so we're clear.\x02\x03",

            "Even if I've changed how I address you,\x01",
            "the fact that I'm your subordinate hasn't\x01",
            "changed in the slightest.\x02\x03",

            "#1443FDon't forget that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x109,
        (
            "#1075F#2PYeah, I know...\x02\x03",

            "#1840FWe can talk like we used to, but there's no way to\x01",
            "turn back the clock to the way things used to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10F,
        "#1445F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x109,
        (
            "#1075F#2POh, and one more thing...\x02\x03",

            "#1060FWe've still got some time until the last airship leaves,\x01",
            "so how about we head over to the department store\x01",
            "in the east block?\x02\x03",

            "We can grab you something you can eat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10F,
        (
            "#1442F#6PI like the sound of that.\x02\x03",

            "#1447FI propose buying all the bread they have left.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #53
        0x109,
        "#1068F#2PI didn't know you were THAT hungry...\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_1C1E():
        OP_6B(2000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_1C1E)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4151   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_5_3A1 end

    def Function_6_1C4C(): pass

    label("Function_6_1C4C")

    OP_99(0x109, 0x3, 0x5, 0x5DC)
    OP_99(0x109, 0x3, 0x5, 0x5DC)
    OP_99(0x109, 0x3, 0x5, 0x5DC)
    Return()

    # Function_6_1C4C end

    def Function_7_1C68(): pass

    label("Function_7_1C68")

    SetChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 3)
    SetChrSubChip(0x109, 0)

    label("loc_1C77")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CC3")
    OP_99(0x109, 0x0, 0x2, 0x7D0)
    OP_99(0x109, 0x0, 0x2, 0x7D0)
    OP_99(0x109, 0x0, 0x2, 0x7D0)
    Sleep(1500)
    OP_99(0x109, 0x0, 0x2, 0x7D0)
    OP_99(0x109, 0x0, 0x2, 0x7D0)
    OP_99(0x109, 0x0, 0x2, 0x7D0)
    Sleep(2000)
    Jump("loc_1C77")

    label("loc_1CC3")

    Return()

    # Function_7_1C68 end

    def Function_8_1CC4(): pass

    label("Function_8_1CC4")


    def lambda_1CCA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1CCA)
    OP_8E(0xFE, 0xFFFECEB0, 0x0, 0x1E0, 0x7D0, 0x0)
    Sleep(100)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_8_1CC4 end

    def Function_9_1CF7(): pass

    label("Function_9_1CF7")


    def lambda_1CFD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1CFD)
    OP_8F(0xFE, 0xFFFECB86, 0x6D6, 0x2FB2, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(100)
    OP_6F(0xC, 59)
    OP_70(0xC, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(100)
    OP_8F(0xFE, 0xFFFEC726, 0x0, 0x19A, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_9_1CF7 end

    def Function_10_1D6C(): pass

    label("Function_10_1D6C")

    OP_8C(0xFE, 135, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFECC9E, 0x0, 0xFFFFFE48, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFED522, 0x0, 0xFFFFFC90, 0x7D0, 0x0)
    Return()

    # Function_10_1D6C end

    def Function_11_1DA1(): pass

    label("Function_11_1DA1")

    OP_8C(0xFE, 90, 600)
    OP_8E(0xFE, 0xFFFED40A, 0x0, 0xFFFFF54C, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFEDD4C, 0x0, 0xFFFFF736, 0x1388, 0x0)
    OP_8C(0xFE, 270, 600)
    Return()

    # Function_11_1DA1 end

    def Function_12_1DD8(): pass

    label("Function_12_1DD8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_71(0x408, 0x0)
    ExitThread()
    OP_72(0x411, 0x0)
    ExitThread()
    OP_6D(-74240, -3500, -14080, 0)
    OP_67(0, 5960, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(310000, 0)
    OP_6E(320, 0)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x151, 0x4)
    SetChrPos(0x103, -73100, -3500, -15300, 0)
    SetChrPos(0x151, -72100, -3500, -15300, 0)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    SetChrPos(0x10, -57040, -3500, -17320, 270)
    SetChrPos(0x11, -73800, -3500, -23360, 0)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_1E9D():
        OP_8E(0xFE, 0xFFFEF1B0, 0xFFFFF254, 0xFFFFBC58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1E9D)
    Sleep(500)
    OP_43(0x11, 0x3, 0x0, 0xD)
    Sleep(2000)
    OP_62(0x151, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x11, 0x1)
    Sleep(300)
    OP_62(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)

    def lambda_1F2A():
        OP_8C(0xFE, 90, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1F2A)
    Sleep(100)

    def lambda_1F3D():
        OP_8C(0xFE, 270, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1F3D)
    Sleep(100)

    def lambda_1F50():
        OP_8E(0xFE, 0xFFFF2CE8, 0xFFFFF254, 0xFFFFBC58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1F50)
    Sleep(100)
    OP_43(0x11, 0x3, 0x0, 0xE)
    Sleep(3000)

    def lambda_1F7C():
        OP_6B(2820, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1F7C)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/T4143   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1DD8 end

    def Function_13_1FA0(): pass

    label("Function_13_1FA0")


    def lambda_1FA6():
        OP_8E(0xFE, 0xFFFEDFB8, 0xFFFFF254, 0xFFFFBC58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1FA6)
    WaitChrThread(0x11, 0x1)

    def lambda_1FC6():
        OP_8E(0xFE, 0xFFFEEC10, 0xFFFFF254, 0xFFFFBC58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1FC6)
    WaitChrThread(0x11, 0x1)
    Return()

    # Function_13_1FA0 end

    def Function_14_1FE1(): pass

    label("Function_14_1FE1")


    def lambda_1FE7():
        OP_8E(0xFE, 0xFFFEDFB8, 0xFFFFF254, 0xFFFFBC58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1FE7)
    WaitChrThread(0x11, 0x1)

    def lambda_2007():
        OP_8E(0xFE, 0xFFFEDFB8, 0xFFFFF254, 0xFFFFA4C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2007)
    WaitChrThread(0x11, 0x1)
    Return()

    # Function_14_1FE1 end

    def Function_15_2022(): pass

    label("Function_15_2022")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x408, 0x0)
    ExitThread()
    OP_72(0x411, 0x0)
    ExitThread()
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x151, 0x8)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -54500, 0, -5600, 270)
    SetChrPos(0x11, -89160, 0, -2500, 90)
    OP_6D(-74700, -3500, -10220, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6E(640, 0)

    def lambda_20B3():
        OP_8E(0xFE, 0xFFFEA1EC, 0x0, 0xFFFFEA20, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_20B3)

    def lambda_20CE():
        OP_6D(-76600, -4500, -8320, 21000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_20CE)

    def lambda_20E6():
        OP_67(0, 6500, -10000, 21000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_20E6)
    FadeToBright(3000, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Aina")

    AnonymousTalk(    #54
        (
            "\x07\x00They all started to live in mine and my grandfather's\x01",
            "house...and before I knew it, my once peaceful life\x01",
            "was shattered.\x02\x03",

            "One day, someone would push me down the stairs;\x01",
            "another, I'd taste something funny in my food...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Aina")

    AnonymousTalk(    #55
        (
            "\x07\x00These kinds of things began happening on a regular\x01",
            "basis.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Aina")

    AnonymousTalk(    #56
        (
            "\x07\x00Legally, they were my relatives while I was a minor,\x01",
            "so there was very little I could do...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Aina")

    AnonymousTalk(    #57
        (
            "\x07\x00I tried reasoning with them at first, but in the end,\x01",
            "I had no choice but to leave home myself.\x02\x03",

            "I wandered the highways alone, going from place to\x01",
            "place and trying not to be discovered...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Aina")

    AnonymousTalk(    #58
        (
            "\x07\x00But I knew that while I could hopefully avoid being\x01",
            "caught that way, I'd eventually just be declared as\x01",
            "missing and presumed dead.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Aina")

    AnonymousTalk(    #59
        (
            "\x07\x00...Besides, after I'd left once, even if I did go back\x01",
            "home, I knew I'd promptly be locked up somewhere\x01",
            "and reported as still missing regardless.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Aina")

    AnonymousTalk(    #60
        (
            "\x07\x00Grandfather's will would be declared as invalid in\x01",
            "time, and my relatives would blissfully share their\x01",
            "newly bequeathed wealth between them.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    def lambda_253C():
        OP_8E(0xFE, 0xFFFF3E2C, 0x0, 0xFFFFF63C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_253C)
    Sleep(1000)
    SetChrName("Aina")

    AnonymousTalk(    #61
        (
            "\x07\x00...I hated the thought of that happening.\x02\x03",

            "That was why I decided to return here to the\x01",
            "capital.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Aina")

    AnonymousTalk(    #62
        (
            "\x07\x00Even if it's the last thing I do, I will formally inherit\x01",
            "what he wanted me to.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4143   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_2022 end

    def Function_16_2643(): pass

    label("Function_16_2643")

    SetPlaceName(0xB8)
    Return()

    # Function_16_2643 end

    def Function_17_2647(): pass

    label("Function_17_2647")

    SetPlaceName(0xB7)
    Return()

    # Function_17_2647 end

    def Function_18_264B(): pass

    label("Function_18_264B")

    SetPlaceName(0xAF)
    Return()

    # Function_18_264B end

    def Function_19_264F(): pass

    label("Function_19_264F")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #63
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_264F end

    SaveToFile()

Try(main)
