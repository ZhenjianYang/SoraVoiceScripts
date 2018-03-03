from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3110   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3110.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Cassius',                              # 9
        'Royal Army Officer',                   # 10
        'Guard',                                # 11
        'Guard',                                # 12
        'Guard',                                # 13
        'Guard',                                # 14
        'Guard',                                # 15
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
        'ED6_DT27/CH03670 ._CH',             # 00
        'ED6_DT27/CH03673 ._CH',             # 01
        'ED6_DT07/CH01600 ._CH',             # 02
        'ED6_DT07/CH01640 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT27/CH03670P._CP',             # 00
        'ED6_DT27/CH03673P._CP',             # 01
        'ED6_DT07/CH01600P._CP',             # 02
        'ED6_DT07/CH01640P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 22110,
        Z                   = 0,
        Y                   = 157150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -24850,
        Z                   = 0,
        Y                   = 38600,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 23150,
        Z                   = 0,
        Y                   = 127870,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -2240,
        Z                   = 0,
        Y                   = 1150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -10400,
        Z                   = 0,
        Y                   = -3510,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )


    DeclEvent(
        X                   = -30350,
        Y                   = -2500,
        Z                   = 38060,
        Range               = -28450,
        Unknown_10          = 0xFFFFFF06,
        Unknown_14          = 0xA3E8,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )


    DeclActor(
        TriggerX            = 21040,
        TriggerZ            = 0,
        TriggerY            = 158020,
        TriggerRange        = 1000,
        ActorX              = 21040,
        ActorZ              = 800,
        ActorY              = 158020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1EE",          # 00, 0
        "Function_1_217",          # 01, 1
        "Function_2_224",          # 02, 2
        "Function_3_23A",          # 03, 3
        "Function_4_2BF",          # 04, 4
        "Function_5_2DC",          # 05, 5
        "Function_6_2F9",          # 06, 6
        "Function_7_316",          # 07, 7
        "Function_8_333",          # 08, 8
        "Function_9_76E",          # 09, 9
        "Function_10_1438",        # 0A, 10
        "Function_11_1461",        # 0B, 11
        "Function_12_14B7",        # 0C, 12
        "Function_13_1521",        # 0D, 13
        "Function_14_1548",        # 0E, 14
        "Function_15_1585",        # 0F, 15
        "Function_16_15CB",        # 10, 16
        "Function_17_1640",        # 11, 17
        "Function_18_1AB4",        # 12, 18
    )


    def Function_0_1EE(): pass

    label("Function_0_1EE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_216")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_216")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_216")

    Return()

    # Function_0_1EE end

    def Function_1_217(): pass

    label("Function_1_217")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_223")

    label("loc_223")

    Return()

    # Function_1_217 end

    def Function_2_224(): pass

    label("Function_2_224")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_239")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_224")

    label("loc_239")

    Return()

    # Function_2_224 end

    def Function_3_23A(): pass

    label("Function_3_23A")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0x12,
        (
            "The general is waiting for you on the training\x01",
            "ground.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "After checking your equipment, make your way to\x01",
            "the rooftop.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_23A end

    def Function_4_2BF(): pass

    label("Function_4_2BF")

    TalkBegin(0xFE)

    ChrTalk(    #2
        0x13,
        "◆Guard dialogue\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_2BF end

    def Function_5_2DC(): pass

    label("Function_5_2DC")

    TalkBegin(0xFE)

    ChrTalk(    #3
        0x14,
        "◆Guard dialogue\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_2DC end

    def Function_6_2F9(): pass

    label("Function_6_2F9")

    TalkBegin(0xFE)

    ChrTalk(    #4
        0x15,
        "◆Guard dialogue\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_2F9 end

    def Function_7_316(): pass

    label("Function_7_316")

    TalkBegin(0xFE)

    ChrTalk(    #5
        0x16,
        "◆Guard dialogue\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_316 end

    def Function_8_333(): pass

    label("Function_8_333")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x10A, 21070, 0, 136950, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 20650, 0, 138370, 0)
    SetChrPos(0x10, 21360, 0, 159470, 180)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 22110, 0, 157150, 180)
    OP_4A(0x12, 255)
    OP_6D(22020, 0, 137120, 0)
    OP_67(0, 5120, -10000, 0)
    OP_6B(2890, 0)
    OP_6C(45000, 0)
    OP_6E(291, 0)

    def lambda_3D4():
        OP_6D(23210, 0, 157170, 4000)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_3D4)

    def lambda_3EC():
        OP_6E(297, 4000)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_3EC)

    def lambda_3FC():
        OP_8E(0xFE, 0x523A, 0x0, 0x25B0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_3FC)

    def lambda_417():
        OP_8E(0xFE, 0x546A, 0x0, 0x25724, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_417)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10A, 0x2)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10A, 0x0)

    ChrTalk(    #6
        0x12,
        (
            "#5PThis is the commander's room.\x02\x03",

            "What business have you here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x11,
        (
            "#6PI'm Warrant Officer Belc of the garrison, and\x01",
            "this is Anelace, a bracer.\x02\x03",

            "We would like to request a meeting with the\x01",
            "general.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10A,
        "#810F#4PP-Please!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x12,
        "#5PVery well. Wait a moment.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8E(0x12, 0x51F4, 0x0, 0x265DE, 0x7D0, 0x0)
    OP_8E(0x12, 0x51F4, 0x0, 0x26854, 0x7D0, 0x0)
    Sleep(300)
    OP_22(0x71, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #10
        0x12,
        (
            "#4PWarrant Officer Belc and a bracer from the guild\x01",
            "are here to see you, sir.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #11
        0x10,
        "Man's Voice",
        "#2PLet them through.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x12,
        "#4PYes, sir!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 90, 400)
    OP_8E(0x12, 0x51F4, 0x0, 0x265DE, 0x7D0, 0x0)
    OP_8E(0x12, 0x565E, 0x0, 0x265DE, 0x7D0, 0x0)
    OP_8C(0x12, 180, 400)
    Sleep(300)

    ChrTalk(    #13
        0x12,
        "#5PPlease enter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        "#6PThank you.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_67F():
        OP_6D(22290, 0, 158760, 2500)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_67F)

    def lambda_697():
        OP_8E(0xFE, 0x51F4, 0x0, 0x26854, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_697)
    Sleep(400)

    def lambda_6B7():
        OP_8E(0xFE, 0x51CC, 0x0, 0x26322, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_6B7)
    WaitChrThread(0x11, 0x0)
    Sleep(300)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x9)
    OP_73(0x0)
    Sleep(300)

    def lambda_6F2():
        OP_8E(0xFE, 0x538E, 0x0, 0x26F0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_6F2)
    Sleep(400)

    def lambda_712():
        OP_8E(0xFE, 0x538E, 0x0, 0x26F0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_712)
    WaitChrThread(0x11, 0x0)

    def lambda_732():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_732)
    WaitChrThread(0x10A, 0x0)

    def lambda_749():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_749)
    WaitChrThread(0x10A, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x12, 255)
    Call(0, 9)
    Return()

    # Function_8_333 end

    def Function_9_76E(): pass

    label("Function_9_76E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_9F(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10A, 20740, 0, 250590, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 20740, 0, 250590, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrFlags(0x10, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 20940, 0, 260040, 180)
    OP_6D(21250, 0, 251550, 0)
    OP_67(0, 5040, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(45000, 0)
    OP_6E(297, 0)

    def lambda_820():
        OP_6D(22440, 0, 258519, 3000)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_820)

    def lambda_838():
        OP_6E(305, 3000)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_838)
    OP_43(0x11, 0x0, 0x0, 0xD)
    OP_43(0x10A, 0x0, 0x0, 0xE)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10A, 0x0)
    WaitChrThread(0x10A, 0x2)
    WaitChrThread(0x10A, 0x3)

    ChrTalk(    #15
        0x11,
        "I've brought your visitor, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "#1120FVery good.\x02\x03",

            "You may return to your duties, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        "Yes, sir!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x11, 0x0, 0x0, 0xC)
    WaitChrThread(0x11, 0x0)

    ChrTalk(    #18
        0x10,
        (
            "#1120FWell, hello. It's good to see you again.\x02\x03",

            "It sounds like my daughter owes you quite a lot,\x01",
            "Anelace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10A,
        (
            "#810FOh, if anything, it's me who owes her.\x02\x03",

            "Umm... I'm really sorry for making you take time\x01",
            "out of your busy schedule to speak with me, by \x01",
            "the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        (
            "#1120FOh, don't worry about it.\x02\x03",

            "I'm relieved to hear your grandfather still seems\x01",
            "to be in good health, too.\x02\x03",

            "I believe it was because of him that you came here\x01",
            "today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10A,
        (
            "#810FY-Yes, that's right...\x02\x03",

            "So you really do know him, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "#1120FIndeed I do. I owe a lot to him as a swordsman.\x02\x03",

            "I haven't seen him since I put down my blade ten\x01",
            "years ago, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10A,
        (
            "#810FI see...\x02\x03",

            "Actually, the reason I came here today was to\x01",
            "continue the conversation he had with you ten\x01",
            "years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        "#1120FOh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10A,
        (
            "#810F...To tell you the truth, Granddad still laments\x01",
            "the fact that you left the path of the sword to\x01",
            "begin with.\x02\x03",

            "That was why when he heard that you had returned\x01",
            "to the army, he decided to write to me.\x02\x03",

            "Because he wondered whether you returning to the\x01",
            "military may mean you were also ready to pick up\x01",
            "a sword again...\x02\x03",

            "That was why he told me to come and meet you.\x01",
            "To ask you directly how you felt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "#1120FHmm... I see...\x02\x03",

            "Well, it's certainly a great honor that ten years\x01",
            "on, he still cares so much about an inexperienced\x01",
            "and utterly lacking swordsman like myself...\x02\x03",

            "...But I'm afraid my answer is that I still have\x01",
            "no intention of taking up a blade again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10A,
        (
            "#810FC-Can I ask you why, then?\x02\x03",

            "Do you believe the staff to be stronger than the\x01",
            "blade?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        (
            "#1120FNo. In the hands of a skilled wielder, no weapon\x01",
            "is inferior to another.\x02\x03",

            "I just believe a staff to be a more fitting weapon\x01",
            "for me as I am now. That's all.\x02\x03",

            "Given that staffs are a symbol of protection,\x01",
            "which are used more for keeping enemies at bay\x01",
            "rather than cleaving through them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10A,
        (
            "#810FY-You say that as if all swords are good for is\x01",
            "cutting and killing! That's not true at all!\x02\x03",

            "I fight because I want to protect things just\x01",
            "like you do!\x02\x03",

            "Are you saying that with a sword, I can't do that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        (
            "#1120FI'm afraid I don't have the answer to that \x01",
            "question.\x02\x03",

            "Still... Hmm...\x02\x03",

            "...I suppose this is just fate. Perhaps she will\x01",
            "be able to answer your question for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10A,
        "#810FWhat?\x02",
    )

    CloseMessageWindow()

    def lambda_11B6():
        OP_6D(22330, 0, 254190, 2500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_11B6)
    OP_43(0x10, 0x0, 0x0, 0xA)

    def lambda_11D5():

        label("loc_11D5")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_11D5")

    QueueWorkItem2(0x10A, 0, lambda_11D5)
    Sleep(2500)

    ChrTalk(    #32
        0x10A,
        "#810F#5PWh-Who?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10A, 0x2)
    OP_44(0x10A, 0x0)
    OP_8C(0x10A, 180, 400)
    WaitChrThread(0x10, 0x0)
    OP_8C(0x10, 0, 400)

    ChrTalk(    #33
        0x10,
        (
            "#1120FI need to go and sort a few things out.\x02\x03",

            "Once your equipment is ready, come to the training\x01",
            "ground outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10A,
        "#810F#5PM-My equipment?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10,
        (
            "#1120FThat's right. This might end up getting a little\x01",
            "violent.\x02\x03",

            "Anyway, I'll be waiting for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10A,
        "#810F#5PR-Right!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x10, 0x0, 0x0, 0xB)
    WaitChrThread(0x10, 0x0)
    OP_6D(22800, 0, 255550, 1000)

    ChrTalk(    #37
        0x10A,
        (
            "#810F#5PWh-Whew...\x02\x03",

            "I guess I should what he says...\x02\x03",

            "Time to check my equipment over.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x10A, 20820, 0, 156030, 180)
    OP_6D(20820, 0, 156030, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_65(0x0, 0x1)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x0)
    OP_72(0x800, 0x0)
    ExitThread()
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x2000, 0x0)
    ExitThread()
    Sleep(1000)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_9_76E end

    def Function_10_1438(): pass

    label("Function_10_1438")

    OP_8E(0xFE, 0x4EFC, 0x0, 0x3F304, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4EFC, 0x0, 0x3E2EC, 0x7D0, 0x0)
    Return()

    # Function_10_1438 end

    def Function_11_1461(): pass

    label("Function_11_1461")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x5028, 0x0, 0x3DA54, 0x7D0, 0x0)
    Sleep(200)
    OP_22(0x6A, 0x0, 0x64)
    Sleep(300)

    def lambda_1491():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1491)
    OP_8E(0xFE, 0x5028, 0x0, 0x3D284, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_11_1461 end

    def Function_12_14B7(): pass

    label("Function_12_14B7")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x4F9C, 0x0, 0x3E120, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5140, 0x0, 0x3D8E2, 0x7D0, 0x0)
    OP_22(0x6A, 0x0, 0x64)
    Sleep(300)

    def lambda_14F6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14F6)
    OP_8E(0xFE, 0x5140, 0x0, 0x3D090, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_22(0xE6, 0x0, 0x64)
    Return()

    # Function_12_14B7 end

    def Function_13_1521(): pass

    label("Function_13_1521")


    def lambda_1527():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1527)
    OP_8E(0xFE, 0x50AA, 0x0, 0x3E59E, 0x7D0, 0x0)
    Return()

    # Function_13_1521 end

    def Function_14_1548(): pass

    label("Function_14_1548")

    Sleep(600)

    def lambda_1553():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1553)

    def lambda_1565():
        OP_8E(0xFE, 0x53F2, 0x0, 0x3E1DE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1565)
    Sleep(700)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_14_1548 end

    def Function_15_1585(): pass

    label("Function_15_1585")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #38
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_1585 end

    def Function_16_15CB(): pass

    label("Function_16_15CB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D8")
    Return()

    label("loc_15D8")

    EventBegin(0x1)
    OP_4A(0x13, 255)

    ChrTalk(    #39
        0x13,
        "The area beyond here is restricted.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x13,
        "Kindly turn around.\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    OP_4B(0x13, 255)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_16_15CB end

    def Function_17_1640(): pass

    label("Function_17_1640")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x10A, 21070, 0, 136950, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 20650, 0, 138370, 0)
    SetChrPos(0x10, 21360, 0, 159470, 180)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 22110, 0, 157150, 180)
    OP_6D(22020, 0, 137120, 0)
    OP_67(0, 7520, -10000, 0)
    OP_6B(2890, 0)
    OP_6C(45000, 0)
    OP_6E(337, 0)

    def lambda_16DD():
        OP_6D(23210, 0, 157170, 7000)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_16DD)

    def lambda_16F5():
        OP_6E(297, 7000)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_16F5)

    def lambda_1705():
        OP_67(0, 5120, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_1705)

    def lambda_171D():
        OP_8E(0xFE, 0x523A, 0x0, 0x25B0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_171D)

    def lambda_1738():
        OP_8E(0xFE, 0x546A, 0x0, 0x25724, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1738)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_22(0x6A, 0x0, 0x64)
    Sleep(1500)
    OP_22(0xE6, 0x0, 0x64)
    Sleep(1000)
    Call(0, 18)
    WaitChrThread(0x10A, 0x2)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10A, 0x0)

    ChrTalk(    #41
        0x12,
        "#5PThis way leads to the commander's room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x12,
        "#5PPlease state your business.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x11,
        (
            "#6PI've brought a bracer under orders from the\x01",
            "general.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        "#6PShe is due to have a meeting with him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10A,
        "#812F#4PP-Please!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x12,
        "#5PUnderstood. Wait a moment, then, please.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8E(0x12, 0x51F4, 0x0, 0x265DE, 0x7D0, 0x0)
    OP_8E(0x12, 0x51F4, 0x0, 0x26854, 0x7D0, 0x0)
    Sleep(300)
    OP_22(0x71, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #47
        0x12,
        (
            "#4PGeneral, your visitor from the Bracer Guild is\x01",
            "here to see you!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #48
        0x10,
        "Man's Voice",
        "#2PLet her through.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x12,
        "#4PYes, sir!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 90, 400)
    OP_8E(0x12, 0x51F4, 0x0, 0x265DE, 0x7D0, 0x0)
    OP_8E(0x12, 0x565E, 0x0, 0x265DE, 0x7D0, 0x0)
    OP_8C(0x12, 180, 400)
    Sleep(300)

    ChrTalk(    #50
        0x12,
        "#5PPlease enter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x11,
        "#6PGood work.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_19C5():
        OP_6D(22290, 0, 158760, 2500)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_19C5)

    def lambda_19DD():
        OP_8E(0xFE, 0x51F4, 0x0, 0x26854, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_19DD)
    Sleep(400)

    def lambda_19FD():
        OP_8E(0xFE, 0x51CC, 0x0, 0x26322, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_19FD)
    WaitChrThread(0x11, 0x0)
    Sleep(300)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x9)
    OP_73(0x0)
    Sleep(300)

    def lambda_1A38():
        OP_8E(0xFE, 0x538E, 0x0, 0x26F0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1A38)
    Sleep(400)

    def lambda_1A58():
        OP_8E(0xFE, 0x538E, 0x0, 0x26F0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1A58)
    WaitChrThread(0x11, 0x0)

    def lambda_1A78():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1A78)
    WaitChrThread(0x10A, 0x0)

    def lambda_1A8F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1A8F)
    WaitChrThread(0x10A, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x12, 255)
    Call(0, 18)
    Return()

    # Function_17_1640 end

    def Function_18_1AB4(): pass

    label("Function_18_1AB4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    OP_9F(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10A, 20740, 0, 250590, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 20740, 0, 250590, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrFlags(0x10, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 20940, 0, 260040, 180)
    OP_51(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(21250, 0, 251550, 0)
    OP_67(0, 5040, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(45000, 0)
    OP_6E(297, 0)

    def lambda_1BA2():
        OP_6D(22360, 0, 258519, 3000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1BA2)

    def lambda_1BBA():
        OP_6E(305, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1BBA)
    OP_43(0x11, 0x0, 0x0, 0xD)
    OP_43(0x10A, 0x0, 0x0, 0xE)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10A, 0x0)
    WaitChrThread(0x10A, 0x2)
    WaitChrThread(0x10A, 0x3)
    Sleep(500)

    ChrTalk(    #52
        0x11,
        "#6PI've brought your visitor, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        (
            "#1125F#5PVery good.\x02\x03",

            "#1120FYou may return to your duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x11,
        "#6PThank you, sir.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x11, 0x0, 0x0, 0xC)
    Sleep(3000)

    def lambda_1C8B():
        OP_6D(22360, 0, 259980, 1500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_1C8B)

    def lambda_1CA3():
        OP_8E(0xFE, 0x51CC, 0x0, 0x3ECC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1CA3)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10A, 0x0)
    Sleep(500)

    ChrTalk(    #55
        0x10,
        (
            "#1123F#5PI'm really sorry about the delay, there,\x01",
            "Anelace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10A,
        (
            "#816F#12P#12POh, don't be.\x02\x03",

            "#1316FI'm more thankful you took the time out\x01",
            "of your busy schedule to speak with me\x01",
            "at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        (
            "#1121F#5PHaha. This is the least I could do for someone\x01",
            "from my old line of work!\x02\x03",

            "#1120FIt's been a while since we last met, though,\x01",
            "hasn't it?\x02\x03",

            "You've become a seasoned veteran before\x01",
            "I knew it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10A,
        (
            "#819F#12PHeehee. I'd certainly like to think I have.\x02\x03",

            "#816FI can't have Estelle soar ahead of me while\x01",
            "she's abroad, can I?\x02\x03",

            "This is just what rivals do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10,
        (
            "#1125F#5PHaha. So they do.\x02\x03",

            "#1120FI'll be looking forward to seeing just how much\x01",
            "stronger the two of you can become.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10A,
        "#811F#12PYou won't be disappointed!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x10,
        (
            "#1120F#5PGetting to the point...I was pleased to hear\x01",
            "that old Master Ka-fai is still in good health.\x02\x03",

            "I believe it was because of him that you came\x01",
            "here today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10A,
        (
            "#1316F#12PY-Yes. That's right...\x02\x03",

            "#818FI didn't realize you were an acquaintance of his\x01",
            "before this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10,
        (
            "#1125F#5PI certainly am. In short, he's the man who taught\x01",
            "me the way of the sword.\x02\x03",

            "#1120FThat was over twenty years ago by this point...\x01",
            "The first time we met was when I was back at\x01",
            "the military academy, so I studied it under him.\x02\x03",

            "#1121FHaha. I still remember the harsh training sessions\x01",
            "he gave here at Leiston like they were yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10A,
        (
            "#819F#12PR-Really...?\x02\x03",

            "#814FIs there any special reason you didn't say you\x01",
            "knew him before?\x02\x03",

            "You knew I was his granddaughter, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        (
            "#1125F#5P...I did.\x02\x03",

            "#1120FBy the time I first met you, I had long given up\x01",
            "the path of the sword.\x02\x03",

            "It didn't feel appropriate in my eyes to act as if\x01",
            "I was his student in light of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10A,
        "#813F#12POh... Got'cha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x10,
        (
            "#1125F#5PI haven't seen him in...about ten years, I think?\x02\x03",

            "#1120FHe does write to me on occasion, but how is he\x01",
            "these days? Does he still have that same old vim\x01",
            "and vigor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x10A,
        (
            "#819F#12PHaha... Yup. He really doesn't act his age at\x01",
            "all.\x02\x03",

            "#812FStill...if you'll let me get right to the point...\x02\x03",

            "...the reason I came here is to continue the \x01",
            "discussion he had with you ten years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x10,
        "#1124F#5POh?\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_21()
    OP_1D(0xAD)
    Sleep(500)

    ChrTalk(    #70
        0x10A,
        (
            "#1316F#12PTo tell you the truth, Pappy still laments the\x01",
            "fact that you left the path of the sword.\x02\x03",

            "That was why he wrote to me when he heard\x01",
            "you'd returned to the army.\x02\x03",

            "#813FHe wondered whether you returning to the\x01",
            "military may mean you were also ready to pick\x01",
            "up a sword again...\x02\x03",

            "#812FSo, this is it. He'd like to know, directly from\x01",
            "you, how you feel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10,
        "#1128F#5PHmm... I see...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #72
        0x10,
        (
            "#1125F#5PWell, it's a great honor that after so many years,\x01",
            "he still cares so much about an inexperienced\x01",
            "and utterly lacking swordsman like me.\x02\x03",

            "#1122FAnd yet I'm afraid my answer is that I still have\x01",
            "no intention of taking up a blade again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10A,
        (
            "#1317F#12P...\x02\x03",

            "#813FC-Can I ask you why?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10,
        (
            "#1123F#5PHmm... You certainly can, but I'm not sure\x01",
            "how to put my answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x10A,
        (
            "#1316F#12PThis has always been on my mind, too...\x02\x03",

            "I've always wondered what would prompt someone\x01",
            "so skilled with a sword that they even gained the\x01",
            "title Divine Blade to leave it all behind...\x02\x03",

            "#813FAnd I don't mean to make light of your skill with\x01",
            "your staff or say it's inferior. Nothing like that.\x02\x03",

            "#812FIt's just hard to wrap my head around why you did\x01",
            "what you did, and there's a little part of me that\x01",
            "can't accept it, either!\x02\x03",

            "Especially now that you've returned to the army!\x01",
            "Why CAN'T you return to being a swordsman?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x10,
        "#1122F#5PHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x10A,
        (
            "#1316F#12PU-Unless...\x02\x03",

            "#813FUnless you believe that the staff is stronger\x01",
            "than the sword after all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x10,
        (
            "#1125F#5PNo. Not at all.\x02\x03",

            "I just believe a staff to be a more fitting weapon\x01",
            "for me as I am now.\x02\x03",

            "#1120FStaves are a symbol of protection which are used\x01",
            "more for keeping enemies at bay than cleaving\x01",
            "through them.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #79
        0x10A,
        (
            "#1317F#12PY-You say that as if all swords are good for\x01",
            "is cutting and killing! That's not true!\x02\x03",

            "#813FI fight because I want to protect things just\x01",
            "like you do!\x02\x03",

            "#30WAs a swordsman, as a bracer, and as myself...\x02\x03",

            "#815F#20WAre you telling me the swordsmanship Pappy\x01",
            "taught me isn't going to let me do that?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x10,
        "#1122F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10A,
        (
            "#1316F#12PI-I'm sorry... I didn't ask for you to take time\x01",
            "out of your day so I could come and shout at\x01",
            "you.\x02\x03",

            "#813F#30WBut I...I can't accept what you're saying.\x02\x03",

            "Up until all of what happened here in Liberl,\x01",
            "I'd never felt any doubts that swordsmanship\x01",
            "was the right path for me.\x02\x03",

            "In the end, all of what happened just served\x01",
            "to remind me of how powerless I really am.\x02\x03",

            "#1316FAnd now, I...I feel like no matter how hard\x01",
            "I try, I'll always be a rookie. I'll never be strong\x01",
            "enough to do what I want to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x10,
        (
            "#1125F#5P...Now I see.\x02\x03",

            "Hmm... Perhaps this is fate.\x02\x03",

            "#1120FI see Master Ka-fai hasn't changed one bit.\x01",
            "He's the same firecracker he always was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x10A,
        "#814F#12PWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x10,
        (
            "#1125F#5PI'm afraid as I am now, I'm not able to answer\x01",
            "the questions you're asking me.\x02\x03",

            "#1122FBut I know someone else who can.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_6B(3130, 3000)
    OP_0D()
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/C3101   ._SN", 100, 0, 0)
    IdleLoop()

    def lambda_305D():
        OP_6D(22360, 0, 257980, 2500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_305D)
    OP_43(0x10, 0x0, 0x0, 0xA)

    def lambda_307C():

        label("loc_307C")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_307C")

    QueueWorkItem2(0x10A, 0, lambda_307C)
    Sleep(2500)

    ChrTalk(    #85
        0x10A,
        "#812F#5PWh-Where are you going?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10A, 0x2)
    OP_44(0x10A, 0x0)
    OP_8C(0x10A, 180, 400)
    WaitChrThread(0x10, 0x0)
    OP_8C(0x10, 0, 400)

    ChrTalk(    #86
        0x10,
        (
            "#1120FYou'll understand soon enough.\x02\x03",

            "Follow me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10A,
        "#813F#5PR-Right...\x02",
    )

    CloseMessageWindow()
    OP_43(0x10, 0x0, 0x0, 0xB)
    Sleep(600)

    def lambda_312D():
        OP_8E(0xFE, 0x51CC, 0x0, 0x3DA54, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_312D)
    WaitChrThread(0x10A, 0x0)

    def lambda_314D():
        OP_8E(0xFE, 0x51CC, 0x0, 0x3D284, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_314D)

    def lambda_3168():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3168)
    FadeToDark(2000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/C3101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_1AB4 end

    SaveToFile()

Try(main)
