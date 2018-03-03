from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M4110   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M4110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
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
        'ED6_DT29/CH14360 ._CH',             # 00
        'ED6_DT29/CH14360 ._CH',             # 01
        'ED6_DT29/CH14690 ._CH',             # 02
        'ED6_DT29/CH14691 ._CH',             # 03
        'ED6_DT29/CH14460 ._CH',             # 04
        'ED6_DT29/CH14461 ._CH',             # 05
        'ED6_DT29/CH14620 ._CH',             # 06
        'ED6_DT29/CH14621 ._CH',             # 07
        'ED6_DT29/CH14630 ._CH',             # 08
        'ED6_DT29/CH14631 ._CH',             # 09
        'ED6_DT29/CH14010 ._CH',             # 0A
        'ED6_DT29/CH14011 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT29/CH14360P._CP',             # 00
        'ED6_DT29/CH14360P._CP',             # 01
        'ED6_DT29/CH14690P._CP',             # 02
        'ED6_DT29/CH14691P._CP',             # 03
        'ED6_DT29/CH14460P._CP',             # 04
        'ED6_DT29/CH14461P._CP',             # 05
        'ED6_DT29/CH14620P._CP',             # 06
        'ED6_DT29/CH14621P._CP',             # 07
        'ED6_DT29/CH14630P._CP',             # 08
        'ED6_DT29/CH14631P._CP',             # 09
        'ED6_DT29/CH14010P._CP',             # 0A
        'ED6_DT29/CH14011P._CP',             # 0B
    )

    DeclMonster(
        X                   = -2320,
        Z                   = 0,
        Y                   = -5480,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x258,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 10670,
        Z                   = -20,
        Y                   = 23680,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -22750,
        Z                   = 0,
        Y                   = 29730,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x259,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -8610,
        Z                   = 0,
        Y                   = -37690,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -44400,
        TriggerZ            = 500,
        TriggerY            = 7650,
        TriggerRange        = 1500,
        ActorX              = -44400,
        ActorZ              = 4000,
        ActorY              = 7650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7980,
        TriggerZ            = 0,
        TriggerY            = 17210,
        TriggerRange        = 1000,
        ActorX              = 7980,
        ActorZ              = 1000,
        ActorY              = 17210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1C2",          # 00, 0
        "Function_1_214",          # 01, 1
        "Function_2_269",          # 02, 2
        "Function_3_3A2",          # 03, 3
        "Function_4_10C3",         # 04, 4
        "Function_5_1872",         # 05, 5
        "Function_6_1B5F",         # 06, 6
        "Function_7_1E18",         # 07, 7
        "Function_8_1EFF",         # 08, 8
        "Function_9_2015",         # 09, 9
    )


    def Function_0_1C2(): pass

    label("Function_0_1C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E1")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_1DA"),
        (SWITCH_DEFAULT, "loc_1E1"),
    )


    label("loc_1DA")

    Event(0, 7)
    Jump("loc_1E1")

    label("loc_1E1")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1ED"),
        (SWITCH_DEFAULT, "loc_1F5"),
    )


    label("loc_1ED")

    SetMapFlags(0x10000000)
    Jump("loc_1F5")

    label("loc_1F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_213")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_213")

    Return()

    # Function_0_1C2 end

    def Function_1_214(): pass

    label("Function_1_214")

    OP_16(0x2, 0xFA0, 0xFFFDE4F0, 0xFFFE0C00, 0x230063)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_237")
    OP_71(0x401, 0x0)
    ExitThread()
    OP_82(0x88, 0x0)

    label("loc_237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_244")
    OP_79(0x0, 0x2)
    OP_7B()

    label("loc_244")

    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_261")
    OP_6F(0x2, 0)
    Jump("loc_268")

    label("loc_261")

    OP_6F(0x2, 60)

    label("loc_268")

    Return()

    # Function_1_214 end

    def Function_2_269(): pass

    label("Function_2_269")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-45540, 2600, 6230, 0)
    OP_67(0, 6280, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(225000, 0)
    OP_6E(376, 0)

    def lambda_2CC():
        OP_6D(-45540, 600, 6230, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2CC)

    def lambda_2E4():
        OP_67(0, 4660, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2E4)

    def lambda_2FC():
        OP_6B(2230, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2FC)

    def lambda_30C():
        OP_6E(376, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_30C)
    FadeToBright(1500, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    def lambda_330():
        OP_6B(2000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_330)
    OP_22(0xD7, 0x0, 0x64)
    Fade(1000)
    OP_72(0x401, 0x0)
    ExitThread()
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7A(0x0, 0x2)
    OP_7B()
    OP_0D()
    Sleep(1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/M3204   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_269 end

    def Function_3_3A2(): pass

    label("Function_3_3A2")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-45100, 250, 6960, 0)
    OP_67(0, 4800, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(225000, 0)
    OP_6E(348, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D1")
    SetChrPos(0x102, -42310, 0, 9750, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_449")
    SetChrPos(0x109, -40950, 0, 9840, 225)
    SetChrPos(0xF0, -42200, 0, 11190, 225)
    SetChrPos(0xF1, -40780, 0, 11320, 225)
    Jump("loc_4CE")

    label("loc_449")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48D")
    SetChrPos(0x109, -40950, 0, 9840, 225)
    SetChrPos(0xEF, -42200, 0, 11190, 225)
    SetChrPos(0xF1, -40780, 0, 11320, 225)
    Jump("loc_4CE")

    label("loc_48D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CE")
    SetChrPos(0x109, -40950, 0, 9840, 225)
    SetChrPos(0xEF, -42200, 0, 11190, 225)
    SetChrPos(0xF0, -40780, 0, 11320, 225)

    label("loc_4CE")

    Jump("loc_515")

    label("loc_4D1")

    SetChrPos(0x109, -42310, 0, 9750, 225)
    SetChrPos(0xEF, -40950, 0, 9840, 225)
    SetChrPos(0xF0, -42200, 0, 11190, 225)
    SetChrPos(0xF1, -40780, 0, 11320, 225)

    label("loc_515")

    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #0
        "\x07\x05The face of the monument is glowing, and words are visible upon its surface.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #1
        (
            "\x07\x02#40WIn my lord's place, I, the Schwarzritter,\x01",
            "do decree:\x01",
            "#500W \x01",
            "#40W Here lies the Black Ark.\x01",
            "#500W \x01",
            "#40W       Place your hand on this monument,\x01",
            "the orphan of a lost village among your number.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B2")
    OP_A2(0x2B22)

    ChrTalk(    #2
        0x102,
        "#1504F#6P#3S!!!\x02",
    )

    CloseMessageWindow()

    label("loc_6B2")


    ChrTalk(    #3
        0x109,
        "#1069F#6PWha...?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F6")

    ChrTalk(    #4
        0x101,
        "#1020F#6PTh-That's...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E6")

    label("loc_6F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_722")

    ChrTalk(    #5
        0x10B,
        "#216F#6PTh-That's...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E6")

    label("loc_722")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74F")

    ChrTalk(    #6
        0x105,
        "#1164F#6PTh-That's...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E6")

    label("loc_74F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77C")

    ChrTalk(    #7
        0x103,
        "#1523F#6PTh-That's...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E6")

    label("loc_77C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B8")

    ChrTalk(    #8
        0x106,
        "#055F#6PW-Wait a sec! Isn't that...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E6")

    label("loc_7B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E4")

    ChrTalk(    #9
        0x108,
        "#072F#6PTh-That's...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E6")

    label("loc_7E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_811")

    ChrTalk(    #10
        0x104,
        "#1542F#6PBut that's...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E6")

    label("loc_811")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_839")

    ChrTalk(    #11
        0x10D,
        "#273F#6P...What?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E6")

    label("loc_839")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_865")

    ChrTalk(    #12
        0x107,
        "#065F#6PTh-That's...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E6")

    label("loc_865")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_891")

    ChrTalk(    #13
        0x110,
        "#262F#6PBut that's...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E6")

    label("loc_891")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8BD")

    ChrTalk(    #14
        0x10C,
        "#112F#6PTh-That's...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E6")

    label("loc_8BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E6")

    ChrTalk(    #15
        0x10E,
        "#172F#6PTh-That's...!\x02",
    )

    CloseMessageWindow()

    label("loc_8E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9E3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94C")

    ChrTalk(    #16
        0x10F,
        "#1444F#6PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10A,
        "#814F#6PWhat's wrong?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9C0")

    label("loc_94C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_988")

    ChrTalk(    #18
        0x10F,
        (
            "#1444F#6PHuh...?\x02\x03",

            "Is something wrong?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C0")

    label("loc_988")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9C0")

    ChrTalk(    #19
        0x10A,
        (
            "#814F#6PHuh...?\x02\x03",

            "Is something wrong?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C0")


    ChrTalk(    #20
        0x109,
        "#1067F#5PW-Well, it's just...\x02",
    )

    CloseMessageWindow()

    label("loc_9E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CF3")
    Sleep(500)

    ChrTalk(    #21
        0x102,
        (
            "#1503F#5P...\x02\x03",

            "#1513FThe Schwarzritter's waiting for us in here.\x02\x03",

            "#1514FAnd for some reason, he really wants me\x01",
            "to come and see him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x109,
        (
            "#1065F#6PYep. That about sums it up.\x02\x03",

            "#1063FSo...the choice is yours, Joshua.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 45, 400)
    Sleep(300)

    ChrTalk(    #23
        0x102,
        (
            "#1505F#5PNaturally, I'll be accepting his invitation.\x02\x03",

            "#1500FAs soon as you're all ready, let me know.\x01",
            "Then I'll touch the monument.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B8E")

    ChrTalk(    #24
        0x101,
        "#1026F#6PJoshua...\x02",
    )

    CloseMessageWindow()

    label("loc_B8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BB2")

    ChrTalk(    #25
        0x10B,
        "#215F#6PU-Umm...\x02",
    )

    CloseMessageWindow()

    label("loc_BB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD8")

    ChrTalk(    #26
        0x105,
        "#1163F#6PJoshua...\x02",
    )

    CloseMessageWindow()

    label("loc_BD8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFF")

    ChrTalk(    #27
        0x107,
        "#063F#6PJ-Joshua...\x02",
    )

    CloseMessageWindow()

    label("loc_BFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C2B")

    ChrTalk(    #28
        0x110,
        "#1307F#6P...You're sure?\x02",
    )

    CloseMessageWindow()

    label("loc_C2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CF0")

    ChrTalk(    #29
        0x102,
        (
            "#1513F#5PI am. No matter what happens, I'll be fine.\x02\x03",

            "#1500FAll we can do now is keep moving forward,\x01",
            "and that's what I intend to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF0")

    Jump("loc_10AC")

    label("loc_CF3")

    Sleep(500)

    ChrTalk(    #30
        0x109,
        (
            "#1065F#5P(The orphan of a lost village? Well, this is the\x01",
            "most obvious one so far.)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 45, 400)
    Sleep(300)

    ChrTalk(    #31
        0x109,
        (
            "#1063F#5PWe should head back to the garden and speak\x01",
            "to Joshua. \x02\x03",

            "We can decide what to do then.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DED")

    ChrTalk(    #32
        0x101,
        "#1007F#6P...Yeah...\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB0")

    label("loc_DED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E15")

    ChrTalk(    #33
        0x10B,
        "#413F#6PY-Yeah...\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB0")

    label("loc_E15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E40")

    ChrTalk(    #34
        0x105,
        "#1169F#6P...Right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB0")

    label("loc_E40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E6A")

    ChrTalk(    #35
        0x103,
        "#1532F#6P...Yeah...\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB0")

    label("loc_E6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E93")

    ChrTalk(    #36
        0x106,
        "#552F#6P...Yeah...\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB0")

    label("loc_E93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EBC")

    ChrTalk(    #37
        0x108,
        "#074F#6P...Yeah...\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB0")

    label("loc_EBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE5")

    ChrTalk(    #38
        0x104,
        "#1542F#6PIndeed...\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB0")

    label("loc_EE5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F0E")

    ChrTalk(    #39
        0x10D,
        "#272F#6P...Indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB0")

    label("loc_F0E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F37")

    ChrTalk(    #40
        0x107,
        "#561F#6PR-Right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB0")

    label("loc_F37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F63")

    ChrTalk(    #41
        0x110,
        "#268F#6P...All right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB0")

    label("loc_F63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F8B")

    ChrTalk(    #42
        0x10C,
        "#115F#6PIndeed...\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB0")

    label("loc_F8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FB0")

    ChrTalk(    #43
        0x10E,
        "#176F#6PIndeed...\x02",
    )

    CloseMessageWindow()

    label("loc_FB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_101E")

    ChrTalk(    #44
        0x10A,
        "#1317F#6P(I-I feel like I'm missing something...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10F,
        "#1445F#6P(As do I...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_10AC")

    label("loc_101E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1067")

    ChrTalk(    #46
        0x10F,
        "#1445F#6P(I feel as though I'm missing something.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_10AC")

    label("loc_1067")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10AC")

    ChrTalk(    #47
        0x10A,
        "#1317F#6P(I-I feel like I'm missing something...)\x02",
    )

    CloseMessageWindow()

    label("loc_10AC")

    OP_A2(0x2B21)
    OP_28(0x3A, 0x1, 0x2)
    OP_28(0x3A, 0x1, 0x4)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_3_3A2 end

    def Function_4_10C3(): pass

    label("Function_4_10C3")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-45100, 250, 6960, 0)
    OP_67(0, 5420, -10000, 0)
    OP_6B(2470, 0)
    OP_6C(225000, 0)
    OP_6E(348, 0)
    SetChrPos(0x109, -42320, 0, 9790, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_115C")
    SetChrPos(0xEF, -43440, 480, 8590, 225)
    SetChrPos(0xF0, -41000, 0, 10170, 225)
    SetChrPos(0xF1, -41900, 0, 11120, 225)
    Jump("loc_11E1")

    label("loc_115C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A0")
    SetChrPos(0xF0, -43440, 480, 8590, 225)
    SetChrPos(0xEF, -41000, 0, 10170, 225)
    SetChrPos(0xF1, -41900, 0, 11120, 225)
    Jump("loc_11E1")

    label("loc_11A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E1")
    SetChrPos(0xF1, -43440, 480, 8590, 225)
    SetChrPos(0xEF, -41000, 0, 10170, 225)
    SetChrPos(0xF0, -41900, 0, 11120, 225)

    label("loc_11E1")

    OP_0D()
    Sleep(300)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #48
        (
            "\x07\x02#40WIn my lord's place, I, \x01",
            "the Schwarzritter, do decree...\x01",
            "#500W \x01",
            "#40W Here lies the Black Ark.\x01",
            "#500W \x01",
            "#40W       Place your hand on this monument,\x01",
            "the orphan of a lost village among your number.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1317")
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #49
        0x102,
        "#1502F#6P...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    label("loc_1317")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_132A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_186F")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Touch the monument\x01",      # 0
            "Step away\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1383"),
        (SWITCH_DEFAULT, "loc_185A"),
    )


    label("loc_1383")

    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    LoadEffect(0x0, "map\\mp200_01.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13FB")

    def lambda_13E9():
        OP_6D(-45100, 10000, 6960, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_13E9)

    label("loc_13FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_155F")
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_144E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_144E)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_14A4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14A4)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_14FA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_14FA)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1550():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1550)
    Jump("loc_1824")

    label("loc_155F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C3")
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_15B2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_15B2)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1608():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1608)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_165E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_165E)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_16B4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_16B4)
    Jump("loc_1824")

    label("loc_16C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1824")
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1716():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1716)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_176C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_176C)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_17C2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_17C2)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1818():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1818)

    label("loc_1824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1834")
    Sleep(1500)
    Jump("loc_1839")

    label("loc_1834")

    Sleep(500)

    label("loc_1839")

    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/M5408   ._SN", 103, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_186C")

    label("loc_185A")

    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_186C")

    label("loc_186C")

    Jump("loc_132A")

    label("loc_186F")

    EventEnd(0x0)
    Return()

    # Function_4_10C3 end

    def Function_5_1872(): pass

    label("Function_5_1872")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-43550, 0, 6920, 0)
    OP_67(0, 6510, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(179000, 0)
    OP_6E(339, 0)
    SetChrPos(0x0, -43470, 490, 8880, 225)
    SetChrPos(0x1, -42470, 0, 10010, 225)
    SetChrPos(0x2, -41040, 0, 10440, 225)
    SetChrPos(0x3, -42120, 0, 11800, 225)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_191D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B5C")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Touch the monument\x01",      # 0
            "Step away\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1976"),
        (SWITCH_DEFAULT, "loc_1B47"),
    )


    label("loc_1976")

    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1A13():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1A13)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1A69():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1A69)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1ABF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1ABF)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1B15():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1B15)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/M5408   ._SN", 103, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B59")

    label("loc_1B47")

    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B59")

    label("loc_1B59")

    Jump("loc_191D")

    label("loc_1B5C")

    EventEnd(0x0)
    Return()

    # Function_5_1872 end

    def Function_6_1B5F(): pass

    label("Function_6_1B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_1B6E")
    Call(0, 5)
    Return()

    label("loc_1B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 2)), scpexpr(EXPR_END)), "loc_1C98")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B8B")
    Call(0, 4)
    Return()

    label("loc_1B8B")

    TalkBegin(0xFF)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #50
        (
            "\x07\x02#40WIn my lord's place, I, the Schwarzritter,\x01",
            "do decree:\x01",
            "#500W \x01",
            "#40W Here lies the Black Ark.\x01",
            "#500W \x01",
            "#40W       Place your hand on this monument,\x01",
            "the orphan of a lost village among your number.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Jump("loc_1E17")

    label("loc_1C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DB1")
    TalkBegin(0xFF)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #51
        (
            "\x07\x02#40WIn my lord's place, I, the Schwarzritter,\x01",
            "do decree:\x01",
            "#500W \x01",
            "#40W Here lies the Black Ark.\x01",
            "#500W \x01",
            "#40W       Place your hand on this monument,\x01",
            "the orphan of a lost village among your number.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Jump("loc_1E17")

    label("loc_1DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_1DC0")
    Call(0, 3)
    Return()

    label("loc_1DC0")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #52
        "\x07\x05Nothing is written on the nohval monument.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_1E17")

    Return()

    # Function_6_1B5F end

    def Function_7_1E18(): pass

    label("Function_7_1E18")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -42220, 0, 10120, 45)
    SetChrPos(0x1, -42220, 0, 10120, 45)
    SetChrPos(0x2, -42220, 0, 10120, 45)
    SetChrPos(0x3, -42220, 0, 10120, 45)
    OP_69(0x0, 0x0)
    OP_6C(180000, 0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 8)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_7_1E18 end

    def Function_8_1EFF(): pass

    label("Function_8_1EFF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F28")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1F1C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1F1C)

    label("loc_1F28")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F51")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1F45():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1F45)

    label("loc_1F51")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F7A")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1F6E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1F6E)

    label("loc_1F7A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FA3")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1F97():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1F97)

    label("loc_1FA3")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FCF")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1FCF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FE6")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1FE6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FFD")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1FFD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2014")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_2014")

    Return()

    # Function_8_1EFF end

    def Function_9_2015(): pass

    label("Function_9_2015")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20EE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x297, 1)"), scpexpr(EXPR_END)), "loc_2083")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #53
        "\x07\x05Found \x1F\x97\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B9C)
    Jump("loc_20EB")

    label("loc_2083")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #54
        (
            "\x07\x05Found \x1F\x97\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x97\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_20EB")

    Jump("loc_2135")

    label("loc_20EE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #55
        "\x07\x05Don't you have better things to do?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x3A, 0x0)

    label("loc_2135")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_2015 end

    SaveToFile()

Try(main)
