from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3111   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        'Dan',                                  # 9
        'Agate',                                # 10
        'Factory Chief Murdock',                # 11
        'Erick',                                # 12
        'Hazel',                                # 13
        'Faye',                                 # 14
        'Ochre',                                # 15
        'Target Camera',                        # 16
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
        'ED6_DT07/CH02030 ._CH',             # 00
        'ED6_DT27/CHDUMMY ._CH',             # 01
        'ED6_DT27/CHDUMMY ._CH',             # 02
        'ED6_DT29/CH14010 ._CH',             # 03
        'ED6_DT29/CH14131 ._CH',             # 04
        'ED6_DT29/CH14160 ._CH',             # 05
        'ED6_DT29/CH14190 ._CH',             # 06
        'ED6_DT29/CH14300 ._CH',             # 07
        'ED6_DT27/CH03980 ._CH',             # 08
        'ED6_DT06/CH20053 ._CH',             # 09
        'ED6_DT07/CH01450 ._CH',             # 0A
        'ED6_DT07/CH01540 ._CH',             # 0B
        'ED6_DT07/CH02620 ._CH',             # 0C
        'ED6_DT07/CH01550 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH02030P._CP',             # 00
        'ED6_DT27/CHDUMMYP._CP',             # 01
        'ED6_DT27/CHDUMMYP._CP',             # 02
        'ED6_DT29/CH14010P._CP',             # 03
        'ED6_DT29/CH14131P._CP',             # 04
        'ED6_DT29/CH14160P._CP',             # 05
        'ED6_DT29/CH14190P._CP',             # 06
        'ED6_DT29/CH14300P._CP',             # 07
        'ED6_DT27/CH03980P._CP',             # 08
        'ED6_DT06/CH20053P._CP',             # 09
        'ED6_DT07/CH01450P._CP',             # 0A
        'ED6_DT07/CH01540P._CP',             # 0B
        'ED6_DT07/CH02620P._CP',             # 0C
        'ED6_DT07/CH01550P._CP',             # 0D
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 8650,
        Z                   = 0,
        Y                   = -1430,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 6130,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -111900,
        Z                   = -4000,
        Y                   = -111000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -110300,
        Z                   = -4000,
        Y                   = -111440,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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


    DeclActor(
        TriggerX            = 50,
        TriggerZ            = 0,
        TriggerY            = 3900,
        TriggerRange        = 400,
        ActorX              = 0,
        ActorZ              = 1500,
        ActorY              = 6130,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6900,
        TriggerZ            = 0,
        TriggerY            = -1410,
        TriggerRange        = 400,
        ActorX              = 8650,
        ActorZ              = 1500,
        ActorY              = -1430,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -200120,
        TriggerZ            = 0,
        TriggerY            = 118010,
        TriggerRange        = 1200,
        ActorX              = -200120,
        ActorZ              = 1500,
        ActorY              = 118010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -121030,
        TriggerZ            = -4000,
        TriggerY            = -99900,
        TriggerRange        = 800,
        ActorX              = -121030,
        ActorZ              = -3000,
        ActorY              = -99900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2AA",          # 00, 0
        "Function_1_2F7",          # 01, 1
        "Function_2_38E",          # 02, 2
        "Function_3_3A4",          # 03, 3
        "Function_4_6F1",          # 04, 4
        "Function_5_910",          # 05, 5
        "Function_6_915",          # 06, 6
        "Function_7_A88",          # 07, 7
        "Function_8_A8D",          # 08, 8
        "Function_9_BA1",          # 09, 9
        "Function_10_16AE",        # 0A, 10
        "Function_11_1712",        # 0B, 11
        "Function_12_1774",        # 0C, 12
    )


    def Function_0_2AA(): pass

    label("Function_0_2AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D7")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D7")
    SetChrFlags(0x15, 0x10)

    label("loc_2D7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_2F6")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 9)

    label("loc_2F6")

    Return()

    # Function_0_2AA end

    def Function_1_2F7(): pass

    label("Function_1_2F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_333")
    OP_B1("T3111_1")
    OP_82(0x80, 0x0)
    OP_71(0x420, 0x0)
    ExitThread()
    OP_71(0x421, 0x0)
    ExitThread()
    OP_71(0x422, 0x0)
    ExitThread()
    OP_71(0x423, 0x0)
    ExitThread()
    OP_71(0x424, 0x0)
    ExitThread()
    OP_71(0x425, 0x0)
    ExitThread()

    label("loc_333")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36F")
    OP_B1("T3111_1")
    OP_82(0x80, 0x0)
    OP_71(0x420, 0x0)
    ExitThread()
    OP_71(0x421, 0x0)
    ExitThread()
    OP_71(0x422, 0x0)
    ExitThread()
    OP_71(0x423, 0x0)
    ExitThread()
    OP_71(0x424, 0x0)
    ExitThread()
    OP_71(0x425, 0x0)
    ExitThread()

    label("loc_36F")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_37F"),
        (109, "loc_37F"),
        (SWITCH_DEFAULT, "loc_387"),
    )


    label("loc_37F")

    OP_22(0xA0, 0x1, 0x64)
    Jump("loc_38D")

    label("loc_387")

    OP_23(0xA0)
    Jump("loc_38D")

    label("loc_38D")

    Return()

    # Function_1_2F7 end

    def Function_2_38E(): pass

    label("Function_2_38E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A3")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_38E")

    label("loc_3A3")

    Return()

    # Function_2_38E end

    def Function_3_3A4(): pass

    label("Function_3_3A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_6ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F1, 4)), scpexpr(EXPR_END)), "loc_588")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_495")

    ChrTalk(    #0
        0xFE,
        (
            "I'm in the middle of talking Ochre here through\x01",
            "my work so he can take over my position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "This job's something you need every detail spelled\x01",
            "out for you, you see. It's kind of hard to pick up\x01",
            "on your own.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_585")

    label("loc_495")


    ChrTalk(    #2
        0xFE,
        (
            "I'm actually going to be becoming an on-board\x01",
            "engineer for the Arseille soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I guess ending up on it that time was just fate,\x01",
            "or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "I was offered the job with some vacation time,\x01",
            "so I wasn't about to tell 'em no!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_585")

    Jump("loc_6ED")

    label("loc_588")

    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x106, 500)
    Sleep(300)

    ChrTalk(    #5
        0xFE,
        "W-Wait! I recognize you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Weren't you one of the bracers on\x01",
            "the Arseille?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x106,
        (
            "#050FYeah...\x02\x03",

            "#051FI remember you, too. You and the other engineers\x01",
            "did a great job when it ended up falling out of the\x01",
            "sky.\x02\x03",

            "Thanks again for what you did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "Ahaha. Think nothing of it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "We were just doing our jobs.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x15, 0x10)
    OP_A2(0x2F8C)

    label("loc_6ED")

    TalkEnd(0xFE)
    Return()

    # Function_3_3A4 end

    def Function_4_6F1(): pass

    label("Function_4_6F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_90C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_83F")

    ChrTalk(    #10
        0xFE,
        (
            "There are conveyor belts like this all throughout\x01",
            "ZCF's underground, connecting various factories\x01",
            "together in a big, complex network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "ZCF itself is like one tall structure, with only\x01",
            "part of it visible above ground.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Not many people know this, but there are\x01",
            "actually a whole five underground floors.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90C")

    label("loc_83F")


    ChrTalk(    #13
        0xFE,
        (
            "I was foreman in an underground orbment\x01",
            "factory at one point...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "...but now I'm going to be working over here\x01",
            "for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Faye's in the middle of explaining the work\x01",
            "she does here to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_90C")

    TalkEnd(0xFE)
    Return()

    # Function_4_6F1 end

    def Function_5_910(): pass

    label("Function_5_910")

    Call(0, 6)
    Return()

    # Function_5_910 end

    def Function_6_915(): pass

    label("Function_6_915")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_A84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_9AE")

    ChrTalk(    #16
        0x14,
        (
            "Professor Russell boarded the elevator not\x01",
            "long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x14,
        (
            "I'm afraid I have no idea where she could've\x01",
            "gone after that, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A84")

    label("loc_9AE")


    ChrTalk(    #18
        0x14,
        "What? You're looking for Professor Russell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x14,
        "She passed by here not long ago, actually.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x14,
        (
            "I saw her boarding the elevator with Tita,\x01",
            "but I'm afraid I have no idea where she\x01",
            "could've gone after that.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_A84")

    TalkEnd(0x14)
    Return()

    # Function_6_915 end

    def Function_7_A88(): pass

    label("Function_7_A88")

    Call(0, 8)
    Return()

    # Function_7_A88 end

    def Function_8_A8D(): pass

    label("Function_8_A8D")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_B9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_B05")

    ChrTalk(    #21
        0x13,
        "It's oddly quiet today, though...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x13,
        (
            "Somehow that just makes me nervous rather\x01",
            "than happy...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9D")

    label("loc_B05")


    ChrTalk(    #23
        0x13,
        (
            "If you happen to hear any strange shouts or\x01",
            "loud explosions while you're here, just...ignore\x01",
            "them, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x13,
        "It's for the best. Just trust me.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_B9D")

    TalkEnd(0x13)
    Return()

    # Function_8_A8D end

    def Function_9_BA1(): pass

    label("Function_9_BA1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-170, 0, -3880, 0)
    OP_67(0, 8480, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(310, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -5000, 0, 9500, 0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x107, 0, 0, -13500, 0)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    FadeToBright(2000, 0)

    def lambda_C40():
        OP_6D(-3950, 0, 4690, 4000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_C40)

    def lambda_C58():
        OP_6C(40000, 4000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_C58)

    def lambda_C68():
        OP_67(0, 5240, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_C68)

    def lambda_C80():
        OP_6B(2760, 4000)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_C80)
    OP_43(0x107, 0x3, 0x0, 0xA)
    Sleep(2500)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_70(0x0, 0x1E)
    OP_73(0x0)

    def lambda_CAC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_CAC)

    def lambda_CBE():
        OP_8E(0xFE, 0xFFFFEC78, 0x0, 0x1AC2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_CBE)
    WaitChrThread(0x12, 0x1)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    WaitChrThread(0x107, 0x3)
    OP_62(0x107, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #25
        0x107,
        "#061F#12POh! Good morning, Mr. Murdock!\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_D48():
        OP_8E(0xFE, 0xFFFFEC78, 0x0, 0x1112, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_D48)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    ChrTalk(    #26
        0x12,
        "#800F#5PO-Oh, it's you, Tita. Good morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x107,
        (
            "#560F#12PUmm... You wouldn't happen to know where\x01",
            "Mom and Grandpa are, would you?\x02\x03",

            "Dad said they came here early this morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x12,
        (
            "#803F#5POooh, they did... I know that very well, indeed...\x02\x03",

            "Erika came charging in with a look on her face\x01",
            "that signaled all hell was about to break loose...\x02\x03",

            "#804FAll the while, she was shouting, 'We've got a new\x01",
            "invention to make, so we need somewhere really,\x01",
            "REALLY big! Hop to it!'#1340W #20W \x01",
            "#803FShe wouldn't take no for an answer, either.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #29
        0x107,
        (
            "#562F#12PI-I'm so sorry about her...\x02\x03",

            "She causes you so much trouble every time she\x01",
            "decides she wants to invent something new.\x02\x03",

            "#067FAt least she's better than Grandpa. Maybe...\x02\x03",

            "She doesn't scare the daylights out of\x01",
            "you by suddenly yelling, 'Fire in the hole!'\x01",
            "riiight before an unexpected explosion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x12,
        (
            "#801F#5PIf only I could wipe that from my memory...\x01",
            "Ahahaha...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #31
        0x12,
        (
            "#800F#5PIn any case, your mother should be up in the\x01",
            "operations room.\x02\x03",

            "I've got no idea what she's planning, but she said\x01",
            "she had something she wanted to look into using\x01",
            "the Capel.\x02\x03",

            "#805FAs for your grandfather, he's in the design room.\x01",
            "I-In a very good mood...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(200)

    def lambda_1253():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1253)
    Sleep(1000)

    ChrTalk(    #32
        0x12,
        (
            "#806F#5PI can't believe the two of them are working\x01",
            "together on something. This can't end well...\x02\x03",

            "P-Please, Goddess... Pleeease don't let them\x01",
            "break anything...\x02\x03",

            "#803FUgh... My stomach hurts...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_133F():

        label("loc_133F")

        TurnDirection(0xFE, 0x12, 500)
        OP_48()
        Jump("loc_133F")

    QueueWorkItem2(0x107, 2, lambda_133F)

    def lambda_1350():
        OP_8E(0xFE, 0xFFFFF31C, 0x0, 0xBE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1350)
    WaitChrThread(0x12, 0x1)

    def lambda_1370():
        OP_8E(0xFE, 0xFFFFF31C, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1370)
    WaitChrThread(0x12, 0x1)

    def lambda_1390():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1390)
    Sleep(1000)

    def lambda_13AF():
        OP_8E(0xFE, 0xFFFFF31C, 0x0, 0xFFFFFE34, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_13AF)
    WaitChrThread(0x12, 0x1)

    def lambda_13CF():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_13CF)
    Sleep(1000)

    def lambda_13EE():
        OP_8E(0xFE, 0xFFFFF31C, 0x0, 0xFFFFDE2C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_13EE)
    Sleep(3000)
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #33
        0x107,
        (
            "#064F#5PActually, now that I think about it, I think this\x01",
            "is the first time they HAVE worked on the same\x01",
            "thing together.\x02\x03",

            "Usually they're competing over who can make\x01",
            "the best invention, not joining forces on one...\x02\x03",

            "#060FGrandpa's amazing on his own, but Mom's just\x01",
            "as capable an engineer, too, even if she is kind\x01",
            "of scary when she gets into her work.\x02\x03",

            "If the two of them are actually going to put \x01",
            "their heads together on something...\x02\x03",

            "#067FHeehee. I can't wait to see the result! ♪\x02\x03",

            "I wanna go see right away!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x107, 0x2)
    OP_8C(0x107, 0, 600)

    def lambda_163F():
        OP_8E(0xFE, 0xFFFFEC78, 0x0, 0x1C70, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_163F)
    WaitChrThread(0x107, 0x1)
    OP_70(0x0, 0x1E)
    OP_73(0x0)

    def lambda_1669():
        OP_8E(0xFE, 0xFFFFEC78, 0x0, 0x251C, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1669)
    WaitChrThread(0x107, 0x1)
    OP_6F(0x0, 30)
    OP_70(0x0, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3119   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_BA1 end

    def Function_10_16AE(): pass

    label("Function_10_16AE")


    def lambda_16B4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_16B4)

    def lambda_16C6():
        OP_8E(0xFE, 0x0, 0x0, 0xFFFFF740, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_16C6)
    Sleep(1000)
    OP_22(0x6D, 0x0, 0x64)
    WaitChrThread(0x107, 0x1)

    def lambda_16F0():
        OP_8E(0xFE, 0xFFFFEC78, 0x0, 0xA78, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_16F0)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 0, 500)
    Return()

    # Function_10_16AE end

    def Function_11_1712(): pass

    label("Function_11_1712")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #34
        (
            "\x07\x05Left: Elevator\x01",
            "Right: Basement Orbment Workshop\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_1712 end

    def Function_12_1774(): pass

    label("Function_12_1774")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #35
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_12_1774 end

    SaveToFile()

Try(main)
