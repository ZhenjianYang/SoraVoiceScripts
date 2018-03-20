from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'U7001_5 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0303.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_B1",           # 03, 3
        "Function_4_21D",          # 04, 4
        "Function_5_936",          # 05, 5
        "Function_6_12DC",         # 06, 6
        "Function_7_20B6",         # 07, 7
        "Function_8_231C",         # 08, 8
        "Function_9_42FA",         # 09, 9
        "Function_10_4A88",        # 0A, 10
        "Function_11_5595",        # 0B, 11
        "Function_12_6EA6",        # 0C, 12
        "Function_13_72F4",        # 0D, 13
        "Function_14_75B8",        # 0E, 14
        "Function_15_7735",        # 0F, 15
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    Call(5, 3)
    Return()

    # Function_2_AC end

    def Function_3_B1(): pass

    label("Function_3_B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_13B")
    SetChrFlags(0x11, 0x10)
    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_117")

    ChrTalk(    #0
        0x11,
        "#1065FZzz... Zzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10F,
        "#1448F(He seems to be sleeping soundly...)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_130")

    label("loc_117")


    ChrTalk(    #2
        0x11,
        "#1065FZzz... Zzz...\x02",
    )

    CloseMessageWindow()

    label("loc_130")

    ClearChrFlags(0x11, 0x10)
    TalkEnd(0x11)
    Jump("loc_21C")

    label("loc_13B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_1C8")
    SetChrFlags(0x11, 0x10)
    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B0")

    ChrTalk(    #3
        0x11,
        "#40W...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#1000FHe looks a lot better compared to before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10F,
        "#1447F...Indeed.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1BD")

    label("loc_1B0")


    ChrTalk(    #6
        0x11,
        "#40W...\x02",
    )

    CloseMessageWindow()

    label("loc_1BD")

    ClearChrFlags(0x11, 0x10)
    TalkEnd(0x11)
    Jump("loc_21C")

    label("loc_1C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_21C")
    SetChrFlags(0x11, 0x10)
    TalkBegin(0x11)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05Kevin appears to be asleep.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #8
        0x10F,
        "#1445F...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    TalkEnd(0x11)

    label("loc_21C")

    Return()

    # Function_3_B1 end

    def Function_4_21D(): pass

    label("Function_4_21D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_3BE")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_366")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A3")

    ChrTalk(    #9
        0x12,
        "#1446FDo you require something from me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x109,
        (
            "#1067FN-No...\x02\x03",

            "#1077FNothing in particular.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_360")

    label("loc_2A3")


    ChrTalk(    #11
        0x12,
        (
            "#1805F(I finally managed to get into the Gralsritter,\x01",
            "I went through all that training...)\x02\x03",

            "(...I was finally promoted to a squire...)\x02\x03",

            "#1445F(...but after all that...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x109,
        "#1067F...\x02",
    )

    CloseMessageWindow()

    label("loc_360")

    OP_A2(0x1)
    Jump("loc_3B3")

    label("loc_366")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A4")

    ChrTalk(    #13
        0x12,
        "#1446FDo you require something from me?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B3")

    label("loc_3A4")


    ChrTalk(    #14
        0x12,
        "#1445F...\x02",
    )

    CloseMessageWindow()

    label("loc_3B3")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_935")

    label("loc_3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_78C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_400")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #15
        0x12,
        "#1445F...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_789")

    label("loc_400")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_623")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #16
        0x12,
        (
            "#1446FKevin's always been like that. Even now, nothing\x01",
            "has changed.\x02\x03",

            "He's selfish, he's arrogant, he's self-centered...\x02\x03",

            "#1443FHe also needs to act like he can handle everything\x01",
            "by himself at all times. He's just a sorry excuse for\x01",
            "a human being.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_597")

    ChrTalk(    #17
        0x103,
        (
            "#1523FSo this is the famous sister, huh?\x02\x03",

            "#1522FShe seems kind of...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x109, 400)

    ChrTalk(    #18
        0x103,
        "#1527F...mad at you, though, Kevin?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DC")

    label("loc_597")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5DC")

    ChrTalk(    #19
        0x10A,
        "#811F(She's super cute when she's angry, too. ㈱)\x02",
    )

    CloseMessageWindow()

    label("loc_5DC")


    ChrTalk(    #20
        0x109,
        "#1068F(Oh, boy... I think I'd better make my exit.)\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x1)
    TalkEnd(0xFE)
    Jump("loc_789")

    label("loc_623")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #21
        0x12,
        (
            "#1446FKevin's always been like that. Even now, nothing\x01",
            "has changed.\x02\x03",

            "He's selfish, he's arrogant, he's self-centered...\x02\x03",

            "#1443FHe also needs to act like he can handle everything\x01",
            "by himself at all times. He's just a sorry excuse for\x01",
            "a human being.\x02\x03",

            "#1805F...And since you're so rudely eavesdropping,\x01",
            "I don't want to talk to you. Go away.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_789")

    Jump("loc_935")

    label("loc_78C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_7B5")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #22
        0x12,
        "#1445F...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_935")

    label("loc_7B5")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AE")

    ChrTalk(    #23
        0x12,
        (
            "#1446FIf you want to keep lying to yourself, Kevin,\x01",
            "then go right ahead.\x02\x03",

            "If that's what makes you happy, I won't stop\x01",
            "you.\x02\x03",

            "#1445FBut...\x02\x03",

            "#1446F...as long as you keep doing so, I don't want\x01",
            "to talk to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        "#1067F...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2634)
    Jump("loc_92D")

    label("loc_8AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90D")

    ChrTalk(    #25
        0x12,
        (
            "#1446F...\x02\x03",

            "Leave me alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        "#1068F(Damn. She's really mad this time...)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_92D")

    label("loc_90D")


    ChrTalk(    #27
        0x12,
        (
            "#1446F...\x02\x03",

            "Leave me alone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92D")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_935")

    Return()

    # Function_4_21D end

    def Function_5_936(): pass

    label("Function_5_936")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_B44")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5B")

    ChrTalk(    #28
        0x10,
        (
            "#1505FI tried asking Celeste a few questions regarding\x01",
            "the Liber Ark...\x02\x03",

            "#1503F...but she doesn't possess most of the real\x01",
            "Celeste's memories regarding the city.\x02\x03",

            "#1503FI can only assume she was given the bare minimum\x01",
            "of information regarding it and nothing more.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_B3E")

    label("loc_A5B")


    ChrTalk(    #29
        0x10,
        (
            "#1505FFrom what I can tell, Celeste was only given the\x01",
            "bare minimum of information and nothing more.\x02\x03",

            "#1503FI suppose that makes sense when you consider\x01",
            "how anything she knew may have ended up being\x01",
            "leaked to the Aureole.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3E")

    TalkEnd(0xFE)
    Jump("loc_12DB")

    label("loc_B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_D9A")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD0")

    ChrTalk(    #30
        0x10,
        (
            "#1503FRichard's circumstances are notably different\x01",
            "from the rest of us who ended up here.\x02\x03",

            "There's got to be some kind of underlying reason\x01",
            "why that was the case... It can't just be random.\x02\x03",

            "#1505FIf we can work that out, I have this feeling we'll\x01",
            "be able to get significantly closer to knowing just\x01",
            "how this world works.\x02\x03",

            "It's just a case of connecting the dots...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_D94")

    label("loc_CD0")


    ChrTalk(    #31
        0x10,
        (
            "#1505FI have a feeling that if we work out why Richard\x01",
            "arrived here how he did, we'll be able to get \x01",
            "closer to knowing just how this world works.\x02\x03",

            "It's just a case of connecting the dots...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D94")

    TalkEnd(0xFE)
    Jump("loc_12DB")

    label("loc_D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_12DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_115D")
    TalkBegin(0xFE)

    ChrTalk(    #32
        0x101,
        "#1000FHow is he, Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        (
            "#1500FGenerally fine. He's in a deep sleep right now.\x02\x03",

            "#1503FHe has been groaning every so often, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#1004FWhat, really? That doesn't sound good...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10F,
        "#1802F...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FA5")

    ChrTalk(    #36
        0x10,
        (
            "#1503FAll we can do is let him rest.\x02\x03",

            "#1505FIt's going to take some time for him to recover--\x01",
            "the mental burden he's carrying is just as taxing\x01",
            "on his body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1003FOh, for sure...\x02\x03",

            "#1002FWell, keep an eye on him, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10F,
        "#1446FThank you, Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        "#1501FOf course.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1154")

    label("loc_FA5")

    OP_4A(0x17, 255)
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x17, 0x0, 0)

    ChrTalk(    #40
        0x17,
        (
            "#1165FDon't worry.\x02\x03",

            "The only real symptom he's showing is a\x01",
            "light fever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        (
            "#1503FAll we can do is let him rest.\x02\x03",

            "#1505FIt's going to take some time for him to recover--\x01",
            "the mental burden he's carrying is just as taxing\x01",
            "on his body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1003FOh, for sure...\x02\x03",

            "#1002FWell, keep an eye on him, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10F,
        "#1446FThank you, Kloe. Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x17,
        "#1167FNo problem, Ries.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        "#1501FLeave it to us.\x02",
    )

    CloseMessageWindow()
    OP_4B(0x17, 255)
    OP_51(0x17, 0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1154")

    TalkEnd(0xFE)
    OP_A2(0x2659)
    Jump("loc_12DB")

    label("loc_115D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_122F")
    OP_A2(0x3)

    ChrTalk(    #46
        0x10,
        (
            "#1505FIt's generally not a good idea to rush the recovery\x01",
            "process of mental strain using medicines. It's best\x01",
            "to let them heal on their own.\x02\x03",

            "#1500FLet's make sure he gets plenty of rest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D8")

    label("loc_122F")


    ChrTalk(    #47
        0x10,
        (
            "#1503FThe cause of this is a mental burden that's\x01",
            "affecting his body, so I think the best thing\x01",
            "to do is just to let him rest for now.\x02\x03",

            "It's all we CAN do, really.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D8")

    TalkEnd(0xFE)

    label("loc_12DB")

    Return()

    # Function_5_936 end

    def Function_6_12DC(): pass

    label("Function_6_12DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_1759")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1373")
    Jump("loc_13B5")

    label("loc_1373")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_138F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13B5")

    label("loc_138F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13AB")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13B5")

    label("loc_13AB")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13B5")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B2")

    ChrTalk(    #48
        0x1C,
        (
            "#1527FThere's no point in rushing things.\x02\x03",

            "#1535FWe've got a good idea what the rest of the\x01",
            "sixth plane is going to be like now, so slow\x01",
            "but sure seems the best way forward to me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1551")

    ChrTalk(    #49
        0x109,
        (
            "#1068FWell, you might be right...\x02\x03",

            "#1840F...but I think sitting around drinking is probably\x01",
            "being a bit TOO relaxed... Then again, it works\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1690")

    label("loc_1551")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1589")

    ChrTalk(    #50
        0x102,
        "#1508FWell, you might be right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_15B0")

    label("loc_1589")


    ChrTalk(    #51
        0x109,
        "#1840FWell, you might be right...\x02",
    )

    CloseMessageWindow()

    label("loc_15B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1619")

    ChrTalk(    #52
        0x101,
        (
            "#1019F...but I'm not sure how I feel about you getting\x01",
            "plastered while we're here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1690")

    label("loc_1619")


    ChrTalk(    #53
        0x109,
        (
            "#1066F...but I think sitting around drinking is probably\x01",
            "being a bit TOO relaxed... Then again, it works\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1690")

    OP_62(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_A2(0x5)
    Jump("loc_174E")

    label("loc_16B2")


    ChrTalk(    #54
        0x1C,
        (
            "#1520FWe've got a pretty good idea what the rest of the \x01",
            "sixth plane is going to be like now.\x02\x03",

            "#1535FSo let's take it slow and steady from here, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_174E")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_20B5")

    label("loc_1759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_1D1C")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BAA")

    ChrTalk(    #55
        0x1C,
        (
            "#1526FI understood the gist of what Celeste was\x01",
            "saying...\x02\x03",

            "#1522F...but that doesn't really explain why there\x01",
            "are all these books here.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1C, 47, 400)
    Sleep(300)

    ChrTalk(    #56
        0x1C,
        (
            "#1532FEspecially so many of them. Something's not\x01",
            "clicking with me.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #57
        0x1C,
        "#1523FOh, look at this weird one!\x02",
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (8, "loc_18D9"),
        (14, "loc_190D"),
        (0, "loc_191F"),
        (1, "loc_1939"),
        (4, "loc_194D"),
        (6, "loc_1974"),
        (5, "loc_199A"),
        (7, "loc_19AB"),
        (3, "loc_19C9"),
        (10, "loc_19EF"),
        (9, "loc_1A18"),
        (13, "loc_1A37"),
        (12, "loc_1A69"),
        (11, "loc_1A7A"),
        (15, "loc_1A8B"),
        (SWITCH_DEFAULT, "loc_1AC1"),
    )


    label("loc_18D9")


    ChrTalk(    #58
        0x109,
        (
            "#1064FWeird one?\x02\x03",

            "#1063FWh-What's it called?\x02",
        )
    )

    Jump("loc_1AC1")

    label("loc_190D")


    ChrTalk(    #59
        0x10F,
        "#1444F...?\x02",
    )

    Jump("loc_1AC1")

    label("loc_191F")


    ChrTalk(    #60
        0x101,
        "#1004FA weird one?\x02",
    )

    Jump("loc_1AC1")

    label("loc_1939")


    ChrTalk(    #61
        0x102,
        "#1504FUmm...\x02",
    )

    Jump("loc_1AC1")

    label("loc_194D")


    ChrTalk(    #62
        0x105,
        (
            "#1164FUmm...\x02\x03",

            "What's it called?\x02",
        )
    )

    Jump("loc_1AC1")

    label("loc_1974")


    ChrTalk(    #63
        0x107,
        (
            "#064FUmm...\x02\x03",

            "What's it called?\x02",
        )
    )

    Jump("loc_1AC1")

    label("loc_199A")


    ChrTalk(    #64
        0x106,
        "#555FHuh?\x02",
    )

    Jump("loc_1AC1")

    label("loc_19AB")


    ChrTalk(    #65
        0x108,
        "#073FWhat's it called?\x02",
    )

    Jump("loc_1AC1")

    label("loc_19C9")


    ChrTalk(    #66
        0x104,
        (
            "#1543FOh?\x02\x03",

            "#1542FTell me more.\x02",
        )
    )

    Jump("loc_1AC1")

    label("loc_19EF")


    ChrTalk(    #67
        0x10B,
        (
            "#213FHuh?\x02\x03",

            "#216FWhat's it called?\x02",
        )
    )

    Jump("loc_1AC1")

    label("loc_1A18")


    ChrTalk(    #68
        0x10A,
        (
            "#814FHuh?\x02\x03",

            "A weird one?\x02",
        )
    )

    Jump("loc_1AC1")

    label("loc_1A37")


    ChrTalk(    #69
        0x10E,
        (
            "#172FA weird one?\x02\x03",

            "#178FWhat is it called?\x02",
        )
    )

    Jump("loc_1AC1")

    label("loc_1A69")


    ChrTalk(    #70
        0x10D,
        "#270FHmm?\x02",
    )

    Jump("loc_1AC1")

    label("loc_1A7A")


    ChrTalk(    #71
        0x10C,
        "#113FHmm?\x02",
    )

    Jump("loc_1AC1")

    label("loc_1A8B")


    ChrTalk(    #72
        0x110,
        (
            "#264FOh?\x02\x03",

            "#261FHeehee. Let me see, let me see!\x02",
        )
    )

    Jump("loc_1AC1")

    label("loc_1AC1")

    CloseMessageWindow()

    ChrTalk(    #73
        0x1C,
        (
            "#1526F#60W'From Fat to Fit!!'#1200W…#20W\x01",
            "By Gilbert Stein.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x29, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #74
        0x1C,
        "#1525FTh-These bookcases really are weird...\x02",
    )

    CloseMessageWindow()
    OP_65(0x1, 0x1)
    OP_A2(0x265F)
    Jump("loc_1D16")

    label("loc_1BAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C92")

    ChrTalk(    #75
        0x1C,
        (
            "#1532FWhy're there so many books here, anyway?\x02\x03",

            "A good chunk of them are so weird, too...\x02\x03",

            "#1525FThe more time I spend here, the more\x01",
            "it feels like this couldn't be a collection\x01",
            "someone had put together manually.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1D16")

    label("loc_1C92")


    ChrTalk(    #76
        0x1C,
        (
            "#1532FWhy're there so many books here, anyway?\x02\x03",

            "At the very least, I can't imagine Celeste\x01",
            "brought them all in here herself...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D16")

    TalkEnd(0xFE)
    Jump("loc_20B5")

    label("loc_1D1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_1E2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC0")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #77
        0x1C,
        (
            "#1526FHe seems to be doing fine now.\x02\x03",

            "Fortunately for us, he's one tough cookie,\x01",
            "so he should be up and about in no time.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x5)
    TalkEnd(0xFE)
    Jump("loc_1E2B")

    label("loc_1DC0")

    TalkBegin(0xFE)

    ChrTalk(    #78
        0x1C,
        (
            "#1520FDon't you worry, mm'kay? He'll be fine.\x02\x03",

            "#1535FI can promise you that he's in good hands.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_1E2B")

    Jump("loc_20B5")

    label("loc_1E2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_20B5")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EAC")

    ChrTalk(    #79
        0x1C,
        "#1520FSo you and Kevin grew up together, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x12,
        "#1802FY-Yes, that's right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F9B")

    label("loc_1EAC")


    ChrTalk(    #81
        0x1C,
        (
            "#1525FUnbelievable...\x02\x03",

            "#1522FIs that REALLY the way you want to make\x01",
            "your first impression on someone? And from\x01",
            "the church, no less.\x02\x03",

            "At least play her a hymn or something!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x102,
        "#1504FI'm not sure his choice of song is the problem...\x02",
    )

    CloseMessageWindow()

    label("loc_1F9B")

    OP_A2(0x5)
    Jump("loc_20AD")

    label("loc_1FA1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2044")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #83
        0x1C,
        (
            "#1526FThis isn't the first time I've met a sister\x01",
            "who's a bit...uh...unique.\x02\x03",

            "#1522FBut this one definitely fits the bill, all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20AD")

    label("loc_2044")


    ChrTalk(    #84
        0x1C,
        (
            "#1525FYou're dealing with someone from the church,\x01",
            "here. I'm not sure love songs are...appropriate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20AD")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_20B5")

    Return()

    # Function_6_12DC end

    def Function_7_20B6(): pass

    label("Function_7_20B6")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_221E")
    Sleep(500)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x49), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0x1F4)
    OP_21()
    OP_1D(0x0)

    ChrTalk(    #898
        0x19,
        "#1545Fこのボクの独奏会にようこそ！\x02\x03",
    )

    CloseMessageWindow()

    ChrTalk(    #899
        0x19,
        "#1540F#30Aさぁ！華麗なショータイムの始まりさ♪\x02",
    )

    CloseMessageWindow()
    Sleep(2500)
    TalkEnd(0xFE)
    EventBegin(0x1)

    ChrTalk(    #900 op#A op#5
        0x19,
        "#1545F20A#0W...\x05\x02",
    )

    OP_4B(0x12, 255)
    CloseMessageWindow()
    Sleep(5770)

    ChrTalk(    #901 op#A op#5
        0x19,
        (
            "#100A#0WBrightly shooting stars,\x01",
            "leaving trails in the skies...\x05\x02",
        )
    )

    Sleep(6600)

    ChrTalk(    #902 op#A op#5
        0x19,
        (
            "#100A#0WLike a guiding light, they show\x01",
            "me the way to your eyes...\x05\x02",
        )
    )

    Sleep(6200)

    ChrTalk(    #903 op#A op#5
        0x19,
        (
            "#100A#0WThis yearning passion,\x01",
            "tears my heart in twain...\x05\x02",
        )
    )

    Sleep(5600)

    ChrTalk(    #904 op#A op#5
        0x19,
        (
            "#100A#0WAnd the cruel moon mocks\x01",
            "my pain...\x05\x02",
        )
    )

    Sleep(7000)

    ChrTalk(    #905 op#A op#5
        0x19,
        (
            "#100A#0WIf this fleeting dream shall\x01",
            "never be...\x05\x02",
        )
    )

    Sleep(7000)

    ChrTalk(    #906 op#A op#5
        0x19,
        (
            "#100A#0WA single wound will remain in\x01",
            "my heart for all to see...\x05\x02",
        )
    )

    Sleep(9500)

    ChrTalk(    #907 op#A op#5
        0x19,
        (
            "#100A#0WOur passionate first and final\x01",
            "kiss...\x05\x02",
        )
    )

    Sleep(8500)

    ChrTalk(    #908 op#A op#5
        0x19,
        (
            "#100A#0WYour tears to me are an\x01",
            "amber bliss...\x05\x02",
        )
    )

    Sleep(8800)

    ChrTalk(    #909 op#A op#5
        0x19,
        "#100A#0WLet us immure this eternal love...\x05\x02",
    )

    Sleep(10800)

    CloseMessageWindow()
    Sleep(5500)
    EventEnd(0x1)
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21A4")

    ChrTalk(    #86
        0x10B,
        "#216FHe was serious...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2218")

    label("loc_21A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21F2")

    ChrTalk(    #87
        0x103,
        "#1525F*sigh* I can't believe he was actually serious...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2218")

    label("loc_21F2")


    ChrTalk(    #88
        0x102,
        "#1505FHe was actually serious...\x02",
    )

    CloseMessageWindow()

    label("loc_2218")

    OP_A2(0x6)
    Jump("loc_2313")

    label("loc_221E")


    ChrTalk(    #89 op#A op#5
        0x19,
        (
            "#1545F#70W#20AIf this wish is doomed to fade... \x01",
            "without ever coming true...\x01\x05\x02",

            "Then may it leave at least a scar...\x05\x02\x03",

            "My first promise is one I cannot keep...\x01\x05\x02",

            "I keep your breath encased in amber...\x01\x05\x02",

            "Sealing within this eternal dream...\x05\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2313")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Return()

    # Function_7_20B6 end

    def Function_8_231C(): pass

    label("Function_8_231C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_27F2")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2534")

    ChrTalk(    #90
        0x17,
        (
            "#1167FThis world may have been created by the Aureole...\x02\x03",

            "#1169F...but it seems it did so without the knowledge of\x01",
            "those who lived on the Liber Ark and relied on its\x01",
            "power to live.\x02\x03",

            "#1162FThey entrusted all of the city's control and\x01",
            "governance to the Aureole, believing that it \x01",
            "would make the city into an actual paradise.\x02\x03",

            "Instead, it betrayed the expectations of those\x01",
            "who actually made the city, creating another\x01",
            "world entirely.\x02\x03",

            "#1169FI wonder if that's what the people of the Liber\x01",
            "Ark really wanted?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_27EC")

    label("loc_2534")


    ChrTalk(    #91
        0x17,
        (
            "#1167F*sigh* I want to look into this more, but it's\x01",
            "proving more than a little difficult.\x02\x03",

            "#1165FThe accounts from people at the time are so\x01",
            "fragmentary that decoding and putting\x01",
            "everything together is quite time consuming.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2669")

    ChrTalk(    #92
        0x101,
        (
            "#1015FDon't go so nuts that you burn yourself out,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27EC")

    label("loc_2669")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26B0")

    ChrTalk(    #93
        0x102,
        "#1501FYou might want to get some rest, you know.\x02",
    )

    CloseMessageWindow()
    Jump("loc_27EC")

    label("loc_26B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2708")

    ChrTalk(    #94
        0x10E,
        (
            "#176FPlease get some rest if you feel you need it,\x01",
            "Your Highness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27EC")

    label("loc_2708")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27C0")

    ChrTalk(    #95
        0x10B,
        (
            "#215FU-Umm... You sure you don't need some R&R?\x02\x03",

            "#210FWe might need you to come fight with us at\x01",
            "some point, and you're not gonna be able to\x01",
            "if you're exhausted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27EC")

    label("loc_27C0")


    ChrTalk(    #96
        0x109,
        "#1066FHaha. Go easy on yourself, okay?\x02",
    )

    CloseMessageWindow()

    label("loc_27EC")

    TalkEnd(0xFE)
    Jump("loc_42F9")

    label("loc_27F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_2AC6")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_295F")

    ChrTalk(    #97
        0x17,
        (
            "#1160FI decided to ask Celeste about this library\x01",
            "a short while ago...\x02\x03",

            "She says this world is capable of absorbing\x01",
            "information spaces into itself.\x02\x03",

            "#1383FThe books we see come from the knowledge\x01",
            "accumulated within being drawn out through\x01",
            "our thoughts and existence.\x02\x03",

            "#1382FThat was what she told me, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x109,
        "#1066FUh... Uh-huh.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_2AC0")

    label("loc_295F")


    ChrTalk(    #99
        0x17,
        (
            "#1167FPerhaps the doors scatted throughout Phantasma\x01",
            "appeared as a result of the same mechanism.\x02\x03",

            "The books in this library are the result of\x01",
            "information spaces being made manifest by our\x01",
            "thoughts and existence.\x02\x03",

            "#1160FI can only assume this area was one of the things\x01",
            "left as is when the Lord of Phantasma remade this\x01",
            "world into its current form.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AC0")

    TalkEnd(0xFE)
    Jump("loc_42F9")

    label("loc_2AC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_379D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35F1")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x17, 0x0, 400)
    Sleep(300)

    ChrTalk(    #100
        0x17,
        "#1164FHi there.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B82")

    ChrTalk(    #101
        0x102,
        (
            "#1500FHey, Kloe. Are you gathering information here?\x02\x03",

            "#1501FFind anything of interest?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7F")

    label("loc_2B82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BF7")

    ChrTalk(    #102
        0x101,
        (
            "#1011FOh, are you looking for useful info in all these\x01",
            "books, Kloe?\x02\x03",

            "#1006FFind anything cool?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7F")

    label("loc_2BF7")


    ChrTalk(    #103
        0x109,
        (
            "#1060FOh, Your Highness. I didn't think we'd find you\x01",
            "still here.\x02\x03",

            "#1066FHave you found anything worthwhile in any of\x01",
            "these books?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C7F")


    ChrTalk(    #104
        0x17,
        (
            "#1165FY-You could say that, yes...\x02\x03",

            "I haven't found anything significant from the \x01",
            "books themselves due to them not being arranged\x01",
            "in any apparent order...\x02\x03",

            "#1160F...but I've discovered that these bookcases seem\x01",
            "to have a few unique rules of their own that need\x01",
            "to be followed to make the most of them.\x02\x03",

            "For one, you can draw the books that you want to\x01",
            "read closer to you rather than being forced to find\x01",
            "them manually.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EFD")

    ChrTalk(    #105
        0x101,
        (
            "#1004FY-You can actually do that? Holy cow...\x02\x03",

            "#1015FAlthough, I guess it makes sense with this world\x01",
            "being what it is.\x02\x03",

            "So, what? You just wish really hard for a book to\x01",
            "appear and it does?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3225")

    label("loc_2EFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FE4")

    ChrTalk(    #106
        0x102,
        (
            "#1504FThat's actually possible?\x02\x03",

            "#1503F...Then again, I shouldn’t really be surprised\x01",
            "with everything else that can be done here.\x02\x03",

            "#1501FDo you simply have to wish strongly enough\x01",
            "for a book to appear, then?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3225")

    label("loc_2FE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_314F")

    ChrTalk(    #107
        0x10E,
        (
            "#173FI had no idea such a thing was possible...\x02\x03",

            "#176FAlthough given what Celeste said about the\x01",
            "nature of this world, I suppose it shouldn't\x01",
            "have been out of the question.\x02\x03",

            "It would explain why these shelves have so\x01",
            "many books entirely out of reach, too.\x02\x03",

            "#170FSo then all you have to do is wish strongly\x01",
            "enough for a book to appear, then?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3225")

    label("loc_314F")


    ChrTalk(    #108
        0x109,
        (
            "#1064FWait. Are you messing with me?\x02\x03",

            "#1068FSheesh... Well, I guess I can't be too surprised.\x01",
            "Feels like just about anything's possible here.\x02\x03",

            "#1066FSo if you just wish for a book to appear near you,\x01",
            "it does?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3225")


    ChrTalk(    #109
        0x17,
        (
            "#1160FNo, it's not quite that simple. Just wishing very\x01",
            "hard isn't enough.\x02\x03",

            "#1165FI'm not sure how to describe it properly, and it's\x01",
            "not like I get how it works, either.\x02\x03",

            "It's like you're...calling out to the bookshelves\x01",
            "themselves, if you will.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33A3")

    ChrTalk(    #110
        0x10E,
        (
            "#173FI-I never would have thought to even try that...\x02\x03",

            "#179FYou've always been rather clever, Your Highness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3576")

    label("loc_33A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3445")

    ChrTalk(    #111
        0x102,
        (
            "#1504FHow on earth were you able to work out\x01",
            "something like that?\x02\x03",

            "#1501FI don't know if I have the confidence to\x01",
            "pull it off, too, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3576")

    label("loc_3445")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34B4")

    ChrTalk(    #112
        0x101,
        (
            "#1007FD-Damn. How'd you even think of that?\x02\x03",

            "It sounds way beyond anything I could do...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3576")

    label("loc_34B4")


    ChrTalk(    #113
        0x109,
        (
            "#1066FO-Oh, right... Trust you to figure that out.\x02\x03",

            "#1068FAaand we'll probably have to leave this to\x01",
            "your expertise, then. Sorry, but it sounds like\x01",
            "too much for me to wrap my head around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3576")


    ChrTalk(    #114
        0x17,
        (
            "#1165FA-Ahaha...\x02\x03",

            "The times I've been able to do it successfully\x01",
            "are few and far between, to be honest.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x265B)
    TalkEnd(0xFE)
    Jump("loc_379A")

    label("loc_35F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36DC")

    ChrTalk(    #115
        0x17,
        (
            "#1160FMaking good use of these bookshelves isn't\x01",
            "quite as simple as just searching for the book\x01",
            "you want.\x02\x03",

            "Still, I see no reason why there wouldn't be\x01",
            "something useful among these.\x02\x03",

            "#1382FSo I'll keep searching.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_3797")

    label("loc_36DC")


    ChrTalk(    #116
        0x17,
        (
            "#1160FMaking good use of these bookshelves isn't\x01",
            "quite as simple as just searching for the book\x01",
            "you want.\x02\x03",

            "Still, I see no reason why there wouldn't be\x01",
            "something useful among these.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3797")

    TalkEnd(0xFE)

    label("loc_379A")

    Jump("loc_42F9")

    label("loc_379D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_3B86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 3)), scpexpr(EXPR_END)), "loc_39FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_395B")
    TalkBegin(0xFE)

    ChrTalk(    #117
        0x17,
        (
            "#1162FHi, everyone. Celeste kindly explained the\x01",
            "situation to me while you were away.\x02\x03",

            "You need my help in order to keep going,\x01",
            "don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x109,
        (
            "#1066FOh, you've been filled in already? Great!\x01",
            "Saves us the time explaining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x17,
        (
            "#1167FI'm ready to leave as soon as you are.\x02\x03",

            "#1162FSo just say the word when you're ready\x01",
            "to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x109,
        (
            "#1075FGot it.\x02\x03",

            "#1060FWe'll head on out as soon as we're\x01",
            "done prepping, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B04)
    TalkEnd(0xFE)
    Jump("loc_39F7")

    label("loc_395B")

    TalkBegin(0xFE)

    ChrTalk(    #121
        0x17,
        (
            "#1167FIf my help is needed in order to advance,\x01",
            "I'll be more than happy to give it.\x02\x03",

            "#1162FSo please, just say the word when you're\x01",
            "ready to go.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_39F7")

    Jump("loc_3B83")

    label("loc_39FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ADA")

    ChrTalk(    #122
        0x17,
        (
            "#1160FIt's almost startling how many books are\x01",
            "here.\x02\x03",

            "#1160FThey don't seem to be arranged in any\x01",
            "specific order, though.\x02\x03",

            "#1167FI want to think that there's more to this\x01",
            "bookcase than meets the eye...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_3B80")

    label("loc_3ADA")


    ChrTalk(    #123
        0x17,
        (
            "#1160FThe books here don't seem to be arranged\x01",
            "in any specific order, which is interesting...\x02\x03",

            "#1167FPerhaps there's more to this bookcase than\x01",
            "meets the eye...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B80")

    TalkEnd(0xFE)

    label("loc_3B83")

    Jump("loc_42F9")

    label("loc_3B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_42F9")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F85")

    ChrTalk(    #124
        0x101,
        "#1000FHow is he, Kloe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x17,
        (
            "#1164FHi there, Estelle.\x02\x03",

            "#1160FHe's doing fine. He's actually sleeping\x01",
            "soundly at the moment.\x02\x03",

            "#1169FHe was groaning a little in his sleep till\x01",
            "a short while ago, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        "#1004FWhat, really? That doesn't sound good...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x10F,
        "#1802F...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E1C")
    OP_4A(0x10, 255)
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x10, 0x0, 0)

    ChrTalk(    #128
        0x10,
        (
            "#1503FAll we can do is let him rest.\x02\x03",

            "#1505FIt's going to take some time for him to recover--\x01",
            "the mental burden he's carrying is just as taxing\x01",
            "on his body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#1003FOh, for sure...\x02\x03",

            "#1002FWell, keep an eye on him, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x10F,
        "#1446FThank you, Kloe. Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x17,
        "#1167FNo problem, Ries.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x10,
        "#1501FLeave it to us.\x02",
    )

    CloseMessageWindow()
    OP_4B(0x10, 255)
    OP_51(0x10, 0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F7F")

    label("loc_3E1C")


    ChrTalk(    #133
        0x17,
        (
            "#1169FWhatever is happening, it's clearly as much\x01",
            "of a mental battle as it is a physical one.\x02\x03",

            "Much like what Joshua experienced with his\x01",
            "own Stigma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x102,
        (
            "#1503FYeah...\x02\x03",

            "Either way, all we can do now is let him rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#1003FOh, for sure...\x02\x03",

            "#1002FCould we ask you to keep an eye on him,\x01",
            "then, Kloe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x10F,
        "#1446FPlease.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x17,
        "#1167FI'd be happy to.\x02",
    )

    CloseMessageWindow()

    label("loc_3F7F")

    OP_A2(0x2659)
    Jump("loc_42F6")

    label("loc_3F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41BE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40F0")

    ChrTalk(    #138
        0x17,
        (
            "#1164FI'm surprised just how capable Josette\x01",
            "actually is.\x02\x03",

            "She's a real natural when it comes to\x01",
            "looking after people.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40C3")

    ChrTalk(    #139
        0x102,
        "#1509FYup. She's way better than Estelle, anyway.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        (
            "#1019FGuh...\x02\x03",

            "#1022FW-Well, I guess that's what happens when\x01",
            "you grow up surrounded with boys!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40ED")

    label("loc_40C3")


    ChrTalk(    #141
        0x101,
        (
            "#1019FIck.\x02\x03",

            "Y-Y-You really think so?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40ED")

    Jump("loc_41B8")

    label("loc_40F0")


    ChrTalk(    #142
        0x17,
        (
            "#1165FTry not to worry about Kevin too much.\x02\x03",

            "I'm used to taking care of people like this.\x01",
            "I'll be able to handle doing it alone.\x02\x03",

            "#1160FInstead, you're better off focusing on\x01",
            "exploring for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41B8")

    OP_A2(0x7)
    Jump("loc_42F6")

    label("loc_41BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_426F")

    ChrTalk(    #143
        0x17,
        (
            "#1160FI'd heard a lot about Josette from Estelle...\x02\x03",

            "#1161F...but I was surprised just how much of a\x01",
            "natural she is when it comes to looking\x01",
            "after people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42F6")

    label("loc_426F")


    ChrTalk(    #144
        0x17,
        (
            "#1160FTry not to worry about Kevin too much.\x02\x03",

            "I'm used to taking care of people like this.\x01",
            "I'll be able to handle doing it alone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42F6")

    TalkEnd(0xFE)

    label("loc_42F9")

    Return()

    # Function_8_231C end

    def Function_9_42FA(): pass

    label("Function_9_42FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_4447")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43CD")

    ChrTalk(    #145
        0x13,
        (
            "#065FI didn't know Kevin was like that when he\x01",
            "was growing up...\x02\x03",

            "#562FThat must have been really tough for you,\x01",
            "Ries...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x109,
        "#1068F(Crap. Sweet Tita's actually buying it all.)\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_443C")

    label("loc_43CD")


    ChrTalk(    #147
        0x13,
        (
            "#065FI-I thought he was a really nice person...\x02\x03",

            "I didn't know he was like that when he\x01",
            "was growing up...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_443C")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_4A87")

    label("loc_4447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_45D5")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4529")

    ChrTalk(    #148
        0x13,
        (
            "#063FSay...Ries? Cheer up, okay?\x02\x03",

            "I... Umm... I can't pretend to know exactly\x01",
            "what you're angry about...\x02\x03",

            "#562F...but I'm sure Kevin really cares about you,\x01",
            "even if he doesn't always show it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_45CA")

    label("loc_4529")


    ChrTalk(    #149
        0x13,
        (
            "#063FI... Umm... I can't pretend to know exactly\x01",
            "what you're angry about...\x02\x03",

            "...but I still think it would be better to try\x01",
            "and make up than staying angry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45CA")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_4A87")

    label("loc_45D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 3)), scpexpr(EXPR_END)), "loc_474A")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46D4")

    ChrTalk(    #150
        0x13,
        (
            "#063FRies had a fight with you, Kevin?\x02\x03",

            "So that's why she looks so down...\x02\x03",

            "#562FIsn't there anything we can do to\x01",
            "make her feel better?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x109,
        (
            "#1068F(Aww, gimme a break, Aidios. As if I didn't\x01",
            "feel guilty enough already.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_473F")

    label("loc_46D4")


    ChrTalk(    #152
        0x13,
        (
            "#063FSo that's why she looks so down...\x02\x03",

            "#562FIsn't there anything we can do to\x01",
            "make her feel better?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_473F")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_4A87")

    label("loc_474A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_END)), "loc_4A87")
    SetChrFlags(0x13, 0x10)
    TalkBegin(0x13)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_476E")
    OP_4A(0x13, 255)
    Jump("loc_4776")

    label("loc_476E")

    OP_4A(0x13, 255)
    OP_4A(0x16, 255)

    label("loc_4776")


    ChrTalk(    #153
        0x13,
        (
            "#063FAre you feeling all right, Ries?\x02\x03",

            "I can go and get you some medicine\x01",
            "if it would help...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4908")

    ChrTalk(    #154
        0x10B,
        "#214FYou big dummy. She's not sick--she's angry!\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x13, 0x10B, 400)

    ChrTalk(    #155
        0x13,
        "#064F...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x10B,
        (
            "#416FCome on! Read between the lines.\x02\x03",

            "That phony priest obviously said something\x01",
            "to make her mad, and this is the result.\x02\x03",

            "#212FYou're better off leaving her alone for now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A26")

    label("loc_4908")


    ChrTalk(    #157
        0x16,
        "#214FYou big dummy. She's not sick--she's angry!\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x13, 0x16, 400)

    ChrTalk(    #158
        0x13,
        "#064F...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x16,
        (
            "#416FCome on! Read between the lines.\x02\x03",

            "That phony priest obviously said something\x01",
            "to make her mad, and this is the result.\x02\x03",

            "#212FYou're better off leaving her alone for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A26")

    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #160
        0x13,
        (
            "#065FUmm...\x02\x03",

            "B-But...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A6D")
    OP_4B(0x13, 255)
    Jump("loc_4A75")

    label("loc_4A6D")

    OP_4B(0x13, 255)
    OP_4B(0x16, 255)

    label("loc_4A75")

    OP_8C(0x13, 45, 0)
    OP_A2(0x2633)
    ClearChrFlags(0x13, 0x10)
    TalkEnd(0x13)

    label("loc_4A87")

    Return()

    # Function_9_42FA end

    def Function_10_4A88(): pass

    label("Function_10_4A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_5282")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DB1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C18")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B35")
    Jump("loc_4B77")

    label("loc_4B35")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B51")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B77")

    label("loc_4B51")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B6D")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B77")

    label("loc_4B6D")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B77")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #161
        0x1B,
        (
            "#816FRies seems to have cheered up some now.\x02\x03",

            "#819FHeehee. I'm glad I decided to come over\x01",
            "and talk to her.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_4DAB")

    label("loc_4C18")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4CA8")
    Jump("loc_4CEA")

    label("loc_4CA8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4CC4")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CEA")

    label("loc_4CC4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CE0")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CEA")

    label("loc_4CE0")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4CEA")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 1)

    ChrTalk(    #162
        0x1B,
        (
            "#818FSo anyway, Estelle and I hurried there as\x01",
            "fast as we could...\x02\x03",

            "#810FOh! Estelle's the name of this bracer I know,\x01",
            "by the way...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    SetChrSubChip(0xFE, 1)

    label("loc_4DAB")

    OP_A2(0x9)
    Jump("loc_527F")

    label("loc_4DB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50A9")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4E4F")
    Jump("loc_4E91")

    label("loc_4E4F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4E6B")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E91")

    label("loc_4E6B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E87")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E91")

    label("loc_4E87")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E91")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #163
        0x1B,
        (
            "#810F...By the way, has Agate headed out already?\x02\x03",

            "#1311FI was planning to make my move on Tita once\x01",
            "he was out of the picture, but I don't want to\x01",
            "try anything too soon and get caught in the act...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_501B")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #164
        0x1B,
        (
            "#1317FY-Yikes! When did you get there?!\x02\x03",

            "Oopsies...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x106,
        "#057FYou'd better watch yourself, cotton-for-brains.\x02",
    )

    CloseMessageWindow()
    Jump("loc_509E")

    label("loc_501B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_509E")

    ChrTalk(    #166
        0x106,
        (
            "#057FYou do know I'm RIGHT IN FRONT OF YOU,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #167
        0x1B,
        "#1317FWh-Where'd YOU come from?!\x02",
    )

    CloseMessageWindow()

    label("loc_509E")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_527F")

    label("loc_50A9")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5139")
    Jump("loc_517B")

    label("loc_5139")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5155")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_517B")

    label("loc_5155")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5171")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_517B")

    label("loc_5171")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_517B")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 1)

    ChrTalk(    #168
        0x1B,
        (
            "#1316FThis was just when that floating city collapsed,\x01",
            "so everyone was really busy...\x02\x03",

            "#1317FBecause of that, I couldn't go out shopping at\x01",
            "aaaaaall...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x109,
        "#1840F(...How did she get on to shopping?)\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    SetChrSubChip(0xFE, 1)

    label("loc_527F")

    Jump("loc_5594")

    label("loc_5282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_5594")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5458")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_4A(0x12, 255)

    ChrTalk(    #170
        0x1B,
        (
            "#818FHuh, really? That doesn't match up with\x01",
            "what I've heard, though...\x02\x03",

            "Weren't you so worried about him that you \x01",
            "collapsed after finding out he was okay not\x01",
            "that long ago?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x12, 0xFE, 400)
    Sleep(200)

    ChrTalk(    #171
        0x12,
        "#1441FP-Please. I did no such thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x1B,
        "#819FHmm? Are you  s-u-u-u-r-e  about that?\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #173
        0x102,
        (
            "#1505F(It didn't take Anelace long to get a handle\x01",
            "on her personality...)\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x12, 255)
    OP_8C(0x12, 71, 0)
    OP_A2(0x265C)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_5594")

    label("loc_5458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54CC")
    TalkBegin(0xFE)

    ChrTalk(    #174
        0x1B,
        "#810FSo this is the famous Ries, huh?\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #175
        0x1B,
        "#1311FShe's so cuuute.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_5591")

    label("loc_54CC")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #176
        0x1B,
        (
            "#818FRies is one of those types who just can't be\x01",
            "honest with herself, huh?\x02\x03",

            "#816FWell, it's her lucky day, because Doctor Anelace\x01",
            "knows exactly how to deal with people like her.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_5591")

    TalkEnd(0xFE)

    label("loc_5594")

    Return()

    # Function_10_4A88 end

    def Function_11_5595(): pass

    label("Function_11_5595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_569F")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_561F")

    ChrTalk(    #177
        0x16,
        (
            "#214F...Come on! Get it together!\x02\x03",

            "If you're just gonna loaf around here,\x01",
            "we're gonna leave you behind!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_5694")

    label("loc_561F")


    ChrTalk(    #178
        0x16,
        (
            "#212FStart getting ready to go! Now!\x02\x03",

            "#214FIf you're just gonna loaf around here,\x01",
            "we're gonna leave you behind!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5694")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_6EA5")

    label("loc_569F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_5A07")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5841")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_570A")

    ChrTalk(    #179
        0x105,
        (
            "#1164FUmm... Josette?\x02\x03",

            "#1163FIs something the matter?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57AD")

    label("loc_570A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5758")

    ChrTalk(    #180
        0x101,
        (
            "#1015FUmm... You okay, Josette?\x02\x03",

            "You look kinda down...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57AD")

    label("loc_5758")


    ChrTalk(    #181
        0x109,
        (
            "#1064F...Josette?\x02\x03",

            "#1060FSomething up? You're lookin' pretty down\x01",
            "in the dumps.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57AD")

    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #182
        0x16,
        (
            "#417FN-Not really.\x02\x03",

            "#417FI just can't help but wonder whether we're\x01",
            "ever gonna be able to go home, 's all...\x02\x03",

            "#416FThat's it, okay?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58D6")

    label("loc_5841")


    ChrTalk(    #183
        0x16,
        (
            "#212FMy brothers are waiting for me to get home!\x02\x03",

            "#214FSo I'm not staying here a moment longer than\x01",
            "I have to! We're heading back to our world!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58D6")

    OP_A2(0x8)
    Jump("loc_59FC")

    label("loc_58DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5967")

    ChrTalk(    #184
        0x16,
        (
            "#413FThere's so many stars, but not a single\x01",
            "constellation I know...\x02\x03",

            "#417F...Are we really gonna be able to go back home?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59FC")

    label("loc_5967")


    ChrTalk(    #185
        0x16,
        (
            "#212FMy brothers are waiting for me to get home!\x02\x03",

            "#214FSo I'm not staying here a moment longer than\x01",
            "I have to! We're heading back to our world!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59FC")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_6EA5")

    label("loc_5A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_5AC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A93")
    TalkBegin(0xFE)

    ChrTalk(    #186
        0x16,
        (
            "#215F*sigh* Why did I have to end up somewhere so\x01",
            "weird, anyway?\x02\x03",

            "...\x02\x03",

            "#413FWhat's even gonna happen to us?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    TalkEnd(0xFE)
    Jump("loc_5ABE")

    label("loc_5A93")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #187
        0x16,
        (
            "#215F...\x02\x03",

            "#413F*sigh*\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_5ABE")

    Jump("loc_6EA5")

    label("loc_5AC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_5D08")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C95")

    ChrTalk(    #188
        0x16,
        (
            "#215FThis world really does make no sense.\x02\x03",

            "I mean, I'm pretty sure what Celeste is saying\x01",
            "is the truth, but it all just seems so...weird.\x02\x03",

            "#413FWell, whatever. Guess there's no point in\x01",
            "me worrying about it. I'll just try and help the\x01",
            "princess here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C8F")

    ChrTalk(    #189
        0x105,
        (
            "#1165FI-I'm sorry, Josette.\x02\x03",

            "I didn't mean to push my work onto you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x16,
        (
            "#213FOh, no! It's no big deal!\x02\x03",

            "#210FIt's not like I've got anything better to do\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C8F")

    OP_A2(0x8)
    Jump("loc_5D02")

    label("loc_5C95")


    ChrTalk(    #191
        0x16,
        (
            "#215F*sigh* This place seriously makes no sense\x01",
            "to me...\x02\x03",

            "#413FWhen are we gonna be able to go home...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D02")

    TalkEnd(0xFE)
    Jump("loc_6EA5")

    label("loc_5D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_5EA2")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DD5")

    ChrTalk(    #192
        0x16,
        (
            "#416FHis condition's stabilized a lot compared to before.\x02\x03",

            "#210FHe does still have a small fever, but it's nothing\x01",
            "worth freaking out about. A little fever never hurt\x01",
            "anybody.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_5E9C")

    label("loc_5DD5")


    ChrTalk(    #193
        0x16,
        (
            "#210FIf you need help exploring, you're welcome to ask\x01",
            "me to come along any time!\x02\x03",

            "#211FThis guy's condition has stabilized a lot compared\x01",
            "to before. He'll be back to his usual self in no time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E9C")

    TalkEnd(0xFE)
    Jump("loc_6EA5")

    label("loc_5EA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_61DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6134")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FEF")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #194
        0x16,
        (
            "#216FD-Don't you dare take one step closer to Joshua\x01",
            "wearing that skimpy-as-hell outfit!\x02\x03",

            "#214FJust because you were blessed with bombtastic\x01",
            "boobs doesn't mean you gotta go showing them\x01",
            "off 24/7!\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x1C, 255)
    OP_62(0x1C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #195
        0x1C,
        "#1523FWha...?\x02",
    )

    CloseMessageWindow()
    OP_4B(0x1C, 255)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_612E")

    label("loc_5FEF")

    TalkBegin(0xFE)

    ChrTalk(    #196
        0x16,
        (
            "#210FHe's sleeping like a log at the moment.\x02\x03",

            "Doesn't seem to be moaning in his sleep\x01",
            "as much anymore, either.\x02\x03",

            "#211FWe just need to get his fever down a little\x01",
            "and he'll be good as new.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_612B")

    ChrTalk(    #197
        0x105,
        "#1161FThank you for taking care of him, Josette.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x16,
        (
            "#213FS-Sure.\x02\x03",

            "#211FLeave everything here to me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_612B")

    TalkEnd(0xFE)

    label("loc_612E")

    OP_A2(0x8)
    Jump("loc_61D7")

    label("loc_6134")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_618C")

    ChrTalk(    #199
        0x16,
        (
            "#216FD-Damn it!\x02\x03",

            "Why is life so unfair?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61D4")

    label("loc_618C")


    ChrTalk(    #200
        0x16,
        (
            "#210FLeave everything here to me!\x02\x03",

            "I'm way used to this stuff now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61D4")

    TalkEnd(0xFE)

    label("loc_61D7")

    Jump("loc_6EA5")

    label("loc_61DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_65DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6436")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #201
        0x16,
        (
            "#210FOkay! That should do the trick for now.\x02\x03",

            "Now we'll just have to make sure he doesn't\x01",
            "get too cold.\x02\x03",

            "#211FMaybe I should whip up some porridge for\x01",
            "when he gets up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        (
            "#1019F(W-Wow...)\x02\x03",

            "(I had her written off as a total dumbass,\x01",
            "but she...may actually be kinda capable?)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6361")

    ChrTalk(    #203
        0x105,
        (
            "#1161F(She seems like she'd be an amazing\x01",
            "housewife if she wanted.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6361")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6411")

    ChrTalk(    #204
        0x102,
        (
            "#1500F(From what I remember, she used to handle\x01",
            "all the chores for the other sky bandits, too.)\x02\x03",

            "#1509F(That kind of stuff actually seems to be her \x01",
            "forte.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6411")


    ChrTalk(    #205
        0x101,
        "#1019F(Gaaaaaah!)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_65D7")

    label("loc_6436")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64A4")

    ChrTalk(    #206
        0x16,
        (
            "#210FThere's nothing to worry about here.\x02\x03",

            "Leave looking after him to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65D4")

    label("loc_64A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6515")

    ChrTalk(    #207
        0x16,
        (
            "#210FThere's nothing to worry about here.\x02\x03",

            "Leave looking after him to me and the princess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65D4")

    label("loc_6515")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6585")

    ChrTalk(    #208
        0x16,
        (
            "#210FThere's nothing to worry about here.\x02\x03",

            "#211FLeave looking after him to me and Joshua.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65D4")

    label("loc_6585")


    ChrTalk(    #209
        0x16,
        (
            "#210FThere's nothing to worry about here.\x02\x03",

            "Leave looking after him to us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65D4")

    TalkEnd(0xFE)

    label("loc_65D7")

    Jump("loc_6EA5")

    label("loc_65DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_68DE")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6777")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66C7")

    ChrTalk(    #210
        0x16,
        (
            "#212FHmm...\x02\x03",

            "Honestly, he does actually look cool\x01",
            "playing the lute in that outfit...\x02\x03",

            "Maybe he really is a prince?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x109,
        (
            "#1068FShockingly, that is the one thing about him\x01",
            "that actually holds water.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6771")

    label("loc_66C7")


    ChrTalk(    #212
        0x16,
        (
            "#413FWhew... Well, she seems to have calmed down\x01",
            "a little, at least.\x02\x03",

            "#215FIt's funny how the quieter ones are always the\x01",
            "scariest once you piss them off, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6771")

    OP_A2(0x8)
    Jump("loc_68D8")

    label("loc_6777")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6801")

    ChrTalk(    #213
        0x16,
        (
            "#215FHe's a freakin' weirdo, but he does look\x01",
            "cool when he's playing his lute...\x02\x03",

            "#212FMaybe he really is a prince?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68D8")

    label("loc_6801")

    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(    #214
        0x16,
        (
            "#212FYou better apologize to her later,\x01",
            "you phony priest. You hear me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x109,
        (
            "#1840FI-I hear you...\x02\x03",

            "#1066FI'd appreciate it if you wouldn't call me a\x01",
            "phony priest, though... I am the real deal,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68D8")

    TalkEnd(0xFE)
    Jump("loc_6EA5")

    label("loc_68DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_6A0B")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_699C")

    ChrTalk(    #216
        0x16,
        (
            "#213FWhoa... That's just awful.\x02\x03",

            "#212FI had no idea he was THAT bad as a kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x109,
        (
            "#1068F(She's exaggerating every detail just so\x01",
            "they'll take her side...)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_6A00")

    label("loc_699C")


    ChrTalk(    #218
        0x16,
        (
            "#210FS-Still, I wouldn't worry about it too much.\x02\x03",

            "#211FMaybe it's all a big misunderstanding?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A00")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_6EA5")

    label("loc_6A0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_6BCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B21")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(700)
    TurnDirection(0xFE, 0x109, 800)

    ChrTalk(    #219
        0x16,
        (
            "#214FHey, you!\x02\x03",

            "#212FYou do know she's REALLY mad, right?\x02\x03",

            "I dunno what you did to make her that way,\x01",
            "but you'd better think about apologizing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x109,
        "#1068F(I would if she'd even give me the chance...)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_6BC9")

    label("loc_6B21")

    TalkBegin(0xFE)

    ChrTalk(    #221
        0x16,
        (
            "#212FYou DO know Ries is, like, really mad, right?\x02\x03",

            "Dunno what you did to make her that way,\x01",
            "but you obviously did SOMETHING.\x02\x03",

            "#214FSo you better apologize!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_6BC9")

    Jump("loc_6EA5")

    label("loc_6BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_END)), "loc_6EA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CE3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6CDC")
    TalkBegin(0xFE)
    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(    #222
        0x16,
        (
            "#416F(Honestly...I have no idea what you said to her,\x01",
            "but you're obviously the one in the wrong here.)\x02\x03",

            "#212F(I hope you have a good long think about what\x01",
            "you did wrong while you're out there.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x109,
        "#1841F(...Yes, ma'am.)\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_6CE0")

    label("loc_6CDC")

    Call(5, 9)

    label("loc_6CE0")

    Jump("loc_6EA5")

    label("loc_6CE3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DBC")
    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(    #224
        0x16,
        (
            "#214F(What're you doing here? Just leave her to us and\x01",
            "get on with exploring.)\x02\x03",

            "(You're just going to make things worse by hanging\x01",
            "around here.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x109,
        "#1067F(Y-Yeah, you're right. My bad.)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_6EA2")

    label("loc_6DBC")

    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(    #226
        0x16,
        (
            "#416F(Honestly...I have no idea what you said to her,\x01",
            "but you're obviously the one in the wrong here.)\x02\x03",

            "#212F(I hope you have a good long think about what\x01",
            "you did wrong while you're out there.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x109,
        "#1841F(...My bad.)\x02",
    )

    CloseMessageWindow()

    label("loc_6EA2")

    TalkEnd(0xFE)

    label("loc_6EA5")

    Return()

    # Function_11_5595 end

    def Function_12_6EA6(): pass

    label("Function_12_6EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_7109")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F72")
    TalkBegin(0xFE)

    ChrTalk(    #228
        0x14,
        (
            "#178FIt seems like not even the ancients knew all that\x01",
            "much about Phantasma.\x02\x03",

            "#176FIn a way, it makes sense. It's a world created by\x01",
            "the Aureole without their involvement.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    TalkEnd(0xFE)
    Jump("loc_7106")

    label("loc_6F72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6FEF")
    TalkBegin(0xFE)

    ChrTalk(    #229
        0x14,
        (
            "#170FI will take care of everything here in your place,\x01",
            "Your Highness.\x02\x03",

            "So please, take a break.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_7106")

    label("loc_6FEF")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_4A(0x17, 255)
    TurnDirection(0xFE, 0x17, 400)
    Sleep(300)

    ChrTalk(    #230
        0x14,
        (
            "#178FBe that as it may, Your Highness, I'd prefer\x01",
            "it if you took a short break soon.\x02\x03",

            "#176FAnd it'd be my pleasure to take over things\x01",
            "in your place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x17,
        (
            "#1165FHmm... I suppose you're right.\x02\x03",

            "#1382FAll right, then. But only a short one.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x17, 255)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_7106")

    Jump("loc_72F3")

    label("loc_7109")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7222")
    OP_A2(0xA)

    ChrTalk(    #232
        0x14,
        (
            "#176FI haven't the slightest idea what these bookshelves\x01",
            "are doing here...\x02\x03",

            "#178F...but the selection of books from all across the land\x01",
            "is really quite impressive.\x02\x03",

            "Perhaps one of them contains some information that\x01",
            "might help us discover what this place is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72F0")

    label("loc_7222")


    ChrTalk(    #233
        0x14,
        (
            "#172FStill, what was the person who built these\x01",
            "shelves thinking by making them so high?!\x02\x03",

            "Surely no human being could reach the top\x01",
            "shelf here...or any of the ones in the upper\x01",
            "half, for that matter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72F0")

    TalkEnd(0xFE)

    label("loc_72F3")

    Return()

    # Function_12_6EA6 end

    def Function_13_72F4(): pass

    label("Function_13_72F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7451")
    TalkBegin(0xFE)

    ChrTalk(    #234
        0x1F,
        (
            "#115FSome here may believe being called to this world\x01",
            "was a coincidence, but I don't feel my presence\x01",
            "here is.\x02\x03",

            "#110FNo matter whose will it was that I was summoned\x01",
            "to Phantasma, I've gained truly invaluable\x01",
            "experiences here.\x02\x03",

            "#111FNow all that remains is for me to make the best\x01",
            "use of them I can in my life going forward.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_A2(0xE)
    Jump("loc_75B7")

    label("loc_7451")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #235
        0x1F,
        (
            "#112FStill, this library truly is an astonishing thing...\x02\x03",

            "#115FThere's so much fascinating material here,\x01",
            "I'm not sure where to start...\x02\x03",

            "I'll have to try and commit as much of it to\x01",
            "memory as possible while I'm still here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_757F")

    ChrTalk(    #236
        0x101,
        "#1016F(Th-That's some real dedication...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_75AF")

    label("loc_757F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75AF")

    ChrTalk(    #237
        0x110,
        "#269F(Heehee. How adorable.)\x02",
    )

    CloseMessageWindow()

    label("loc_75AF")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_75B7")

    Return()

    # Function_13_72F4 end

    def Function_14_75B8(): pass

    label("Function_14_75B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76A7")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #238
        0x15,
        (
            "#270F...'Flamant's Nobility Annual,'\x01",
            "'The Man Without A Name, Volume 4'...\x02\x03",

            "'Ored's Unspoiled Beauty,'\x01",
            "back issues of the Imperial Chronicle...\x02\x03",

            "#272FWell, none of these are going to be of any\x01",
            "use to us.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0xF)
    TalkEnd(0xFE)
    Jump("loc_7734")

    label("loc_76A7")

    TalkBegin(0xFE)

    ChrTalk(    #239
        0x15,
        (
            "#276FI was hoping I might be able to find information\x01",
            "about our foes here in this library...\x02\x03",

            "No such luck so far, unfortunately.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_7734")

    Return()

    # Function_14_75B8 end

    def Function_15_7735(): pass

    label("Function_15_7735")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77EF")
    OP_A2(0xC)
    OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
    Sleep(200)

    ChrTalk(    #240
        0x21,
        (
            "#1228F*pant*...*pant*...\x02\x03",

            "#1224FD-Don't talk to me... Please...\x02\x03",

            "I'm too tired to move another muscle...\x02\x03",

            "#1227FJ-Just leave me alone!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78F8")

    label("loc_77EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_788E")
    OP_A2(0xD)
    OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
    Sleep(200)

    ChrTalk(    #241
        0x21,
        (
            "#1225FD-Did you not hear me? Don't talk to me!\x02\x03",

            "#1224FUgh... Are you making fun of me?\x02\x01",

            "#1227FYou are, aren't you?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78F8")

    label("loc_788E")

    OP_A3(0xC)
    OP_A3(0xD)

    ChrTalk(    #242
        0x21,
        (
            "#1228FJ-Just leave me alone... Please...\x02\x03",

            "If you wanna laugh at me, go do it somewhere\x01",
            "else...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78F8")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Return()

    # Function_15_7735 end

    SaveToFile()

Try(main)
