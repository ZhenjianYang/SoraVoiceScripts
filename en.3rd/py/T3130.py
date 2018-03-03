from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3130   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3130.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Father Vixen',                         # 9
        'Sister Kiera',                         # 10
        'Lane',                                 # 11
        'Ada',                                  # 12
        'Factory Chief Murdock',                # 13
        'Target Camera',                        # 14
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
        'ED6_DT07/CH01400 ._CH',             # 00
        'ED6_DT07/CH01410 ._CH',             # 01
        'ED6_DT07/CH01450 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH02620 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01400P._CP',             # 00
        'ED6_DT07/CH01410P._CP',             # 01
        'ED6_DT07/CH01450P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH02620P._CP',             # 04
    )

    DeclNpc(
        X                   = 59010,
        Z                   = 1000,
        Y                   = 52150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 56310,
        Z                   = 1000,
        Y                   = 50360,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 63750,
        Z                   = 0,
        Y                   = 45060,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 59010,
        Z                   = 1000,
        Y                   = 50160,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 59000,
        Z                   = 0,
        Y                   = 47000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        TriggerX            = 58950,
        TriggerZ            = 1000,
        TriggerY            = 50290,
        TriggerRange        = 400,
        ActorX              = 58800,
        ActorZ              = 2500,
        ActorY              = 52200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1B6",          # 00, 0
        "Function_1_1F1",          # 01, 1
        "Function_2_1F2",          # 02, 2
        "Function_3_1F7",          # 03, 3
        "Function_4_471",          # 04, 4
        "Function_5_65B",          # 05, 5
        "Function_6_8C0",          # 06, 6
        "Function_7_A65",          # 07, 7
    )


    def Function_0_1B6(): pass

    label("Function_0_1B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D1")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)

    label("loc_1D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1F0")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_1F0")

    Return()

    # Function_0_1B6 end

    def Function_1_1F1(): pass

    label("Function_1_1F1")

    Return()

    # Function_1_1F1 end

    def Function_2_1F2(): pass

    label("Function_2_1F2")

    Call(0, 3)
    Return()

    # Function_2_1F2 end

    def Function_3_1F7(): pass

    label("Function_3_1F7")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_46D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 7)), scpexpr(EXPR_END)), "loc_2DD")

    ChrTalk(    #0
        0x10,
        (
            "Only a select few people know about Kilika\x01",
            "leaving. She hasn't told all that many yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "I can't help but wonder whether she intends\x01",
            "to keep it that way and depart without telling\x01",
            "the townsfolk, too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46D")

    label("loc_2DD")


    ChrTalk(    #2
        0x10,
        "Oh, if it isn't Agate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "...Have you already heard about Kilika\x01",
            "returning to Calvard?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F1, 0)), scpexpr(EXPR_END)), "loc_37A")

    ChrTalk(    #4
        0x106,
        "#050FYeah. Was talking to her about it earlier.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B8")

    label("loc_37A")


    ChrTalk(    #5
        0x106,
        (
            "#050FYeah...\x02\x03",

            "Jean was the one who told me back in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B8")


    ChrTalk(    #6
        0x10,
        "I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        (
            "All of us in Zeiss owe some kind of debt to her,\x01",
            "big or small.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "So I just hope that we can all come together to\x01",
            "do something for her before she leaves us.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F87)

    label("loc_46D")

    TalkEnd(0x10)
    Return()

    # Function_3_1F7 end

    def Function_4_471(): pass

    label("Function_4_471")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_657")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_55C")
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Sleep(500)

    ChrTalk(    #9
        0xFE,
        (
            "It's a difficult call to make, but I think it would\x01",
            "be best to keep this from the factory chief for\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "I don't think we would be doing him any favors\x01",
            "by telling him now...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_657")

    label("loc_55C")


    ChrTalk(    #11
        0xFE,
        (
            "I don't think I was supposed to hear about her\x01",
            "departure, but I accidentally did when she was\x01",
            "talking to Father Vixen yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "It's hard to believe that she's going to be leaving\x01",
            "us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "Zeiss isn't going to be the same without her.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_657")

    TalkEnd(0xFE)
    Return()

    # Function_4_471 end

    def Function_5_65B(): pass

    label("Function_5_65B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_8BC")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_67A"),
        (1, "loc_72D"),
        (2, "loc_83B"),
        (SWITCH_DEFAULT, "loc_8BC"),
    )


    label("loc_67A")


    ChrTalk(    #14
        0x14,
        (
            "#803FOh, Aidios above...\x02\x03",

            "The time has finally come for the Orbal Gear\x01",
            "experiments to begin...\x02\x03",

            "Please let them finish without causing any\x01",
            "major catastrophes...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8BC")

    label("loc_72D")


    ChrTalk(    #15
        0x14,
        (
            "#803FO-Oh, and one more thing...\x02\x03",

            "Professor Russell seems to be in contact with\x01",
            "an acquaintance of his over in Leman State.\x02\x03",

            "A-And he seems to be intent on visiting them\x01",
            "at some point, too...\x02\x03",

            "#805FI-I hope he doesn't go and cause any more \x01",
            "trouble...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8BC")

    label("loc_83B")


    def lambda_841():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_841)
    Sleep(1000)

    ChrTalk(    #16
        0x14,
        (
            "#803FOh, Aidios... Oh, Kilika... Please protect all of\x01",
            "us in Zeiss from harm...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8BC")

    label("loc_8BC")

    TalkEnd(0xFE)
    Return()

    # Function_5_65B end

    def Function_6_8C0(): pass

    label("Function_6_8C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_A61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_965")

    ChrTalk(    #17
        0xFE,
        (
            "Factory Chief Murdock has been coming here\x01",
            "to pray an awful lot lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Haha. I wonder what suddenly turned him into\x01",
            "such a pious man?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A61")

    label("loc_965")


    ChrTalk(    #19
        0xFE,
        (
            "Whew... I think that'll do for today's afternoon\x01",
            "prayers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I'd normally feel bad about skipping work to\x01",
            "come here and pray...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "...but considering the factory chief is right here,\x01",
            "I think I can probably be let off for it today...\x01",
            "Right?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_A61")

    TalkEnd(0xFE)
    Return()

    # Function_6_8C0 end

    def Function_7_A65(): pass

    label("Function_7_A65")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(59900, 0, 49800, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 59000, 0, 47000, 0)
    OP_4A(0x14, 0)
    SetChrPos(0x107, 59000, 0, 37520, 0)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_AEA():
        OP_6D(59900, 0, 44300, 6000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_AEA)

    def lambda_B02():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_B02)
    FadeToBright(2000, 0)
    Sleep(4500)
    OP_22(0x6, 0x0, 0x64)

    def lambda_B25():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_B25)

    def lambda_B37():
        OP_8E(0xFE, 0xE678, 0x0, 0xA988, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_B37)
    Sleep(800)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x107, 0x1)
    OP_62(0x107, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #22
        0x107,
        "#061F#12PFound you, Mr. Murdock!\x02",
    )

    CloseMessageWindow()

    def lambda_B9E():
        OP_6D(60340, 0, 47520, 1300)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_B9E)

    def lambda_BB6():
        OP_67(0, 5040, -10000, 1300)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_BB6)

    def lambda_BCE():
        OP_8E(0xFE, 0xE678, 0x0, 0xB1BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_BCE)
    WaitChrThread(0x107, 0x1)
    Sleep(300)
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #23
        0x107,
        "#064F#12P...Mr. Murdock?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x14,
        "#803F#5POh, Aidios above... Please protect us all...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x14, 180, 500)
    Sleep(300)

    ChrTalk(    #25
        0x14,
        (
            "#802F#5PHmm? Hello again, Tita... Can I help you with\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #26
        0x14,
        (
            "#805F#5PW-Wait. You aren't here to tell me that the\x01",
            "experiment was a failure and the building is\x01",
            "now full of poisonous gases, are you?!\x02\x03",

            "Or that there was a giant explosion and half\x01",
            "of it was destroyed?! Or... Or...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x107,
        (
            "#561F#12PI'm so sorry...\x02\x03",

            "I really can't apologize enough for all the stress\x01",
            "Mom and Grandpa cause you...\x02\x03",

            "#560FNothing like that's happened yet, though,\x01",
            "so don't worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x14,
        (
            "#802F#5PR-Really? #803FWhew... That's a relief...\x02\x03",

            "Maybe that's a sign my prayers reached the\x01",
            "Goddess after all...\x02\x03",

            "#806FPerhaps I should say my prayers for tomorrow\x01",
            "while I'm here, too, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14, 0, 500)
    Sleep(500)
    OP_62(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_62(0x107, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #29
        0x107,
        (
            "#560F#12PUmm... That said...\x02\x03",

            "...I do have a little favor to ask of you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14)
    Sleep(300)
    OP_62(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x14, 180, 500)
    Sleep(300)

    ChrTalk(    #30
        0x14,
        "#802F#5PWhat kind of favor?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #31
        (
            "\x07\x05Tita passed on what her mother had told her and asked if Murdock could sort\x01",
            "out the necessary paperwork.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #32
        0x14,
        (
            "#801F#5PThey arrived by air, did they?\x02\x03",

            "I can only imagine how surprised you must\x01",
            "have been...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x14)
    Sleep(500)

    ChrTalk(    #33
        0x14,
        "#802F#3S#5PTh-They entered the country illegally?!\x02",
    )

    Sleep(50)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #34
        0x107,
        "#064F#12PIt sounds that way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x14,
        (
            "#806F#5POh, no... I need to go and sort that out right\x01",
            "away!\x02\x03",

            "#800FCould you stay and pray to Aidios in my place,\x01",
            "Tita?\x02\x03",

            "Please, just pray that nothing gets destroyed\x01",
            "because of that new invention of theirs and it\x01",
            "all goes to plan!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x107,
        "#065F#12POkay! I will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x14,
        "#800F#5PTh-Thank you!\x02",
    )

    CloseMessageWindow()

    def lambda_12D3():

        label("loc_12D3")

        TurnDirection(0xFE, 0x14, 500)
        OP_48()
        Jump("loc_12D3")

    QueueWorkItem2(0x107, 2, lambda_12D3)
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x14, 135, 500)

    def lambda_12FD():
        OP_8E(0xFE, 0xEA60, 0x0, 0xB3B0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_12FD)
    WaitChrThread(0x14, 0x1)

    def lambda_131D():
        OP_8E(0xFE, 0xEA60, 0x0, 0x927C, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_131D)
    WaitChrThread(0x14, 0x1)
    Sleep(1000)

    ChrTalk(    #38
        0x107,
        "#062F#5PPhew...\x02",
    )

    CloseMessageWindow()
    OP_44(0x107, 0x2)
    OP_8C(0x107, 0, 500)
    Sleep(300)
    OP_8E(0x107, 0xE678, 0x0, 0xB6D0, 0x4B0, 0x0)
    Sleep(1000)

    ChrTalk(    #39
        0x107,
        (
            "#563F#12P(Please keep Mom and Grandpa from doing\x01",
            "anything too reckless...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #40
        0x107,
        (
            "#063F#12P(...I wish I knew what I could do, though.)\x02\x03",

            "(I'm not strong like Estelle...)\x02\x03",

            "(I couldn't say anything to Renne like she did.)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x107, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #41
        0x107,
        (
            "#064F#12P(I-I know!)\x02\x03",

            "#062F(I'll get them to let me help with the Orbal\x01",
            "Gear's development!)\x02\x03",

            "(If it really does end up having the same\x01",
            "amount of power as Pater-Mater...)\x02\x03",

            "(...maybe then I'll finally be able to have\x01",
            "a proper conversation with her.)\x02\x03",

            "(Time to go and ask!)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 180, 600)

    def lambda_15B5():
        OP_8E(0xFE, 0xE678, 0x0, 0x93F8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_15B5)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3116   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_A65 end

    SaveToFile()

Try(main)
