from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M4111   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M4111.x',
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
        '',                                     # 13
        '',                                     # 14
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
        X                   = 54240,
        Z                   = 0,
        Y                   = 4960,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 39410,
        Z                   = 0,
        Y                   = -13960,
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
        X                   = 42430,
        Z                   = 40,
        Y                   = -41320,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 3040,
        Z                   = 0,
        Y                   = -21430,
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
        X                   = -31660,
        Z                   = -40,
        Y                   = -17490,
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
        X                   = -58180,
        Z                   = 0,
        Y                   = -14580,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -34410,
        Y                   = -1000,
        Z                   = -1390,
        Range               = -17390,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xF32,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )


    DeclActor(
        TriggerX            = 9670,
        TriggerZ            = 500,
        TriggerY            = -54320,
        TriggerRange        = 1500,
        ActorX              = 9670,
        ActorZ              = 4000,
        ActorY              = -54320,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23880,
        TriggerZ            = 1000,
        TriggerY            = -10260,
        TriggerRange        = 1000,
        ActorX              = 23880,
        ActorZ              = 1000,
        ActorY              = -10260,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -18470,
        TriggerZ            = 0,
        TriggerY            = -5070,
        TriggerRange        = 1500,
        ActorX              = -18470,
        ActorZ              = 1700,
        ActorY              = -5070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_23E",          # 00, 0
        "Function_1_2C0",          # 01, 1
        "Function_2_339",          # 02, 2
        "Function_3_472",          # 03, 3
        "Function_4_161E",         # 04, 4
        "Function_5_1DBB",         # 05, 5
        "Function_6_20EA",         # 06, 6
        "Function_7_2381",         # 07, 7
        "Function_8_259E",         # 08, 8
        "Function_9_295F",         # 09, 9
        "Function_10_3A7D",        # 0A, 10
        "Function_11_3AB1",        # 0B, 11
        "Function_12_3AEA",        # 0C, 12
        "Function_13_3B23",        # 0D, 13
        "Function_14_3B5C",        # 0E, 14
        "Function_15_3D56",        # 0F, 15
        "Function_16_3E18",        # 10, 16
        "Function_17_3EFF",        # 11, 17
        "Function_18_4015",        # 12, 18
        "Function_19_4181",        # 13, 19
    )


    def Function_0_23E(): pass

    label("Function_0_23E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25D")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_256"),
        (SWITCH_DEFAULT, "loc_25D"),
    )


    label("loc_256")

    Event(0, 16)
    Jump("loc_25D")

    label("loc_25D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_273")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    Event(0, 14)
    Jump("loc_2BF")

    label("loc_273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_289")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 9)
    Jump("loc_2BF")

    label("loc_289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_2AA")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)
    Jump("loc_2BF")

    label("loc_2AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_2BF")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    Event(0, 2)

    label("loc_2BF")

    Return()

    # Function_0_23E end

    def Function_1_2C0(): pass

    label("Function_1_2C0")

    OP_16(0x2, 0xFA0, 0xFFFDDD20, 0xFFFDDD20, 0x230064)
    OP_1B(0x1, 0x0, 0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_2E7")
    OP_71(0x400, 0x0)
    ExitThread()
    Jump("loc_2F6")

    label("loc_2E7")

    OP_10(0x1, 0x0)
    OP_82(0x8A, 0x0)
    OP_82(0x8B, 0x0)
    OP_82(0x8C, 0x0)
    OP_82(0x8D, 0x0)

    label("loc_2F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_307")
    OP_71(0x401, 0x0)
    ExitThread()
    OP_82(0x8E, 0x0)

    label("loc_307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_314")
    OP_79(0x0, 0x2)
    OP_7B()

    label("loc_314")

    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_331")
    OP_6F(0x2, 0)
    Jump("loc_338")

    label("loc_331")

    OP_6F(0x2, 60)

    label("loc_338")

    Return()

    # Function_1_2C0 end

    def Function_2_339(): pass

    label("Function_2_339")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(12000, 6850, -52200, 0)
    OP_67(0, 5810, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(225000, 0)
    OP_6E(256, 0)

    def lambda_39C():
        OP_6D(12000, 2800, -52200, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_39C)

    def lambda_3B4():
        OP_67(0, 3860, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_3B4)

    def lambda_3CC():
        OP_6B(3410, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_3CC)

    def lambda_3DC():
        OP_6E(244, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_3DC)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    def lambda_400():
        OP_6B(3100, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_400)
    OP_22(0xD7, 0x0, 0x64)
    Fade(1000)
    OP_72(0x401, 0x0)
    ExitThread()
    PlayEffect(0x8E, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7A(0x0, 0x2)
    OP_7B()
    OP_0D()
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/U2610   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_339 end

    def Function_3_472(): pass

    label("Function_3_472")

    EventBegin(0x0)
    Fade(500)
    OP_6D(9470, 250, -54520, 0)
    OP_67(0, 5140, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(224000, 0)
    OP_6E(355, 0)
    SetChrPos(0x109, 11600, 0, -52440, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50B")
    SetChrPos(0xEF, 13000, 0, -50910, 225)
    SetChrPos(0xF0, 14390, 0, -50400, 225)
    SetChrPos(0xF1, 13360, 0, -49260, 225)
    Jump("loc_5C6")

    label("loc_50B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54F")
    SetChrPos(0xF0, 13000, 0, -50910, 225)
    SetChrPos(0xEF, 14390, 0, -50400, 225)
    SetChrPos(0xF1, 13360, 0, -49260, 225)
    Jump("loc_5C6")

    label("loc_54F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_593")
    SetChrPos(0xF1, 13000, 0, -50910, 225)
    SetChrPos(0xEF, 14390, 0, -50400, 225)
    SetChrPos(0xF0, 13360, 0, -49260, 225)
    Jump("loc_5C6")

    label("loc_593")

    SetChrPos(0xEF, 13000, 0, -50910, 225)
    SetChrPos(0xF0, 14390, 0, -50400, 225)
    SetChrPos(0xF1, 13360, 0, -49260, 225)

    label("loc_5C6")

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
            "\x07\x02#40WThe Lord of Phantasma does decree...\x01",
            "#500W \x01",
            "#40W Here lies the looking glass.\x01",
            "#500W \x01",
            "#40W       Place your hand on this monument,\x01",
            "the sword-wielding dame among your number.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E42")

    ChrTalk(    #2
        0x109,
        (
            "#1063F#6PThe looking glass? That's gotta be the name of\x01",
            "our next tourist attraction around here.\x02\x03",

            "#1067FHmm... Still, the sword-wielding dame...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A1")
    OP_A2(0x0)

    ChrTalk(    #3
        0x101,
        (
            "#1007F#6PWe've got a few women with us who fight\x01",
            "with swords, so we've got our pick...\x02\x03",

            "#1006F...but personally, I think it's Anelace.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAC")

    label("loc_8A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_93E")

    ChrTalk(    #4
        0x103,
        (
            "#1525F#6PWe've got a few women with us who fight\x01",
            "with swords, so we've got our pick...\x02\x03",

            "#1520F...but personally, I think it's Anelace.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAC")

    label("loc_93E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A01")

    ChrTalk(    #5
        0x10C,
        (
            "#115F#6PHmm... We have a number of women with us\x01",
            "who fight using swords, so there are several\x01",
            "potential candidates...\x02\x03",

            "#110F...but I think the most fitting here is Anelace.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAC")

    label("loc_A01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD5")

    ChrTalk(    #6
        0x10E,
        (
            "#176F#6PHmm... We have a number of women with us\x01",
            "who fight using swords--myself included--so\x01",
            "there are several potential candidates...\x02\x03",

            "#170F...but I think the most fitting here is Anelace.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAC")

    label("loc_AD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BAC")

    ChrTalk(    #7
        0x105,
        (
            "#1167F#6PHmm... There are a few women among us who\x01",
            "fight using swords, so we have more than one\x01",
            "potential candidate this time...\x02\x03",

            "#1160F...but I have this feeling that it's talking about\x01",
            "Anelace.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D0A")
    OP_A2(0x2B0B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C7A")

    ChrTalk(    #8
        0x10A,
        (
            "#819F#5PI dunnooo... I mean, it's a cool-sounding title\x01",
            "and all, but does it really fit me?\x02\x03",

            "#816FStill, it doesn't hurt to try, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1001F#6PYup, yup. Give it a go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_D07")

    label("loc_C7A")


    ChrTalk(    #10
        0x10A,
        (
            "#819F#5PI dunno... I mean, it's a cool-sounding title and\x01",
            "all, but does it really fit me?\x02\x03",

            "#816FStill, I guess it doesn't hurt to try. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_D07")

    Jump("loc_E3F")

    label("loc_D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DB5")
    OP_8C(0x109, 45, 400)
    Sleep(300)

    ChrTalk(    #11
        0x109,
        (
            "#1075F#5PYou think so, too, huh?\x02\x03",

            "#1060FAll right. Let's head back to the garden and\x01",
            "get her to come here with us, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1006FOkie dokie!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E3F")

    label("loc_DB5")

    OP_8C(0x109, 45, 400)
    Sleep(300)

    ChrTalk(    #13
        0x109,
        (
            "#1075F#5PYou think so, too, huh?\x02\x03",

            "#1060FAll right. Let's head back to the garden and get\x01",
            "her to come here with us, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3F")

    Jump("loc_1403")

    label("loc_E42")


    ChrTalk(    #14
        0x109,
        (
            "#1063F#6PThe looking glass? That's gotta be the name of\x01",
            "our next tourist attraction around here.\x02\x03",

            "#1067FHmm... Still, the sword-wielding dame...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 45, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F70")

    ChrTalk(    #15
        0x109,
        (
            "#1078F#5PWe've got a few women in our ranks who'd apply,\x01",
            "but the one that feels the most right here to me\x01",
            "is Anelace.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FEB")

    label("loc_F70")


    ChrTalk(    #16
        0x109,
        (
            "#1078F#5PWe've got a few women in our ranks who'd apply,\x01",
            "but the one that feels the most right here to me\x01",
            "is Anelace.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_108C")
    OP_A2(0x2B0B)

    ChrTalk(    #17
        0x10A,
        (
            "#819F#6PI dunno... I mean, it's a cool-sounding title and\x01",
            "all, but does it really fit me?\x02\x03",

            "#816FStill, I guess it doesn't hurt to try. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1403")

    label("loc_108C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1104")

    ChrTalk(    #18
        0x10F,
        (
            "#1446F#6PI see...\x02\x03",

            "#1448FWe'll have to head back to the garden and\x01",
            "get her to come with us, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1403")

    label("loc_1104")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_118C")

    ChrTalk(    #19
        0x102,
        (
            "#1505F#6PThat sounds right to me.\x02\x03",

            "#1500FWe'll have to head back to the garden and\x01",
            "get her to come with us, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1403")

    label("loc_118C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1209")

    ChrTalk(    #20
        0x106,
        (
            "#053F#6PThat sounds right to me.\x02\x03",

            "#051FBest head back to the garden and get her\x01",
            "to come with us, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1403")

    label("loc_1209")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_128F")

    ChrTalk(    #21
        0x107,
        (
            "#560F#6PThat sounds right to me.\x02\x03",

            "#061FWe'll have to head back to the garden and\x01",
            "get her to come with us, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1403")

    label("loc_128F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_130F")

    ChrTalk(    #22
        0x108,
        (
            "#573F#6PThat sounds right to me.\x02\x03",

            "#070FTime to head back to the garden and get\x01",
            "her to come with us, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1403")

    label("loc_130F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1380")

    ChrTalk(    #23
        0x104,
        (
            "#1545F#6PAgreed.\x02\x03",

            "#1540FTime to head back to the garden and ask\x01",
            "her to come with us, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1403")

    label("loc_1380")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1403")

    ChrTalk(    #24
        0x10D,
        (
            "#278F#6PThat sounds right to me.\x02\x03",

            "#277FWe'll have to head back to the garden and\x01",
            "ask her to come with us, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1403")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1607")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14FE")

    ChrTalk(    #25
        0x110,
        (
            "#260F#6PAnelace was the girl with the pretty ribbon, right?\x02\x03",

            "#261FHeehee. I would have called her the stuffed-toy-\x01",
            "loving dame than the sword-wielding one off the\x01",
            "top of my head, but oh, well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15B2")

    label("loc_14FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15B2")

    ChrTalk(    #26
        0x10B,
        (
            "#210F#6PShe's the bracer with the yellow ribbon, right?\x02\x03",

            "#211FI would've called her the stuffed-toy-loving dame\x01",
            "than the sword-wielding one if it were up to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15B2")


    ChrTalk(    #27
        0x109,
        (
            "#1066F#5PHaha. A clue like that would've hit the nail on the\x01",
            "head, no question.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1607")

    OP_A2(0x2B09)
    OP_28(0x38, 0x1, 0x1)
    OP_28(0x38, 0x1, 0x2)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_3_472 end

    def Function_4_161E(): pass

    label("Function_4_161E")

    EventBegin(0x0)
    Fade(500)
    OP_6D(9470, 250, -54520, 0)
    OP_67(0, 5140, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(224000, 0)
    OP_6E(355, 0)
    SetChrPos(0x109, 11790, 0, -52090, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16B7")
    SetChrPos(0xEF, 10550, 480, -53470, 225)
    SetChrPos(0xF0, 13300, 0, -51640, 225)
    SetChrPos(0xF1, 12430, 0, -50420, 225)
    Jump("loc_173C")

    label("loc_16B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16FB")
    SetChrPos(0xF0, 10550, 480, -53470, 225)
    SetChrPos(0xEF, 13300, 0, -51640, 225)
    SetChrPos(0xF1, 12430, 0, -50420, 225)
    Jump("loc_173C")

    label("loc_16FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_173C")
    SetChrPos(0xF1, 10550, 480, -53470, 225)
    SetChrPos(0xEF, 13300, 0, -51640, 225)
    SetChrPos(0xF0, 12430, 0, -50420, 225)

    label("loc_173C")

    OP_0D()
    Sleep(300)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #28
        (
            "\x07\x02#40WThe Lord of Phantasma does decree...\x01",
            "#500W \x01",
            "#40W Here lies the looking glass.\x01",
            "#500W \x01",
            "#40W       Place your hand on this monument,\x01",
            "the sword-wielding dame among your number.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1860")
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #29
        0x10A,
        "#812F#6PUmm...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    label("loc_1860")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1873")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DB8")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Touch the Monument\x01",      # 0
            "Step Away\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_18CC"),
        (SWITCH_DEFAULT, "loc_1DA3"),
    )


    label("loc_18CC")

    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x8E, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    LoadEffect(0x0, "map\\mp200_01.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1944")

    def lambda_1932():
        OP_6D(9320, 10000, -55000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1932)

    label("loc_1944")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AA8")
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1997():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1997)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_19ED():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_19ED)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1A43():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1A43)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1A99():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1A99)
    Jump("loc_1D6D")

    label("loc_1AA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C0C")
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1AFB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1AFB)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1B51():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1B51)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1BA7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1BA7)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1BFD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1BFD)
    Jump("loc_1D6D")

    label("loc_1C0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D6D")
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1C5F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1C5F)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1CB5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1CB5)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1D0B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1D0B)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1D61():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1D61)

    label("loc_1D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D7D")
    Sleep(1500)
    Jump("loc_1D82")

    label("loc_1D7D")

    Sleep(500)

    label("loc_1D82")

    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/M5600   ._SN", 104, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DB5")

    label("loc_1DA3")

    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DB5")

    label("loc_1DB5")

    Jump("loc_1873")

    label("loc_1DB8")

    EventEnd(0x0)
    Return()

    # Function_4_161E end

    def Function_5_1DBB(): pass

    label("Function_5_1DBB")

    EventBegin(0x0)
    Fade(500)
    OP_6D(9320, 0, -55000, 0)
    OP_67(0, 4870, -10000, 0)
    OP_6B(3290, 0)
    OP_6C(224000, 0)
    OP_6E(285, 0)
    SetChrPos(0x0, 10550, 480, -53470, 225)
    SetChrPos(0x1, 11790, 0, -52090, 225)
    SetChrPos(0x2, 13300, 0, -51640, 225)
    SetChrPos(0x3, 12430, 0, -50420, 225)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #30
        "\x07\x05The front of the monument is glowing.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1EA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20E7")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Touch the Monument\x01",      # 0
            "Step Away\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F01"),
        (SWITCH_DEFAULT, "loc_20D2"),
    )


    label("loc_1F01")

    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x8E, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1F9E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1F9E)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x1, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1FF4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1FF4)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x2, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_204A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_204A)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x3, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_20A0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_20A0)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/M5600   ._SN", 104, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20E4")

    label("loc_20D2")

    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20E4")

    label("loc_20E4")

    Jump("loc_1EA8")

    label("loc_20E7")

    EventEnd(0x0)
    Return()

    # Function_5_1DBB end

    def Function_6_20EA(): pass

    label("Function_6_20EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_20F9")
    Call(0, 5)
    Return()

    label("loc_20F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 3)), scpexpr(EXPR_END)), "loc_2212")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2116")
    Call(0, 4)
    Return()

    label("loc_2116")

    TalkBegin(0xFF)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #31
        (
            "\x07\x02#40WThe Lord of Phantasma does decree...\x01",
            "#500W \x01",
            "#40W Here lies the looking glass.\x01",
            "#500W \x01",
            "#40W       Place your hand on this monument,\x01",
            "the sword-wielding dame among your number.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Jump("loc_2380")

    label("loc_2212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_231A")
    TalkBegin(0xFF)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #32
        (
            "\x07\x02#40WThe Lord of Phantasma does decree...\x01",
            "#500W \x01",
            "#40W Here lies the looking glass.\x01",
            "#500W \x01",
            "#40W       Place your hand on this monument,\x01",
            "the sword-wielding dame among your number.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Jump("loc_2380")

    label("loc_231A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_2329")
    Call(0, 3)
    Return()

    label("loc_2329")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #33
        "\x07\x05Nothing is written on the amberl monument.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_2380")

    Return()

    # Function_6_20EA end

    def Function_7_2381(): pass

    label("Function_7_2381")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-25570, 7850, -21590, 0)
    OP_67(0, 9600, -10000, 0)
    OP_6B(3590, 0)
    OP_6C(0, 0)
    OP_6E(298, 0)

    def lambda_23E4():
        OP_6D(-25570, 7850, -2740, 6500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_23E4)

    def lambda_23FC():
        OP_67(0, 7220, -10000, 6500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_23FC)

    def lambda_2414():
        OP_6B(4120, 6500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2414)

    def lambda_2424():
        OP_6C(0, 6500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_2424)

    def lambda_2434():
        OP_6E(300, 6500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2434)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(1000)
    Fade(1000)

    def lambda_245D():
        OP_6B(4000, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_245D)
    OP_22(0x117, 0x0, 0x64)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_0D()
    Sleep(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x8A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8B, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8C, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8D, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xEE, 0x0)

    def lambda_255C():
        OP_6D(-25570, 7850, -500, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_255C)

    def lambda_2574():
        OP_6B(3400, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2574)
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2B2B)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M5415   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_2381 end

    def Function_8_259E(): pass

    label("Function_8_259E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25A7")
    Return()

    label("loc_25A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 5)), scpexpr(EXPR_END)), "loc_25AF")
    Return()

    label("loc_25AF")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-24790, 0, -920, 0)
    OP_67(0, 5880, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(45000, 0)
    OP_6E(278, 0)
    SetChrPos(0xEE, -26850, 0, -2240, 0)
    SetChrPos(0xEF, -25550, 0, -2130, 0)
    SetChrPos(0xF0, -27030, 0, -3900, 0)
    SetChrPos(0xF1, -25370, 0, -3510, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2663")

    ChrTalk(    #34
        0x10F,
        "#1444F#11PMist?\x02",
    )

    CloseMessageWindow()
    Jump("loc_287C")

    label("loc_2663")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2689")

    ChrTalk(    #35
        0x101,
        "#1004F#11PMist?\x02",
    )

    CloseMessageWindow()
    Jump("loc_287C")

    label("loc_2689")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26AF")

    ChrTalk(    #36
        0x102,
        "#1504F#11PMist?\x02",
    )

    CloseMessageWindow()
    Jump("loc_287C")

    label("loc_26AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26D6")

    ChrTalk(    #37
        0x10B,
        "#213F#11PM-Mist?\x02",
    )

    CloseMessageWindow()
    Jump("loc_287C")

    label("loc_26D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26FF")

    ChrTalk(    #38
        0x110,
        "#264F#11POh, my...\x02",
    )

    CloseMessageWindow()
    Jump("loc_287C")

    label("loc_26FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2726")

    ChrTalk(    #39
        0x107,
        "#065F#11PM-Mist?\x02",
    )

    CloseMessageWindow()
    Jump("loc_287C")

    label("loc_2726")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_274B")

    ChrTalk(    #40
        0x10A,
        "#814F#11PMist?\x02",
    )

    CloseMessageWindow()
    Jump("loc_287C")

    label("loc_274B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2771")

    ChrTalk(    #41
        0x105,
        "#1164F#11PMist?\x02",
    )

    CloseMessageWindow()
    Jump("loc_287C")

    label("loc_2771")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2797")

    ChrTalk(    #42
        0x103,
        "#1523F#11PMist?\x02",
    )

    CloseMessageWindow()
    Jump("loc_287C")

    label("loc_2797")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27BC")

    ChrTalk(    #43
        0x106,
        "#052F#11PMist?\x02",
    )

    CloseMessageWindow()
    Jump("loc_287C")

    label("loc_27BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27E1")

    ChrTalk(    #44
        0x108,
        "#073F#11PMist?\x02",
    )

    CloseMessageWindow()
    Jump("loc_287C")

    label("loc_27E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2806")

    ChrTalk(    #45
        0x10E,
        "#173F#11PMist?\x02",
    )

    CloseMessageWindow()
    Jump("loc_287C")

    label("loc_2806")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2835")

    ChrTalk(    #46
        0x104,
        "#1543F#11PInteresting...\x02",
    )

    CloseMessageWindow()
    Jump("loc_287C")

    label("loc_2835")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_285A")

    ChrTalk(    #47
        0x10D,
        "#273F#11PMist?\x02",
    )

    CloseMessageWindow()
    Jump("loc_287C")

    label("loc_285A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_287C")

    ChrTalk(    #48
        0x10C,
        "#113F#11PMist?\x02",
    )

    CloseMessageWindow()

    label("loc_287C")


    ChrTalk(    #49
        0x109,
        (
            "#1065F#6PWell, once again, we're in for some fun\x01",
            "times up ahead.\x02\x03",

            "#1063FNo telling what it could be, but we'll have\x01",
            "to walk through here eventually. Just take\x01",
            "a deep breath and step inside, I guess.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B2D)
    OP_28(0x3B, 0x1, 0x8)
    OP_28(0x3B, 0x1, 0x10)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_8_259E end

    def Function_9_295F(): pass

    label("Function_9_295F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0xEE, -26720, 0, 2920, 180)
    SetChrPos(0xEF, -25360, 0, 3530, 180)
    SetChrPos(0xF0, -26760, 0, 4290, 180)
    SetChrPos(0xF1, -25240, 0, 4710, 180)
    OP_6D(-24900, 0, -1950, 0)
    OP_67(0, 7150, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(45000, 0)
    OP_6E(294, 0)
    Sleep(1000)

    def lambda_29F7():
        OP_8E(0xFE, 0xFFFF97DC, 0x0, 0xFFFFF1D2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_29F7)
    Sleep(100)

    def lambda_2A17():
        OP_8E(0xFE, 0xFFFF9D36, 0x0, 0xFFFFF146, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2A17)
    Sleep(100)

    def lambda_2A37():
        OP_8E(0xFE, 0xFFFF9778, 0x0, 0xFFFFF786, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2A37)
    Sleep(100)

    def lambda_2A57():
        OP_8E(0xFE, 0xFFFF9EC6, 0x0, 0xFFFFF74A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2A57)
    FadeToBright(2000, 0)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AB2")

    ChrTalk(    #50
        0x101,
        "#1020F#5PWha...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CA8")

    label("loc_2AB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD7")

    ChrTalk(    #51
        0x102,
        "#1502F#5P...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CA8")

    label("loc_2AD7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AFD")

    ChrTalk(    #52
        0x10B,
        "#216F#5P...Huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CA8")

    label("loc_2AFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B23")

    ChrTalk(    #53
        0x110,
        "#264F#5P...Huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CA8")

    label("loc_2B23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B4A")

    ChrTalk(    #54
        0x107,
        "#065F#5PWha...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CA8")

    label("loc_2B4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B72")

    ChrTalk(    #55
        0x10A,
        "#1317F#5PWha...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CA8")

    label("loc_2B72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B9A")

    ChrTalk(    #56
        0x105,
        "#1164F#5PWha...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CA8")

    label("loc_2B9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BC2")

    ChrTalk(    #57
        0x103,
        "#1523F#5PWha...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CA8")

    label("loc_2BC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BE9")

    ChrTalk(    #58
        0x106,
        "#055F#5PWha...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CA8")

    label("loc_2BE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C10")

    ChrTalk(    #59
        0x108,
        "#072F#5PWha...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CA8")

    label("loc_2C10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C37")

    ChrTalk(    #60
        0x10E,
        "#172F#5PWha...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CA8")

    label("loc_2C37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C5F")

    ChrTalk(    #61
        0x104,
        "#1542F#5PWha...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CA8")

    label("loc_2C5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C86")

    ChrTalk(    #62
        0x10D,
        "#270F#5P...What?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CA8")

    label("loc_2C86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CA8")

    ChrTalk(    #63
        0x10C,
        "#112F#5PWhat?!\x02",
    )

    CloseMessageWindow()

    label("loc_2CA8")


    def lambda_2CAE():
        OP_6D(-25140, 0, -5790, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2CAE)

    def lambda_2CC6():
        OP_67(0, 8070, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2CC6)

    def lambda_2CDE():
        OP_6B(3610, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_2CDE)

    def lambda_2CEE():
        OP_6E(314, 3000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_2CEE)
    OP_43(0xEE, 0x0, 0x0, 0xA)
    Sleep(150)
    OP_43(0xEF, 0x0, 0x0, 0xB)
    Sleep(200)
    OP_43(0xF0, 0x0, 0x0, 0xC)
    Sleep(150)
    OP_43(0xF1, 0x0, 0x0, 0xD)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x1)
    Fade(500)
    OP_6D(-25380, 0, -6900, 0)
    OP_67(0, 6670, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(45000, 0)
    OP_6E(279, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DE9")

    ChrTalk(    #64
        0x101,
        (
            "#1019F#5PH-How'd we end up here? We walked straight\x01",
            "in the opposite direction!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_331D")

    label("loc_2DE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E25")

    ChrTalk(    #65
        0x102,
        "#1502F#5PHow did we end up back here?\x02",
    )

    CloseMessageWindow()
    Jump("loc_331D")

    label("loc_2E25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E89")

    ChrTalk(    #66
        0x10B,
        (
            "#216F#5PH-How'd we end up here? We walked straight\x01",
            "in the opposite direction!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_331D")

    label("loc_2E89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ECC")

    ChrTalk(    #67
        0x110,
        "#1306F#5PHuh... How did we end up back here?\x02",
    )

    CloseMessageWindow()
    Jump("loc_331D")

    label("loc_2ECC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F30")

    ChrTalk(    #68
        0x107,
        (
            "#065F#5PH-How'd we end up here? We walked straight\x01",
            "in the opposite direction!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_331D")

    label("loc_2F30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F95")

    ChrTalk(    #69
        0x10A,
        (
            "#1317F#5PH-How'd we end up here? We walked straight\x01",
            "in the opposite direction!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_331D")

    label("loc_2F95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3001")

    ChrTalk(    #70
        0x105,
        (
            "#1163F#5PWe walked straight in the opposite direction...\x01",
            "How did we end up back here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_331D")

    label("loc_3001")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_306D")

    ChrTalk(    #71
        0x103,
        (
            "#1522F#5PWe walked straight in the opposite direction...\x01",
            "How did we end up back here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_331D")

    label("loc_306D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30E0")

    ChrTalk(    #72
        0x106,
        (
            "#055F#5PThe hell? We walked straight in the opposite\x01",
            "direction... How'd we end up back here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_331D")

    label("loc_30E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_314B")

    ChrTalk(    #73
        0x108,
        (
            "#072F#5PWe walked straight in the opposite direction...\x01",
            "How did we end up back here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_331D")

    label("loc_314B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31C3")

    ChrTalk(    #74
        0x10E,
        (
            "#178F#5PImpossible... We walked straight in the opposite \x01",
            "direction! How did we end up back here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_331D")

    label("loc_31C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3238")

    ChrTalk(    #75
        0x104,
        (
            "#1540F#5PStrange... We walked straight in the opposite\x01",
            "direction. How did we end up back here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_331D")

    label("loc_3238")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32AC")

    ChrTalk(    #76
        0x10D,
        (
            "#270F#5PStrange... We walked straight in the opposite\x01",
            "direction. How did we end up back here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_331D")

    label("loc_32AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_331D")

    ChrTalk(    #77
        0x10C,
        (
            "#112F#5PStrange... We walked straight in the opposite\x01",
            "direction. How did we end up back here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_331D")


    ChrTalk(    #78
        0x109,
        (
            "#1063F#6P...It looks like there's some kind of condition\x01",
            "for advancing into the next area in this case,\x01",
            "too.\x02\x03",

            "#1067F...\x02\x03",

            "#1065FI think we might actually need to have Ries\x01",
            "with us.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33FE")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3465")

    label("loc_33FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3426")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3465")

    label("loc_3426")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_344E")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3465")

    label("loc_344E")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3465")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3492")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_34F9")

    label("loc_3492")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34BA")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_34F9")

    label("loc_34BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34E2")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_34F9")

    label("loc_34E2")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_34F9")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3526")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_358D")

    label("loc_3526")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_354E")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_358D")

    label("loc_354E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3576")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_358D")

    label("loc_3576")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_358D")

    Sleep(1000)

    def lambda_3598():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3598)
    Sleep(100)

    def lambda_35AB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_35AB)
    Sleep(100)
    OP_8C(0xF1, 225, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35E5")

    ChrTalk(    #79
        0x107,
        "#064F#5PRies?\x02",
    )

    CloseMessageWindow()

    label("loc_35E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_360D")

    ChrTalk(    #80
        0x110,
        "#1305F#5PDo we, now?\x02",
    )

    CloseMessageWindow()

    label("loc_360D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3634")

    ChrTalk(    #81
        0x101,
        "#1004F#5PR-Ries?\x02",
    )

    CloseMessageWindow()
    Jump("loc_367D")

    label("loc_3634")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_365A")

    ChrTalk(    #82
        0x10B,
        "#212F#5PR-Ries?\x02",
    )

    CloseMessageWindow()
    Jump("loc_367D")

    label("loc_365A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_367D")

    ChrTalk(    #83
        0x10A,
        "#814F#5PR-Ries?\x02",
    )

    CloseMessageWindow()

    label("loc_367D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36AA")

    ChrTalk(    #84
        0x102,
        "#1504F#5PHow come her?\x02",
    )

    CloseMessageWindow()
    Jump("loc_36D4")

    label("loc_36AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36D4")

    ChrTalk(    #85
        0x105,
        "#1163F#5PHow come her?\x02",
    )

    CloseMessageWindow()

    label("loc_36D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3711")

    ChrTalk(    #86
        0x103,
        "#1522F#5PDid you figure something out?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3876")

    label("loc_3711")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3749")

    ChrTalk(    #87
        0x106,
        "#555F#5PYou figure somethin' out?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3876")

    label("loc_3749")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3788")

    ChrTalk(    #88
        0x108,
        "#072F#5PThink you figured something out?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3876")

    label("loc_3788")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37C4")

    ChrTalk(    #89
        0x10E,
        "#178F#5PDid you figure something out?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3876")

    label("loc_37C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3801")

    ChrTalk(    #90
        0x104,
        "#1540F#5PDid you figure something out?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3876")

    label("loc_3801")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_383D")

    ChrTalk(    #91
        0x10D,
        "#270F#5PDid you figure something out?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3876")

    label("loc_383D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3876")

    ChrTalk(    #92
        0x10C,
        "#112F#5PDid you figure something out?\x02",
    )

    CloseMessageWindow()

    label("loc_3876")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3992")

    ChrTalk(    #93
        0x109,
        (
            "#1075F#6PIf my other theory is right--and I think it is--\x01",
            "this is a fairly safe deduction to make.\x02\x03",

            "#1840FStill, the fastest way to be sure is to give this\x01",
            "a whirl. Let's get Ries and have her come with\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A66")

    label("loc_3992")


    ChrTalk(    #94
        0x109,
        (
            "#1075F#6PIf my other theory is right--and I think it is--\x01",
            "this is a fairly safe deduction to make.\x02\x03",

            "#1840FStill, the fastest way to be sure is to give this\x01",
            "a whirl. Let's get Ries and have her come with\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A66")

    OP_A2(0x2B2C)
    OP_28(0x3B, 0x1, 0x20)
    OP_28(0x3B, 0x1, 0x40)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_9_295F end

    def Function_10_3A7D(): pass

    label("Function_10_3A7D")

    OP_8E(0xFE, 0xFFFF9606, 0x0, 0xFFFFDE86, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Sleep(600)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_10_3A7D end

    def Function_11_3AB1(): pass

    label("Function_11_3AB1")

    OP_8E(0xFE, 0xFFFF9BF6, 0x0, 0xFFFFDF1C, 0x7D0, 0x0)
    Sleep(100)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(300)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_11_3AB1 end

    def Function_12_3AEA(): pass

    label("Function_12_3AEA")

    OP_8E(0xFE, 0xFFFF95C0, 0x0, 0xFFFFE3F4, 0x7D0, 0x0)
    Sleep(100)
    OP_8C(0xFE, 315, 400)
    Sleep(400)
    OP_8C(0xFE, 270, 400)
    Sleep(700)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_12_3AEA end

    def Function_13_3B23(): pass

    label("Function_13_3B23")

    OP_8E(0xFE, 0xFFFF9CC8, 0x0, 0xFFFFE520, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 90, 400)
    Sleep(300)
    OP_8C(0xFE, 135, 400)
    Sleep(600)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_13_3B23 end

    def Function_14_3B5C(): pass

    label("Function_14_3B5C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0xEE, -26720, 0, 2920, 180)
    SetChrPos(0xEF, -25360, 0, 3530, 180)
    SetChrPos(0xF0, -26760, 0, 4290, 180)
    SetChrPos(0xF1, -25240, 0, 4710, 180)
    OP_6D(-24900, 0, -1950, 0)
    OP_67(0, 7150, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(45000, 0)
    OP_6E(284, 0)

    def lambda_3BEF():
        OP_8E(0xFE, 0xFFFF97DC, 0x0, 0xFFFFF1D2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3BEF)
    Sleep(100)

    def lambda_3C0F():
        OP_8E(0xFE, 0xFFFF9D36, 0x0, 0xFFFFF146, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_3C0F)
    Sleep(100)

    def lambda_3C2F():
        OP_8E(0xFE, 0xFFFF9778, 0x0, 0xFFFFF786, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_3C2F)
    Sleep(100)

    def lambda_3C4F():
        OP_8E(0xFE, 0xFFFF9EC6, 0x0, 0xFFFFF74A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_3C4F)
    FadeToBright(2000, 0)
    WaitChrThread(0xEE, 0x0)

    def lambda_3C78():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_3C78)
    WaitChrThread(0xEF, 0x0)

    def lambda_3C8B():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3C8B)
    WaitChrThread(0xF0, 0x0)

    def lambda_3C9E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_3C9E)
    WaitChrThread(0xF1, 0x0)

    def lambda_3CB1():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_3CB1)
    OP_0D()
    Sleep(500)

    ChrTalk(    #95
        0x109,
        (
            "#1065F#6PIf my other theory is right--and I think it is--\x01",
            "then we're gonna need Ries to go farther.\x02\x03",

            "#1063FLet's head back to the garden.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_14_3B5C end

    def Function_15_3D56(): pass

    label("Function_15_3D56")

    EventBegin(0x1)
    SetMapFlags(0x80)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(1000, 16777215, -1)

    def lambda_3D76():
        OP_90(0x0, 0x0, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3D76)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_0D()
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DDA")
    NewScene("ED6_DT21/P7000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3E17")

    label("loc_3DDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DF4")
    NewScene("ED6_DT21/P7000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3E17")

    label("loc_3DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E0B")
    OP_A2(0x2506)
    NewScene("ED6_DT21/M4111   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3E17")

    label("loc_3E0B")

    OP_A2(0x2507)
    NewScene("ED6_DT21/M4111   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3E17")

    Return()

    # Function_15_3D56 end

    def Function_16_3E18(): pass

    label("Function_16_3E18")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 12090, 0, -52300, 45)
    SetChrPos(0x1, 12090, 0, -52300, 45)
    SetChrPos(0x2, 12090, 0, -52300, 45)
    SetChrPos(0x3, 12090, 0, -52300, 45)
    OP_69(0x0, 0x0)
    OP_6C(270000, 0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 17)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_16_3E18 end

    def Function_17_3EFF(): pass

    label("Function_17_3EFF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F28")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3F1C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3F1C)

    label("loc_3F28")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F51")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3F45():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3F45)

    label("loc_3F51")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F7A")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3F6E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3F6E)

    label("loc_3F7A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FA3")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3F97():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3F97)

    label("loc_3FA3")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FCF")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3FCF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FE6")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3FE6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FFD")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3FFD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4014")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4014")

    Return()

    # Function_17_3EFF end

    def Function_18_4015(): pass

    label("Function_18_4015")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40EE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x299, 1)"), scpexpr(EXPR_END)), "loc_4083")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #96
        "\x07\x05Found \x1F\x99\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B9D)
    Jump("loc_40EB")

    label("loc_4083")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #97
        (
            "\x07\x05Found \x1F\x99\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x99\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_40EB")

    Jump("loc_4173")

    label("loc_40EE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #98
        (
            "\x07\x05Isn't this the part where you give me something in exchange? Y'know...\x01",
            "like a decent human being?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x3B, 0x0)

    label("loc_4173")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_18_4015 end

    def Function_19_4181(): pass

    label("Function_19_4181")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #99
        (
            "\x07\x05North: Erbe Royal Villa\x01",
            "West: Sanktheim Gate        224 selge\x01",
            "East: Gurune Gate           256 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_4181 end

    SaveToFile()

Try(main)
