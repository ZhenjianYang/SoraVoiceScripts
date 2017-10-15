from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1301   ._SN',
        MapName             = 'Bose',
        Location            = 'C1301.x',
        MapIndex            = 52,
        MapDefaultBGM       = "ed60089",
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
        'Guard Captain',                        # 9
        'Major Vander',                         # 10
        'Dorothy',                              # 11
        'Soldier',                              # 12
        'Soldier',                              # 13
        ' ',                                    # 14
        ' ',                                    # 15
        ' ',                                    # 16
        ' ',                                    # 17
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
        'ED6_DT07/CH01600 ._CH',             # 00
        'ED6_DT27/CH03570 ._CH',             # 01
        'ED6_DT07/CH01300 ._CH',             # 02
        'ED6_DT07/CH02070 ._CH',             # 03
        'ED6_DT06/CH20063 ._CH',             # 04
        'ED6_DT06/CH20064 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01600P._CP',             # 00
        'ED6_DT27/CH03570P._CP',             # 01
        'ED6_DT07/CH01300P._CP',             # 02
        'ED6_DT07/CH02070P._CP',             # 03
        'ED6_DT06/CH20063P._CP',             # 04
        'ED6_DT06/CH20064P._CP',             # 05
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -11400,
        TriggerZ            = 4000,
        TriggerY            = -2400,
        TriggerRange        = 1500,
        ActorX              = -8930,
        ActorZ              = 6520,
        ActorY              = -880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -9150,
        TriggerZ            = 5540,
        TriggerY            = -590,
        TriggerRange        = 1000,
        ActorX              = -10940,
        ActorZ              = 5000,
        ActorY              = -1870,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_242",          # 00, 0
        "Function_1_269",          # 01, 1
        "Function_2_26F",          # 02, 2
        "Function_3_1762",         # 03, 3
        "Function_4_17A8",         # 04, 4
        "Function_5_17D3",         # 05, 5
        "Function_6_17EF",         # 06, 6
        "Function_7_181F",         # 07, 7
        "Function_8_1872",         # 08, 8
        "Function_9_18CC",         # 09, 9
        "Function_10_1943",        # 0A, 10
        "Function_11_1C87",        # 0B, 11
        "Function_12_1CB2",        # 0C, 12
        "Function_13_1CDD",        # 0D, 13
        "Function_14_1D08",        # 0E, 14
        "Function_15_1D33",        # 0F, 15
        "Function_16_1D63",        # 10, 16
        "Function_17_1DA7",        # 11, 17
        "Function_18_1DEB",        # 12, 18
        "Function_19_1E2F",        # 13, 19
        "Function_20_1F13",        # 14, 20
        "Function_21_1F6B",        # 15, 21
        "Function_22_1FB5",        # 16, 22
        "Function_23_1FF1",        # 17, 23
        "Function_24_201F",        # 18, 24
        "Function_25_2103",        # 19, 25
        "Function_26_215B",        # 1A, 26
        "Function_27_21A5",        # 1B, 27
        "Function_28_21E1",        # 1C, 28
    )


    def Function_0_242(): pass

    label("Function_0_242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_25C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 2)
    Jump("loc_268")

    label("loc_25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_268")
    Event(0, 10)

    label("loc_268")

    Return()

    # Function_0_242 end

    def Function_1_269(): pass

    label("Function_1_269")

    SetMapFlags(0x2000000)
    Return()

    # Function_1_269 end

    def Function_2_26F(): pass

    label("Function_2_26F")

    EventBegin(0x0)
    LoadEffect(0x0, "map\\\\mp032_00.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-17010, 4000, -16370, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_43(0x8, 0x1, 0x0, 0x3)
    Sleep(1000)
    OP_43(0x9, 0x1, 0x0, 0x4)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #0
        0x8,
        "Please, this way.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)

    ChrTalk(    #1
        0x9,
        "#273F#4PHmm...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)

    def lambda_33B():
        OP_6D(-6100, 4000, -2470, 7000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_33B)

    def lambda_353():
        OP_67(0, 5960, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_353)

    def lambda_36B():
        OP_6E(255, 7000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_36B)

    def lambda_37B():
        OP_6B(4500, 7000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_37B)
    OP_43(0x8, 0x1, 0x0, 0x5)
    Sleep(300)
    OP_43(0x9, 0x1, 0x0, 0x6)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x8, 0x0)

    ChrTalk(    #2
        0x9,
        (
            "#277F#2PIt seems to be in perfect condition.\x02\x03",

            "Your men have been maintaining it\x01",
            "since its capture, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#1PHaha, well, we've used it for flight\x01",
            "practice a number of times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        "#1PEven flew it myself a few times.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        (
            "#277F#2PI'm curious. As a man with experience,\x01",
            "how would you say it handles?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#1PAmazingly, I'd say. Its speed and\x01",
            "agility are superior to even our military\x01",
            "patrol ships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#1PIt's one of the high-speed classes\x01",
            "made by the Reinford Company some\x01",
            "years back, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#1PThat was a bit of a surprise--er, begging\x01",
            "your pardon, Major. I always tend to think\x01",
            "of airships as a Liberlian thing, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        (
            "#277F#2PNone taken. And yes, it's 'ours,' but the\x01",
            "armor is frighteningly thin compared to\x01",
            "your ships, and it carries few weapons.\x02\x03",

            "At the same time, however, it's far too\x01",
            "expensive and non-expendable to use\x01",
            "as a scout vessel.\x02\x03",

            "Airships of this type frankly have little\x01",
            "military value.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        "#1PHuh... I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "#1PWell, it's a good ship, though.\x01",
            "Feels like a waste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x9,
        (
            "#272F#2PIn Erebonia, ships of this type\x01",
            "are really little more than toys of\x01",
            "the nobility and newly wealthy.\x02\x03",

            "I'm sure those 'bandits' obtained it\x01",
            "in a similar fashion.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)

    ChrTalk(    #13
        0x8,
        (
            "#1PRight, they're the family of Baron Capua,\x01",
            "correct?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)

    ChrTalk(    #14
        0x9,
        (
            "#270F#2PFORMER baron, Captain.\x02\x03",

            "With the loss of their land, the family's\x01",
            "been stripped of the title, as well.\x02\x03",

            "In fact, the creditor who issued the\x01",
            "original title loan on this airship has\x01",
            "requested we return it to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        "#1PI see... Sounds like a bit of a mess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        (
            "#272F#2PRegardless. The fact of the matter is,\x01",
            "former Imperial nobility have caused\x01",
            "Liberl a great deal of hardship.\x02\x03",

            "You have my apologies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#1PHaha, don't worry, it wasn't\x01",
            "that big a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        "#1PSo when would you like to take it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x9,
        (
            "#277F#2PIn a few days, at the earliest.\x02\x03",

            "I would imagine you're busy\x01",
            "with a few things as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "#1PHah! No, it's nothing.\x01",
            "Dregs of the old Intelligence\x01",
            "Division is all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#1PIt's really just the final thrashings\x01",
            "of a dying beast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#1PWe'll have them all in stocks before\x01",
            "the month's out, mark my words.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xA, -17490, 4000, -5790, 180)
    SetChrChipByIndex(0xA, 4)

    NpcTalk(    #23
        0xA,
        "Young Woman's Voice",
        (
            "#1PWooow, it's way different from the\x01",
            "last time I was here!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0xA, -17100, 2000, -11000, 180)

    def lambda_C89():
        OP_6D(-12350, 4000, -10330, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_C89)

    def lambda_CA1():
        OP_6B(3830, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_CA1)
    OP_43(0xB, 0x1, 0x0, 0x7)
    Sleep(400)
    OP_43(0xA, 0x1, 0x0, 0x8)

    def lambda_CC4():

        label("loc_CC4")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_CC4")

    QueueWorkItem2(0x9, 3, lambda_CC4)
    Sleep(100)

    def lambda_CDA():

        label("loc_CDA")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_CDA")

    QueueWorkItem2(0x8, 3, lambda_CDA)
    Sleep(5000)

    def lambda_CF0():
        OP_6D(-10820, 4000, -7210, 2000)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_CF0)
    WaitChrThread(0xA, 0x1)
    OP_44(0x9, 0x3)
    OP_44(0x8, 0x3)
    OP_8C(0xA, 45, 400)
    Sleep(100)
    OP_8C(0xB, 45, 400)
    WaitChrThread(0xA, 0x0)

    ChrTalk(    #24
        0xA,
        (
            "#153FOooh, the sky bandit ship!\x02\x03",

            "#150FI didn't know it was still here...\x01",
            "Neat!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0xA, 5)
    SetChrSubChip(0xA, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #25
        0xA,
        (
            "#151FAhhh, it's so nice.\x02\x03",

            "Very cutely lit by the night sky\x01",
            "and everything!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xA, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xA, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xA, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_8C(0xB, 180, 400)

    ChrTalk(    #26
        0xB,
        "#6PUh, 'scuse me, missy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        (
            "#6PYou mind getting permission before\x01",
            "snapping pictures?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0xA, 4)
    SetChrSubChip(0xA, 0)
    OP_0D()
    OP_8C(0xA, 180, 600)
    Sleep(500)

    ChrTalk(    #28
        0xA,
        "#153F#6P#3SOoooooh!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_F68():
        OP_6D(-8500, 4000, -21880, 3000)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_F68)

    def lambda_F80():
        OP_67(0, 3170, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_F80)

    def lambda_F98():
        OP_6C(169000, 3000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_F98)

    def lambda_FA8():
        OP_6B(4090, 3000)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_FA8)

    def lambda_FB8():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_FB8)
    OP_8E(0xA, 0xFFFFD5EE, 0xFA0, 0xFFFFCBB2, 0x1388, 0x0)
    OP_8C(0xA, 180, 400)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #29
        0xA,
        (
            "#150F#5PAnd the misty valley's all\x01",
            "glowy and stuff from the light\x01",
            "of the moon...\x02\x03",

            "#151FHee, it's so magical! And cute!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0xA, 5)
    SetChrSubChip(0xA, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #30
        0xA,
        "#151F#5POkay, say cheeeese! ㈱\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0xA, 5)
    SetChrSubChip(0xA, 0)
    OP_0D()
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xA, -300, 1300, 1000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xA, -300, 1300, 1000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xA, -300, 1300, 1000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    ChrTalk(    #31
        0xB,
        "#5PLISTEN to me, woman!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    OP_6D(-9870, 4000, -5820, 0)
    OP_67(0, 5730, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(145000, 0)
    OP_6E(342, 0)
    OP_8C(0x9, 180, 0)
    OP_0D()

    ChrTalk(    #32
        0x9,
        "#273F#5PWho...is that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "#5PAh, her? Liberl News photographer,\x01",
            "if I remember right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "#5PShe visited--more like pushed her way in,\x01",
            "really--to write an article on the training\x01",
            "ground we're running.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "#5PShe had an appointment earlier... Didn't\x01",
            "think she'd be around, uh, this late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        "#272F#5PHm.\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0xA, 4)
    SetChrSubChip(0xA, 0)
    OP_0D()
    OP_8C(0xA, 0, 600)
    Sleep(500)

    ChrTalk(    #37
        0xA,
        "#153F#3S#4PWhooooooooa!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_1374():

        label("loc_1374")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_1374")

    QueueWorkItem2(0xB, 0, lambda_1374)

    def lambda_1385():
        OP_6D(-10080, 4000, -2580, 2000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1385)
    OP_8E(0xA, 0xFFFFD652, 0xFA0, 0xFFFFF0C4, 0x1388, 0x0)
    WaitChrThread(0xA, 0x1)
    OP_44(0xB, 0x0)

    ChrTalk(    #38
        0xA,
        (
            "#150FI've never seen a uniform like that.\x02\x03",

            "And you're reeeally tall, too!\x02\x03",

            "Hey, hey, what squad are you a\x01",
            "member of?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        "#273F#6PErm, No, I'm--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xA,
        (
            "#151FOops. I forgot to introduce myself,\x01",
            "sorry!\x02\x03",

            "I'm Dorothy! Dorothy Hyatt!\x01",
            "I'm a camerawoman for the Liberl News!\x02\x03",

            "I'm here to get a lotta pictures of the new\x01",
            "training grounds for a special edition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "#272F#6P...I'm Mueller of the Erebonian Imperial\x01",
            "military, here on a diplomatic mission\x01",
            "on behalf of my country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xA,
        (
            "#153FNo way! Erebonian army man?!\x02\x03",

            "#151FWoooow, I've never seen one of\x01",
            "YOU guys before!\x02\x03",

            "I was living in Grancel during the war,\x01",
            "you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        "#270F#6PIs that...so?\x02",
    )

    CloseMessageWindow()

    def lambda_163E():
        OP_6D(-12340, 4000, -8660, 2000)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_163E)
    Sleep(200)
    OP_43(0xC, 0x1, 0x0, 0x9)
    WaitChrThread(0xC, 0x2)
    Sleep(2000)

    def lambda_166C():
        OP_6D(-11560, 4000, -3660, 2000)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_166C)
    WaitChrThread(0xC, 0x2)
    WaitChrThread(0xC, 0x1)

    ChrTalk(    #44
        0xC,
        "Sir, may I have a moment?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        "What is it, soldier?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xC,
        "Communication from headquarters, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xC,
        (
            "There's been a change in the movements\x01",
            "of the Intelligence remnants.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C1402   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_26F end

    def Function_3_1762(): pass

    label("Function_3_1762")

    SetChrPos(0xFE, -16500, 0, -8750, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFBF8C, 0xFA0, 0xFFFFBF8C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFC4DC, 0xFA0, 0xFFFFBFDC, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_3_1762 end

    def Function_4_17A8(): pass

    label("Function_4_17A8")

    SetChrPos(0xFE, -17490, 0, -8830, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFBCD0, 0xFA0, 0xFFFFBF8C, 0xBB8, 0x0)
    Return()

    # Function_4_17A8 end

    def Function_5_17D3(): pass

    label("Function_5_17D3")

    OP_8E(0xFE, 0xFFFFD6F2, 0xFA0, 0x1F4, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_5_17D3 end

    def Function_6_17EF(): pass

    label("Function_6_17EF")

    OP_8E(0xFE, 0xFFFFC61C, 0xFA0, 0xFFFFC072, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD6FC, 0xFA0, 0xFFFFFB32, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_6_17EF end

    def Function_7_181F(): pass

    label("Function_7_181F")

    SetChrPos(0xFE, -16500, 0, -8750, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFBF8C, 0xFA0, 0xFFFFBF8C, 0xBB8, 0x0)
    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFD026, 0xFA0, 0xFFFFE408, 0xBB8, 0x0)
    Return()

    # Function_7_181F end

    def Function_8_1872(): pass

    label("Function_8_1872")

    SetChrPos(0xFE, -17490, 0, -8830, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFBBAE, 0xFA0, 0xFFFFBF8C, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFCF5E, 0xFA0, 0xFFFFDEF4, 0xBB8, 0x0)
    Return()

    # Function_8_1872 end

    def Function_9_18CC(): pass

    label("Function_9_18CC")

    SetChrPos(0xFE, -16500, 0, -8750, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_18F3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_18F3)
    OP_8E(0xFE, 0xFFFFBBAE, 0xFA0, 0xFFFFBF8C, 0xFA0, 0x0)
    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFCA7C, 0xFA0, 0xFFFFE70A, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 0)
    Return()

    # Function_9_18CC end

    def Function_10_1943(): pass

    label("Function_10_1943")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-17010, 4000, -16370, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    OP_43(0x129, 0x1, 0x0, 0xB)
    Sleep(500)
    OP_43(0x12A, 0x1, 0x0, 0xC)
    Sleep(500)
    OP_43(0x146, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0xE)
    WaitChrThread(0x129, 0x1)
    OP_8C(0x129, 45, 400)

    ChrTalk(    #48
        0x129,
        "#192F#4PAhhhhh...!\x02",
    )

    CloseMessageWindow()

    def lambda_19EB():
        OP_6D(-7610, 4000, -1690, 7000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_19EB)

    def lambda_1A03():
        OP_67(0, 5790, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1A03)

    def lambda_1A1B():
        OP_6E(255, 7000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1A1B)

    def lambda_1A2B():
        OP_6B(4660, 7000)
        ExitThread()

    QueueWorkItem(0x129, 3, lambda_1A2B)
    OP_43(0x129, 0x1, 0x0, 0xF)
    Sleep(300)
    OP_43(0x12A, 0x1, 0x0, 0x10)
    Sleep(300)
    OP_43(0x146, 0x1, 0x0, 0x11)
    Sleep(400)
    OP_43(0x102, 0x1, 0x0, 0x12)
    WaitChrThread(0x146, 0x1)

    ChrTalk(    #49
        0x129,
        (
            "#191F#5PMy beautiful, beautiful Bobcat!\x01",
            "How I've missed you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x146,
        (
            "#211FLooks like they kept her fixed up,\x01",
            "at least!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x12A,
        (
            "#202F#5PThe Royal Army knows how to\x01",
            "treat an airship, if nothing else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x102,
        (
            "#1035F#2PI know this is a happy reunion,\x01",
            "but we're very short on time.\x02\x03",

            "#1030FWe don't have the ignition key,\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12A, 180, 400)

    ChrTalk(    #53
        0x12A,
        "#200F#5PRight, right. Let's see if we can find it.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x129, 180, 400)
    OP_8C(0x146, 180, 400)

    ChrTalk(    #54
        0x129,
        (
            "#198F#5PHmph. Could've let me have my\x01",
            "moment for a LITTLE longer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x146,
        (
            "#210F#5PHopefully, the key's still somewhere\x01",
            "in the Bobcat.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1804)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_10_1943 end

    def Function_11_1C87(): pass

    label("Function_11_1C87")

    SetChrPos(0xFE, -17220, 0, -8680, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0xBB8, 0x0)
    Return()

    # Function_11_1C87 end

    def Function_12_1CB2(): pass

    label("Function_12_1CB2")

    SetChrPos(0xFE, -17220, 0, -8680, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFE55C, 0xBB8, 0x0)
    Return()

    # Function_12_1CB2 end

    def Function_13_1CDD(): pass

    label("Function_13_1CDD")

    SetChrPos(0xFE, -17220, 0, -8680, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFE944, 0xBB8, 0x0)
    Return()

    # Function_13_1CDD end

    def Function_14_1D08(): pass

    label("Function_14_1D08")

    SetChrPos(0xFE, -17220, 0, -8680, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFED2C, 0xBB8, 0x0)
    Return()

    # Function_14_1D08 end

    def Function_15_1D33(): pass

    label("Function_15_1D33")

    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD6FC, 0xFA0, 0x2DA, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_15_1D33 end

    def Function_16_1D63(): pass

    label("Function_16_1D63")

    OP_90(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD5EE, 0xFA0, 0xFFFFFE20, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_16_1D63 end

    def Function_17_1DA7(): pass

    label("Function_17_1DA7")

    OP_90(0xFE, 0x0, 0x0, 0xFFFFF830, 0xBB8, 0x0)
    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD0E4, 0xFA0, 0x2D0, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_17_1DA7 end

    def Function_18_1DEB(): pass

    label("Function_18_1DEB")

    OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD210, 0xFA0, 0xFFFFF9B6, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_18_1DEB end

    def Function_19_1E2F(): pass

    label("Function_19_1E2F")

    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x0, 0x1, 0x0, 0x17)
    OP_43(0x1, 0x1, 0x0, 0x16)
    OP_43(0x2, 0x1, 0x0, 0x15)
    OP_43(0x3, 0x1, 0x0, 0x14)
    WaitChrThread(0x3, 0x1)
    OP_30(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_19_1E2F end

    def Function_20_1F13(): pass

    label("Function_20_1F13")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0xF, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0xE, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0xD, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 90, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFDD3C, 0x1586, 0xFFFFFD80, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_20_1F13 end

    def Function_21_1F6B(): pass

    label("Function_21_1F6B")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0xE, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0xD, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 90, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFDD3C, 0x1586, 0xFFFFFD80, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_21_1F6B end

    def Function_22_1FB5(): pass

    label("Function_22_1FB5")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0xD, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 90, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFDD3C, 0x1586, 0xFFFFFD80, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_22_1FB5 end

    def Function_23_1FF1(): pass

    label("Function_23_1FF1")

    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 90, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFDD3C, 0x1586, 0xFFFFFD80, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_23_1FF1 end

    def Function_24_201F(): pass

    label("Function_24_201F")

    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x0, 0x1, 0x0, 0x1C)
    OP_43(0x1, 0x1, 0x0, 0x1B)
    OP_43(0x2, 0x1, 0x0, 0x1A)
    OP_43(0x3, 0x1, 0x0, 0x19)
    WaitChrThread(0x3, 0x1)
    OP_30(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_24_201F end

    def Function_25_2103(): pass

    label("Function_25_2103")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0xF, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0xE, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0xD, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 270, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFD508, 0xFA0, 0xFFFFF83A, 0x1F4, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_25_2103 end

    def Function_26_215B(): pass

    label("Function_26_215B")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0xE, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0xD, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 270, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFD508, 0xFA0, 0xFFFFF83A, 0x1F4, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_26_215B end

    def Function_27_21A5(): pass

    label("Function_27_21A5")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0xD, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 270, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFD508, 0xFA0, 0xFFFFF83A, 0x1F4, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_27_21A5 end

    def Function_28_21E1(): pass

    label("Function_28_21E1")

    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 270, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFD508, 0xFA0, 0xFFFFF83A, 0x1F4, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_28_21E1 end

    SaveToFile()

Try(main)
