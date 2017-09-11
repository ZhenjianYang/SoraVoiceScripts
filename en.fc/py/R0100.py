from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R0100   ._SN',
        MapName             = 'Rolent',
        Location            = 'R0100.x',
        MapIndex            = 23,
        MapDefaultBGM       = "ed60020",
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
        'Rolent',                               # 9
        'Bright Family House',                  # 10
        'Gurune Gate',                          # 11
    )

    DeclEntryPoint(
        Unknown_00              = -35000,
        Unknown_04              = 1000,
        Unknown_08              = 144000,
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
        Unknown_3A              = 23,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10020 ._CH',             # 00
        'ED6_DT09/CH10021 ._CH',             # 01
        'ED6_DT09/CH10180 ._CH',             # 02
        'ED6_DT09/CH10181 ._CH',             # 03
        'ED6_DT09/CH10260 ._CH',             # 04
        'ED6_DT09/CH10261 ._CH',             # 05
        'ED6_DT09/CH10210 ._CH',             # 06
        'ED6_DT09/CH10211 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10020P._CP',             # 00
        'ED6_DT09/CH10021P._CP',             # 01
        'ED6_DT09/CH10180P._CP',             # 02
        'ED6_DT09/CH10181P._CP',             # 03
        'ED6_DT09/CH10260P._CP',             # 04
        'ED6_DT09/CH10261P._CP',             # 05
        'ED6_DT09/CH10210P._CP',             # 06
        'ED6_DT09/CH10211P._CP',             # 07
    )

    DeclNpc(
        X                   = -14030,
        Z                   = 1000,
        Y                   = 217340,
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
        X                   = -60890,
        Z                   = 1030,
        Y                   = 216800,
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
        X                   = -39320,
        Z                   = 1000,
        Y                   = 90280,
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


    DeclActor(
        TriggerX            = -36800,
        TriggerZ            = 1000,
        TriggerY            = 152300,
        TriggerRange        = 1500,
        ActorX              = -36800,
        ActorZ              = 2500,
        ActorY              = 152800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -39100,
        TriggerZ            = 1000,
        TriggerY            = 153300,
        TriggerRange        = 1500,
        ActorX              = -39100,
        ActorZ              = 2200,
        ActorY              = 153300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_192",          # 00, 0
        "Function_1_20B",          # 01, 1
        "Function_2_24C",          # 02, 2
        "Function_3_2B6",          # 03, 3
        "Function_4_2FB",          # 04, 4
        "Function_5_A73",          # 05, 5
        "Function_6_AA2",          # 06, 6
        "Function_7_AD1",          # 07, 7
    )


    def Function_0_192(): pass

    label("Function_0_192")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_19E"),
        (SWITCH_DEFAULT, "loc_20A"),
    )


    label("loc_19E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA")
    Return()

    label("loc_1AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(-14000, 1000, 197160, 0)
    SetChrPos(0x102, -13816, 1000, 198240, 180)
    SetChrPos(0x101, -14816, 1000, 199400, 180)
    OP_6C(40000, 0)
    SetMapFlags(0x400000)
    FadeToBright(500, 0)
    Event(0, 4)

    label("loc_207")

    Jump("loc_20A")

    label("loc_20A")

    Return()

    # Function_0_192 end

    def Function_1_20B(): pass

    label("Function_1_20B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_223")
    OP_B1("R0100_y")
    Jump("loc_22C")

    label("loc_223")

    OP_B1("R0100_n")

    label("loc_22C")

    OP_16(0x2, 0xFA0, 0xFFFD7F60, 0x6D60, 0x30008)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B")
    OP_1B(0x2, 0x0, 0x7)

    label("loc_24B")

    Return()

    # Function_1_20B end

    def Function_2_24C(): pass

    label("Function_2_24C")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "\x07\x05North: Rolent - 49 selge\x01",
            "South: Gurune Gate - 259 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_2_24C end

    def Function_3_2B6(): pass

    label("Function_3_2B6")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "\x07\x05West: Bright House\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_3_2B6 end

    def Function_4_2FB(): pass

    label("Function_4_2FB")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_43(0x101, 0x0, 0x0, 0x5)
    OP_43(0x102, 0x0, 0x0, 0x6)
    OP_A2(0x0)
    OP_A2(0x1)

    def lambda_31C():
        OP_6D(-13905, 1000, 185268, 4500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31C)
    OP_A5(0x0)

    ChrTalk(    #2
        0x101,
        "#003FHey, Joshua...\x02",
    )

    CloseMessageWindow()
    OP_A5(0x1)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #3
        0x102,
        "#010FHmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#003F...\x02\x03",

            "#003FDo you think...I'm really cut\x01",
            "out to be a bracer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#010F...\x02\x03",

            "#015FWell, you seem to have inherited\x01",
            "your father's skill with a staff...\x02\x03",

            "#015FAnd your nosy personality\x01",
            "doesn't let you ignore someone\x01",
            "in distress...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#008FReally? You think so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#010FSure, but why are you asking?\x01",
            "Are you still thinking about what\x01",
            "happened back at the Tower?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#003FYeah...\x02\x03",

            "#003FBecause of my carelessness,\x01",
            "Luke almost got caught in the\x01",
            "middle of a dangerous situation.\x02\x03",

            "#003FIf Dad hadn't come when he did,\x01",
            "he could have been seriously\x01",
            "injured.\x02\x03",

            "#003FI guess I'm just worried about\x01",
            "whether or not I'll be able to stay\x01",
            "on top of things in the future...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#010F...\x02\x03",

            "#019FThat kind of talk doesn't sound\x01",
            "like the Estelle I know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x102,
        (
            "#010FIf we fail today, then all that's\x01",
            "left to do is take back our losses\x01",
            "tomorrow, right?\x02\x03",

            "#010FOverthinking and worrying about\x01",
            "things that haven't happened yet\x01",
            "is definitely not like you.\x02\x03",

            "#010FIsn't being a bracer what you've always dreamed of?\x01",
            "How can you expect to succeed if you let something\x01",
            "like what happened today discourage you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#003FJoshua...\x02\x03",

            "#500F...\x02\x03",

            "#500FYou're right...\x02\x03",

            "#006FThis isn't like me at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x102,
        (
            "#011FI don't think a serious expression\x01",
            "really suits your face either.\x02\x03",

            "#011FYou laughing like a big ditz is\x01",
            "far more natural for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#009FHey, what's that supposed\x01",
            "to mean?!\x02\x03",

            "#009FYou're gonna see my 'angry\x01",
            "expression' if you keep that\x01",
            "up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x102,
        (
            "#019FHa ha...okay. I admit that last\x01",
            "comment was pushing things\x01",
            "a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#000FI'll overlook it this time...\x01",
            "And...thanks for cheering me up.\x02\x03",

            "#001FI don't know about you, but I'm\x01",
            "sooo ready to get home and eat.\x02\x03",

            "#001FMy stomach just started growling\x01",
            "like a bear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        (
            "#010F(Maybe 'glutton' is closer to the\x01",
            "mark than 'ditz'...)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_A2(0x218)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    SetMapFlags(0x1)
    Return()

    # Function_4_2FB end

    def Function_5_A73(): pass

    label("Function_5_A73")

    OP_A6(0x0)
    OP_8E(0xFE, 0xFFFFC729, 0x0, 0x2D7BD, 0xBB8, 0x0)
    OP_A3(0x0)
    OP_A6(0x0)
    OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
    OP_A3(0x0)
    Return()

    # Function_5_A73 end

    def Function_6_AA2(): pass

    label("Function_6_AA2")

    OP_A6(0x1)
    OP_8E(0xFE, 0xFFFFCB34, 0x0, 0x2D073, 0xBB8, 0x0)
    OP_A3(0x1)
    OP_A6(0x1)
    OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
    OP_A3(0x1)
    Return()

    # Function_6_AA2 end

    def Function_7_AD1(): pass

    label("Function_7_AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CBD")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_B5F")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #18
        0x102,
        (
            "#010FIt's getting late.\x02\x03",

            "#010FI'm sure Dad's waiting for us,\x01",
            "so let's head home.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #19
        0x101,
        "#000FRoger that!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CA2")

    label("loc_B5F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2C")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #20
        0x102,
        (
            "#014FEstelle, Rolent City is in the\x01",
            "opposite direction.\x02\x03",

            "You're not sleepwalking again,\x01",
            "are you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #21
        0x101,
        (
            "#009FHow about you just be quiet and\x01",
            "keep your comments to yourself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA2")

    label("loc_C2C")


    ChrTalk(    #22
        0x102,
        (
            "#012F(This way leads to the Royal City\x01",
            "of Grancel... We've got to head the\x01",
            "opposite way if we're going to town.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA2")

    OP_90(0x0, 0x0, 0x0, 0x9C4, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_CBD")

    Return()

    # Function_7_AD1 end

    SaveToFile()

Try(main)
